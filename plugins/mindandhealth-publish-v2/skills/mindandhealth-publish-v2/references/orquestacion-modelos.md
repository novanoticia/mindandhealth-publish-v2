# Orquestación opcional de modelos (subagente frontera)

Compatible con el protocolo `/alternancia-modelos` de Pablo. Leer solo cuando se vaya a delegar de verdad.

## Gate de entorno (paso 0, obligatorio)

Delegar requiere un mecanismo real de subagentes con selección de modelo (p. ej. la herramienta Agent/Task de Claude Code o Cowork con override `model`). Si no existe — claude.ai web/móvil, Perplexity, u otros —, **degradación elegante**: todo corre en el modelo de la sesión y se declara en una línea al cierre del trabajo. **Nunca simular una delegación que no ocurrió.**

## Roles (por rol, no por nombre fijo)

- **Primario** = el modelo de la sesión. Ejecuta todo por defecto: conversación, canvas, iteración.
- **Subagente frontera** (selectivo) = el modelo más capaz disponible en el entorno como configuración de enrutado (a fecha de esta versión: `claude-fable-5`; si no está disponible, el más capaz que el entorno ofrezca). Solo para tramos acotados de alto valor.
- **Fallback = primario.** Bloqueo, redirección por salvaguardas o cuota agotada → el tramo vuelve al primario sin detener el flujo. Una redirección es comportamiento normal, no un error.

## Cuándo delegar (cualquiera de estas; si una pasada basta, no delegar)

- `modes/transform.md` con **muchas fuentes** (varios papers/URLs largos) que exceden una pasada con profundidad.
- **Lote de derivados** (newsletter + feed + prompt de imagen) sobre un artículo largo, en paralelo.
- **Revisión profunda** de un canvas extenso (>2000 palabras) contra la voz editorial completa.

## Contrato del subagente (no negociable)

1. Hereda íntegras las reglas de este skill: **nunca escribir en el vault ni en disco; el canvas vive en el chat; no generar etiquetas finales ni bloque de coautoría; no inventar artículos del vault**.
2. Recibe alcance exacto (qué fuente, qué derivado, qué sección) y el material que posee.
3. Devuelve **material crudo etiquetado** (sección, fuente, confianza si aplica) al orquestador; **no redacta el canvas final** ni habla con Pablo.
4. El orquestador reintegra, verifica contra la voz editorial y compone la versión que ve Pablo.

## Transparencia

Si hubo delegación, cerrar el trabajo con una línea: qué tramo se delegó y por qué (valor / bloqueo / cuota). Ante Pablo, describirlo como "análisis delegado a un proceso de razonamiento auxiliar"; los nombres de modelo solo aparecen como configuración de enrutado, nunca como "el motor" del contenido editorial.
