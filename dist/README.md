# /dist — skill descargable (fuera del sistema de plugins)

Esta carpeta existe para **clientes que no soportan marketplaces de plugins de Claude** pero sí la [Agent Skills Specification](https://agentskills.io/specification) abierta — hoy: **Mistral (Vibe Work)** y **Perplexity (Spaces / Computer)**. Ambos leen exactamente el mismo formato de carpeta (`SKILL.md` con frontmatter YAML + subcarpetas de contenido) que ya usa este repositorio; no ha hecho falta reescribir nada, solo hacerlo descargable como archivo suelto, ya que el marketplace de plugins lo anida bajo `plugins/.../skills/`.

## Qué descargar

| Archivo | Para quién | Diferencia |
|---|---|---|
| **`mindandhealth-publish-v2.zip`** | Perplexity, y cualquier cliente estándar de la Agent Skills Spec | `description` completa (665 car.) |
| **`mindandhealth-publish-v2.skill`** | claude.ai (Ajustes → Capacidades → Skills → Subir skill) | Idéntico al `.zip` anterior; solo cambia la extensión |
| **`mindandhealth-publish-v2-mistral.zip`** | Mistral / Vibe Work | `description` recortada a ≤450 caracteres (439 car. / 443 bytes UTF-8) |

Los tres contienen la carpeta `mindandhealth-publish-v2/` con `SKILL.md` en su raíz — el nombre de la carpeta coincide con el campo `name:` del frontmatter, como exige la especificación.

## Por qué existe la variante Mistral

La spec abierta permite `description` de hasta 1024 caracteres, y así la usan Claude y Perplexity. Mistral, en la práctica, trabaja mejor con descripciones más cortas (~450 caracteres); por eso hay una segunda copia con la misma `description` comprimida a lo esencial — qué hace y cuándo activarse — sin las frases-ejemplo redundantes de la versión larga. El resto del skill (instrucciones, `modes/`, `references/`, `derivatives/`) es **idéntico byte a byte** en las tres variantes.

## Cómo instalar

**Perplexity (Space o Computer):** en el Space, *Add Sources* → sube **todos** los archivos de `mindandhealth-publish-v2.zip` descomprimido (no solo `SKILL.md`), o en Computer: *Skills → + Create skill* y sube el `.zip`.

**Mistral / Vibe Work:** copia la carpeta descomprimida de `mindandhealth-publish-v2-mistral.zip` a `~/.vibe/skills/` (nivel usuario) o `./.vibe/skills/` (nivel proyecto), o usa el flujo *New Skill* de la interfaz.

**claude.ai (sin plugins):** sube `mindandhealth-publish-v2.skill` en Ajustes → Capacidades → Skills.

> Si usas Claude con soporte de plugins, **no uses esta carpeta**: instala vía marketplace como se explica en el [README principal](../README.md) — obtienes sincronización automática con este repositorio, algo que ninguna de estas descargas sueltas ofrece.

## Mantenimiento

Estos zips son una **instantánea manual** del skill en `plugins/mindandhealth-publish-v2/skills/mindandhealth-publish-v2/`, generada en cada release relevante. Si el skill cambia y esta carpeta no se regenera, quedará desactualizada — no hay sincronización automática fuera del marketplace de plugins.

---

*Generado con asistencia de IA. Requiere revisión humana antes de publicarse como release.*
