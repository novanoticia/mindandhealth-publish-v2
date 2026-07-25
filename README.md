# mindandhealth-publish-v2

*Conversational editorial companion skill for Claude — Spanish-first. Ideas crystallize through dialogue into an iterative markdown canvas; the skill never writes to the author's vault.*

Skill de **acompañamiento editorial conversacional** para [Claude](https://claude.com) al servicio de las publicaciones de [mindandhealth.org](https://mindandhealth.org) (Obsidian Publish). Su premisa de diseño: **los artículos no se piden, emergen**. El skill no redacta a demanda; conversa, y solo cuando la conversación cristaliza abre un borrador iterable.

Este repositorio es, además, un **marketplace de plugins de Claude**: contiene el manifiesto `.claude-plugin/marketplace.json` que permite instalarlo directamente desde los ajustes de Claude y mantenerlo sincronizado con cada cambio publicado aquí.

## Cómo funciona

1. **Conversación exploratoria** (modo por defecto). Tema, intuición, duda o lectura. El skill actúa como interlocutor transdisciplinar: contraargumenta, matiza, propone metáforas y referencias.
2. **Cristalización.** Cuando hay tesis, ideas fuerza y una metáfora con peso, el autor pide canvas — o el skill lo sugiere una única vez, sin insistir.
3. **Canvas.** Un bloque markdown vivo *dentro del chat* que recoge lo destilado. No es un archivo en disco.
4. **Iteración por carriles.** Pregunta, sugerencia, petición, exploración, pausa… El canvas solo se reedita ante petición o sugerencia aprobada, siempre con un mini-diff de cambios.
5. **Cierre y derivados.** El autor copia el resultado a su vault de Obsidian. Bajo petición: newsletter de LinkedIn, post de feed y prompt de imagen (ratio 1570:880).

## Qué no hace, por diseño

- No escribe **nunca** en el vault ni en disco: todo vive en la conversación.
- No genera las etiquetas finales ni el bloque YAML de coautoría (los produce el autor con sus propias herramientas).
- No genera imágenes (solo prompts descriptivos) y no publica nada.
- No inventa la existencia ni la URL de artículos previos: si no puede verificarlos, pregunta.
- No precipita hacia la redacción cuando la conversación apenas empieza.

## Instalación

**Como plugin, desde este marketplace (recomendado).** En la app de Claude: **Ajustes → Plugins → Añadir** (añadir marketplace) → escribe `novanoticia/mindandhealth-publish-v2` → **Sincronizar**, e instala el plugin `mindandhealth-publish-v2` desde la lista. Con **"Sincronizar automáticamente"** activado, cada cambio publicado en este repositorio se propaga solo a tu Claude.

**Desde la línea de comandos de Claude Code:**

```
/plugin marketplace add novanoticia/mindandhealth-publish-v2
/plugin install mindandhealth-publish-v2@mindandhealth-publish-v2
```

**Como skill suelto en claude.ai, Mistral o Perplexity (alternativa sin plugins).** Estos clientes no leen marketplaces, pero sí la [Agent Skills Specification](https://agentskills.io/specification) abierta que ya usa este skill. Descarga el zip listo desde **[`/dist/mindandhealth-publish-v2.zip`](dist/mindandhealth-publish-v2.zip)** (o `.skill` para claude.ai) — mismo contenido, sin tener que recortar nada del repo a mano.

- **claude.ai:** Ajustes → Capacidades → Skills → Subir skill → `mindandhealth-publish-v2.skill`.
- **Perplexity:** en un Space, *Add Sources* → sube todos los archivos del zip descomprimido; o en Computer, *Skills → + Create skill*.
- **Mistral / Vibe Work:** el zip se instala tal cual; solo hay que acortar la `description` a menos de 500 caracteres en el propio formulario de instalación (la spec permite hasta 1024; el resto de clientes usa la versión larga). El texto ya recortado está en [`/dist/README.md`](dist/README.md), listo para copiar y pegar.

Con cualquiera de estas vías pierdes la sincronización automática del marketplace; el resto del skill funciona igual.

## Uso

```
/mindandhealth-publish-v2:mindandhealth-publish-v2 [contexto opcional]
```

O en lenguaje natural, que funciona igual con cualquier método de instalación: «pensemos sobre X», «me ronda esta idea», «saca canvas con lo que llevamos», «haz la newsletter del último artículo», «dame el prompt de imagen para este post».

## Estructura

```
mindandhealth-publish-v2/                 ← repositorio = marketplace de plugins
├── .claude-plugin/
│   └── marketplace.json                  ← manifiesto del marketplace (lo que Claude lee al añadirlo)
├── plugins/
│   └── mindandhealth-publish-v2/         ← el plugin
│       ├── .claude-plugin/
│       │   └── plugin.json               ← manifiesto del plugin
│       └── skills/
│           └── mindandhealth-publish-v2/ ← el skill
│               ├── SKILL.md              ← orquestador: modelo mental, gates, flujo
│               ├── CHANGELOG.md          ← trazabilidad completa de la v2
│               ├── modes/                ← conversar · generate · refine · transform · pipeline
│               ├── references/           ← protocolo de canvas (fuente canónica), voz editorial,
│               │                            YAML, pie ético, mapa temático, orquestación de modelos
│               └── derivatives/          ← newsletter LinkedIn · post de feed · banner 1570:880
├── dist/                                  ← skill suelto para clientes sin plugins
│   ├── README.md                         ← instrucciones por cliente (Mistral/Perplexity/claude.ai)
│   ├── mindandhealth-publish-v2.zip      ← Perplexity y estándar de la spec
│   └── mindandhealth-publish-v2.skill    ← claude.ai
├── README.md
└── LICENSE
```

## Entornos y portabilidad

El skill declara un **gate de entorno** explícito: con acceso de lectura al sistema de archivos (Claude Code, Desktop, Cowork) puede verificar artículos del vault; sin él (claude.ai, otros asistentes), pide el material al autor en lugar de suponerlo. En entornos con mecanismo de subagentes admite **delegación opcional** de tramos pesados a un modelo frontera, con contrato heredado y *fallback* al modelo de la sesión — nunca simula una delegación que no ocurrió. La `description` del frontmatter se mantiene bajo 1024 bytes UTF-8 para conservar la portabilidad a otros ecosistemas de skills.

## Novedades de la v2

Versión auditada (protocolo de auditoría estructurada con calibración de confianza) y mejorada respecto al skill original:

- Ratio de imagen unificado en **1570:880** con fuente canónica declarada.
- Ruta personal del vault eliminada; sustituida por el gate de entorno.
- Pie ético con **variación controlada**: cuatro invariantes fijos, redacción fresca en cada artículo.
- Nota de vigencia en el mapa temático (anti-alucinación de enlaces internos).
- Nueva referencia de orquestación de modelos.
- Distribución como **marketplace de plugins** con sincronización automática desde GitHub.
- Empaquetado suelto en `/dist/` para clientes sin plugins que sí siguen la Agent Skills Spec (**Mistral**, **Perplexity**), sin reescritura del skill.

Detalle completo, con identificadores de hallazgo y fix, en [CHANGELOG.md](plugins/mindandhealth-publish-v2/skills/mindandhealth-publish-v2/CHANGELOG.md).

## Contexto del proyecto

Este skill sirve al proyecto editorial de **Pablo Rodríguez López** en [mindandhealth.org](https://mindandhealth.org), que trabaja con criterios públicos de coautoría humano-IA. Referencia: el [manifiesto editorial ético](https://mindandhealth.org/website/ethical-editorial-manifesto) del sitio.

## Licencia

[Apache-2.0](LICENSE). El skill es de propósito personal pero su estructura (gate de entorno, variación controlada del pie ético, orquestación opcional, distribución como marketplace) es reutilizable como patrón para otros skills editoriales.

---

*Este README y el skill que documenta han sido elaborados con asistencia de IA bajo supervisión humana. Requieren revisión humana antes de basar decisiones en ellos.*
