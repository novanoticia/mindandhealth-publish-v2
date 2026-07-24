# Changelog — mindandhealth-publish-v2

## 2.0 (2026-07-24) — duplicado auditado y mejorado del plugin original (2026-04-16)

Base: versión plugin `mindandhealth-publish` (abr-2026), auditada con `github-plugin-analyzer-ia-v4` e incorporando las mejoras que la rama user (jun-2026) ya había introducido, más correcciones nuevas.

- **[QW1 · F2]** Ratio de imagen normalizado **1570:881 → 1570:880** en los 16 puntos del árbol (SKILL.md, banner-spec, linkedin-newsletter, generate, pipeline), alineado con la rama más reciente y la preferencia registrada del autor. `derivatives/banner-spec.md` declarado **fuente canónica** del valor.
- **[QW2 · F3]** Eliminada la ruta absoluta del vault de iCloud codificada en SKILL.md. Sustituida por un **gate de entorno**: con filesystem (Code/Desktop/Cowork) se puede leer el vault; sin él (claude.ai, Perplexity), se piden títulos/textos a Pablo. Prohibido inventar existencia o URL de artículos.
- **[QW3 · F5]** URLs del pie ético normalizadas a la convención **sin `www`** declarada en `mapa-tematico.md` (la variante EN resuelve verificadamente sin www). ⚠️ Pendiente de verificación humana: que el slug ES `manifiesto-editorial-etico-mindandhealth.org` resuelva en el navegador.
- **[QW4 · F6]** `pie-etico.md`: las plantillas pasan a **anclas** con protocolo de **variación controlada** (4 invariantes + redacción fresca por artículo), fusionando el enfoque de la rama user sin perder el contenido valioso de las plantillas (política de ética, no-financiación, marcos UNESCO/OdiseIA/APA/CAIDP).
- **[CM1 · F1]** Renombrado a `mindandhealth-publish-v2` + `metadata.version` + este CHANGELOG, para poder **consolidar** las dos versiones divergentes que coexistían (plugin abr / user jun) sin crear una tercera ambigüedad. Tras validar v2: desinstalar el plugin antiguo y archivar la rama user.
- **[CM2]** Nueva `references/orquestacion-modelos.md`: delegación opcional a **subagente frontera** en entornos con orquestación (Claude Code / Cowork), con gate de entorno, fallback = primario, contrato heredado y degradación elegante declarada. Compatible con `/alternancia-modelos`.
- **[F7]** SKILL.md deja de duplicar el protocolo de carriles completo: `modo-iterativo-canvas.md` es la fuente canónica declarada (la tabla del SKILL.md queda como resumen operativo).
- **Higiene:** nota de **vigencia/snapshot** en `mapa-tematico.md` (anti-alucinación de enlaces internos); typo «tematicas» corregido; description reescrita con triggers explícitos (<1024 bytes UTF-8, portable a Perplexity).

Sin cambios de contenido en: `modes/conversar.md`, `modes/refine.md`, `references/voz-editorial.md`, `references/estructura-yaml.md`, `derivatives/linkedin-feed.md`.
