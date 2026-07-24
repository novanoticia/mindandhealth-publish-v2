# mindandhealth-publish-v2

*Conversational editorial companion skill for Claude — Spanish-first. Ideas crystallize through dialogue into an iterative markdown canvas; the skill never writes to the author's vault.*

Skill de **acompañamiento editorial conversacional** para [Claude](https://claude.com) al servicio de las publicaciones de [mindandhealth.org](https://mindandhealth.org) (Obsidian Publish). Su premisa de diseño: **los artículos no se piden, emergen**. El skill no redacta a demanda; conversa, y solo cuando la conversación cristaliza abre un borrador iterable.

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

**En claude.ai (web):** descarga el repo (botón verde **Code → Download ZIP**), y en claude.ai ve a **Ajustes → Capacidades → Skills → Subir skill** y selecciona el ZIP. Se activa con `/mindandhealth-publish-v2` o con lenguaje natural.

**En Claude Code / Claude Desktop:** copia la carpeta del skill al directorio de skills de tu entorno (personal o de proyecto). En esos entornos se habilita además el acceso de **solo lectura** al vault para proponer enlaces internos verificados, y la orquestación opcional de subagentes.

## Uso

```
/mindandhealth-publish-v2 [contexto opcional]
```

O en lenguaje natural: «pensemos sobre X», «me ronda esta idea», «saca canvas con lo que llevamos», «haz la newsletter del último artículo», «dame el prompt de imagen para este post».

## Estructura

```
mindandhealth-publish-v2/
├── SKILL.md                          # Orquestador: modelo mental, gates, flujo
├── CHANGELOG.md                      # Trazabilidad completa de la v2
├── modes/
│   ├── conversar.md                  # Modo por defecto: exploración y cristalización
│   ├── generate.md                   # Primer volcado del canvas
│   ├── refine.md                     # Pulido de borrador aportado
│   ├── transform.md                  # Canvas desde material fuente (papers, URLs, notas)
│   └── pipeline.md                   # Recorrido completo hasta derivados
├── references/
│   ├── modo-iterativo-canvas.md      # Fuente canónica del protocolo de canvas
│   ├── voz-editorial.md              # Tono, ritmo y patrones del sitio
│   ├── estructura-yaml.md            # Frontmatter mínimo Obsidian
│   ├── pie-etico.md                  # Invariantes éticos + variación controlada
│   ├── mapa-tematico.md              # Taxonomía del sitio (snapshot con nota de vigencia)
│   └── orquestacion-modelos.md       # Delegación opcional a subagente frontera
└── derivatives/
    ├── linkedin-newsletter.md        # Artículo → newsletter
    ├── linkedin-feed.md              # Newsletter → post de feed
    └── banner-spec.md                # Prompt de imagen · fuente canónica del ratio 1570:880
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

Detalle completo, con identificadores de hallazgo y fix, en [CHANGELOG.md](CHANGELOG.md).

## Contexto del proyecto

Este skill sirve al proyecto editorial de **Pablo Rodríguez López** en [mindandhealth.org](https://mindandhealth.org), que trabaja con criterios públicos de coautoría humano-IA. Referencia: el [manifiesto editorial ético](https://mindandhealth.org/website/ethical-editorial-manifesto) del sitio.

## Licencia

[Apache-2.0](LICENSE). El skill es de propósito personal pero su estructura (gate de entorno, variación controlada del pie ético, orquestación opcional) es reutilizable como patrón para otros skills editoriales.

---

*Este README y el skill que documenta han sido elaborados con asistencia de IA bajo supervisión humana. Requieren revisión humana antes de basar decisiones en ellos.*
