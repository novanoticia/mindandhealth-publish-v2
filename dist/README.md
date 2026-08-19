# /dist — skill descargable (fuera del sistema de plugins)

Esta carpeta existe para **clientes que no soportan marketplaces de plugins de Claude** pero sí la [Agent Skills Specification](https://agentskills.io/specification) abierta — hoy: **Mistral (Vibe Work)** y **Perplexity (Spaces / Computer)**. Ambos leen exactamente el mismo formato de carpeta (`SKILL.md` con frontmatter YAML + subcarpetas de contenido) que ya usa este repositorio; no ha hecho falta reescribir nada, solo hacerlo descargable como archivo suelto, ya que el marketplace de plugins lo anida bajo `plugins/.../skills/`.

## Qué descargar

Un único paquete sirve para todos los clientes:

| Archivo | Para quién |
|---|---|
| **`mindandhealth-publish-v2.zip`** | Perplexity, Mistral, y cualquier cliente estándar de la Agent Skills Spec |
| **`mindandhealth-publish-v2.skill`** | claude.ai (Ajustes → Capacidades → Skills → Subir skill) — idéntico al `.zip`, solo cambia la extensión |

Contienen la carpeta `mindandhealth-publish-v2/` con `SKILL.md` en su raíz — el nombre de la carpeta coincide con el campo `name:` del frontmatter, como exige la especificación.

## Cómo instalar

**Perplexity (Space o Computer):** en el Space, *Add Sources* → sube **todos** los archivos de `mindandhealth-publish-v2.zip` descomprimido (no solo `SKILL.md`), o en Computer: *Skills → + Create skill* y sube el `.zip`.

**Mistral / Vibe Work:** el `.zip` es 100% válido tal cual — Mistral solo pide, en el propio formulario de instalación, acortar el campo `description` a menos de 500 caracteres (la spec abierta permite hasta 1024, y así viene por defecto para el resto de clientes). **No existe una copia distinta del zip para esto**: al instalar, pega en el formulario esta versión ya recortada de la description en lugar de la que trae el archivo:

> Acompañamiento editorial conversacional para publicaciones de Pablo en mindandhealth.org. La conversación cristaliza en un canvas markdown iterativo en el chat (nunca escribe en el vault de Obsidian) y derivados bajo petición: newsletter LinkedIn, post de feed, prompt de imagen 1570:880. Actívalo con /mindandhealth-publish-v2 o frases como "pensemos sobre X", "saca canvas", o al pedir crear, refinar o transformar contenido para su web.

(439 caracteres.) El resto del skill —`SKILL.md`, `modes/`, `references/`, `derivatives/`— se sube sin tocar.

**claude.ai (sin plugins):** sube `mindandhealth-publish-v2.skill` en Ajustes → Capacidades → Skills.

> Si usas Claude con soporte de plugins, **no uses esta carpeta**: instala vía marketplace como se explica en el [README principal](../README.md) — obtienes sincronización automática con este repositorio, algo que ninguna de estas descargas sueltas ofrece.

## Mantenimiento

La **fuente canónica** del skill es `plugins/mindandhealth-publish-v2/skills/mindandhealth-publish-v2/`. Estos paquetes son **instantáneas manuales** de esa carpeta, regeneradas en cada release relevante; si el skill cambia y no se regeneran, quedan desactualizados — no hay sincronización automática fuera del marketplace de plugins.

Por eso aquí solo viven los paquetes comprimidos y no una copia descomprimida del skill: una segunda carpeta con su propio `SKILL.md` haría que cualquier herramienta que recorra el repositorio encontrase **dos skills declarando el mismo `name`** y abortase, ya que dos skills no pueden reclamar el mismo nombre publicado. Para leer el contenido, ve a la fuente canónica; para instalarlo, descarga el paquete.

---

*Generado con asistencia de IA. Requiere revisión humana antes de publicarse como release.*
