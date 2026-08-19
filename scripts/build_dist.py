#!/usr/bin/env python3
"""
Valida el skill y regenera los paquetes de /dist.

    python3 scripts/build_dist.py           # valida y regenera si hace falta
    python3 scripts/build_dist.py --check   # solo valida; falla si /dist está desactualizado

Fuente canónica: plugins/<PLUGIN>/skills/<SKILL>/
Salida:          dist/<SKILL>.zip  y  dist/<SKILL>.skill (copia idéntica, otra extensión)

Los paquetes se generan de forma REPRODUCIBLE (marca de tiempo fija y orden
alfabético), así que dos ejecuciones con el mismo contenido producen bytes
idénticos. Eso es lo que permite detectar si /dist está al día comparando
hashes, sin falsos positivos por la fecha de checkout.
"""

import argparse
import hashlib
import json
import pathlib
import sys
import zipfile

import yaml

SKILL_NAME = "mindandhealth-publish-v2"
SRC = pathlib.Path(f"plugins/{SKILL_NAME}/skills/{SKILL_NAME}")
DIST = pathlib.Path("dist")
MANIFIESTOS = [
    pathlib.Path(".claude-plugin/marketplace.json"),
    pathlib.Path(f"plugins/{SKILL_NAME}/plugin.json"),
    pathlib.Path(f"plugins/{SKILL_NAME}/.claude-plugin/plugin.json"),
]

# Fecha fija dentro del zip (reproducibilidad). No es la fecha del release.
MTIME_FIJA = (2020, 1, 1, 0, 0, 0)

# Límites de la Agent Skills Specification y de los clientes.
MAX_BYTES_DESCRIPTION = 1024   # spec abierta: error duro por encima
AVISO_CHARS_MISTRAL = 500      # Mistral valida en caracteres, no en bytes

errores: list[str] = []
avisos: list[str] = []


def frontmatter(p: pathlib.Path) -> dict:
    texto = p.read_text(encoding="utf-8")
    if not texto.startswith("---"):
        errores.append(f"{p}: no empieza con el delimitador '---' del frontmatter")
        return {}
    try:
        return yaml.safe_load(texto.split("---")[1]) or {}
    except yaml.YAMLError as e:
        errores.append(f"{p}: frontmatter YAML ilegible ({e})")
        return {}


def versiones_de(p: pathlib.Path) -> list[tuple[str, str]]:
    """Todas las versiones declaradas en un manifiesto, con su ubicación."""
    datos = json.loads(p.read_text(encoding="utf-8"))
    out = []
    if "version" in datos:
        out.append((f"{p}", datos["version"]))
    for i, plug in enumerate(datos.get("plugins", [])):
        if "version" in plug:
            out.append((f"{p} → plugins[{i}]", plug["version"]))
    return out


def validar() -> str:
    """Comprobaciones previas al empaquetado. Devuelve la versión declarada."""
    if not SRC.is_dir():
        errores.append(f"no existe la carpeta fuente {SRC}")
        return ""

    # 1. Un único SKILL.md en todo el repositorio.
    #    Dos skills no pueden reclamar el mismo `name` publicado: cualquier
    #    conversor o validador que recorra el árbol completo aborta.
    encontrados = sorted(
        p for p in pathlib.Path(".").rglob("SKILL.md") if ".git/" not in str(p)
    )
    if len(encontrados) != 1:
        errores.append(
            "el repositorio declara "
            f"{len(encontrados)} SKILL.md ({', '.join(map(str, encontrados))}); "
            "debe haber exactamente uno. Si es una copia de distribución, "
            "empaquétala en /dist en lugar de dejarla descomprimida."
        )

    fm = frontmatter(SRC / "SKILL.md")
    if not fm:
        return ""

    # 2. El `name` coincide con la carpeta (lo exige la spec para el bundle).
    if fm.get("name") != SKILL_NAME:
        errores.append(
            f"SKILL.md declara name={fm.get('name')!r} pero la carpeta es {SKILL_NAME!r}"
        )

    # 3. Frontmatter sin claves inventadas: los clientes fallan con error duro.
    permitidas = {"name", "description", "license", "allowed-tools", "metadata"}
    if sobran := set(fm) - permitidas:
        errores.append(f"claves no permitidas en el frontmatter: {sorted(sobran)}")

    # 4. Longitud de description.
    desc = fm.get("description", "")
    if len(desc.encode("utf-8")) > MAX_BYTES_DESCRIPTION:
        errores.append(
            f"description: {len(desc.encode())} bytes UTF-8, "
            f"por encima del máximo de {MAX_BYTES_DESCRIPTION} de la spec"
        )
    if len(desc) > AVISO_CHARS_MISTRAL:
        avisos.append(
            f"description: {len(desc)} caracteres. Mistral valida en caracteres "
            f"(límite {AVISO_CHARS_MISTRAL}): habrá que acortarla a mano al instalar allí. "
            "El texto ya recortado está en dist/README.md."
        )

    # 5. Coherencia de versiones entre el skill y los manifiestos.
    version = str((fm.get("metadata") or {}).get("version", ""))
    if not version:
        errores.append("SKILL.md no declara metadata.version")
    elif version.count(".") != 2:
        errores.append(f"metadata.version={version!r} no es SemVer completo (mayor.menor.parche)")

    for m in MANIFIESTOS:
        if not m.exists():
            errores.append(f"falta el manifiesto {m}")
            continue
        try:
            for donde, v in versiones_de(m):
                if version and v != version:
                    errores.append(f"{donde}: version={v!r}, pero el skill declara {version!r}")
        except json.JSONDecodeError as e:
            errores.append(f"{m}: JSON inválido ({e})")

    return version


def construir_zip() -> bytes:
    """Empaqueta la fuente de forma reproducible y devuelve los bytes."""
    import io

    buffer = io.BytesIO()
    archivos = sorted(p for p in SRC.rglob("*") if p.is_file() and p.name != ".DS_Store")
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
        for f in archivos:
            info = zipfile.ZipInfo(f"{SKILL_NAME}/{f.relative_to(SRC).as_posix()}", MTIME_FIJA)
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, f.read_bytes())
    return buffer.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="no escribe nada; falla si /dist no coincide con la fuente")
    args = ap.parse_args()

    version = validar()
    if errores:
        print("✗ Validación fallida:\n" + "\n".join(f"  · {e}" for e in errores), file=sys.stderr)
        return 1

    nuevo = construir_zip()
    huella = hashlib.sha256(nuevo).hexdigest()[:12]
    destinos = [DIST / f"{SKILL_NAME}.zip", DIST / f"{SKILL_NAME}.skill"]
    desfasados = [d for d in destinos if not d.exists() or d.read_bytes() != nuevo]

    n = sum(1 for p in SRC.rglob("*") if p.is_file())
    print(f"  skill {SKILL_NAME} v{version} · {n} archivos · sha256:{huella}")
    for a in avisos:
        print(f"  ⚠ {a}")

    if not desfasados:
        print("✓ /dist está al día.")
        return 0

    if args.check:
        print("✗ /dist está desactualizado respecto a la fuente: "
              + ", ".join(str(d) for d in desfasados), file=sys.stderr)
        print("  Ejecuta scripts/build_dist.py (o deja que lo haga el workflow al fusionar).",
              file=sys.stderr)
        return 1

    DIST.mkdir(exist_ok=True)
    for d in desfasados:
        d.write_bytes(nuevo)
        print(f"↻ regenerado {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())