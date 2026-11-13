# Política de privacidad de mindandhealth-publish-v2

Última actualización: 13 de noviembre de 2026.

## Alcance

Esta política corresponde al plugin de Claude situado en `plugins/mindandhealth-publish-v2` de este repositorio. Es un conjunto de instrucciones y referencias para acompañamiento editorial: conversación, borradores en el chat y derivados bajo petición.

## Contenido que utiliza

Claude procesa los temas, notas, borradores, fuentes y mensajes que el usuario aporta para el trabajo editorial. Pueden contener datos personales. No es necesario proporcionar información identificativa para utilizar el método; omite o anonimiza los datos que no sean necesarios.

Cuando el entorno tiene acceso de lectura a una carpeta que el usuario ha conectado o indicado, el plugin contempla leer artículos Markdown para verificar referencias o proponer enlaces. En entornos sin ese acceso, solicita al usuario el material. Sus instrucciones prohíben escribir en el vault o crear archivos de trabajo en disco: los borradores permanecen en el chat y el usuario decide qué copiar y publicar.

## Servicios y conservación

El plugin no incorpora servidores MCP, almacenamiento remoto, cuentas ni telemetría propios. El desarrollador no recibe ni conserva las conversaciones o documentos mediante un servicio del plugin.

El procesamiento, historial, conservación y eliminación de los datos en Claude dependen del producto, plan, configuración y condiciones de Anthropic. Esta política no modifica esas condiciones ni implica que Anthropic no conserve datos.

- [Política de privacidad de Anthropic](https://www.anthropic.com/legal/privacy)

Si el usuario aporta una URL o solicita consultar fuentes, Claude puede usar las herramientas de navegación o conectores disponibles en su entorno. Sus proveedores pueden recibir las consultas y datos necesarios para atenderlas, conforme a sus propias políticas. El plugin no incluye conectores propios. La delegación opcional a subagentes, si el entorno la admite, comparte el material asignado con ese mecanismo del entorno, sujeto a sus condiciones.

## Control del usuario

El usuario decide el material que proporciona, las carpetas que conecta y qué contenido copia o publica. El plugin prepara textos y prompts descriptivos, pero no publica artículos o posts ni genera imágenes.

Al no recibir las conversaciones mediante el plugin, el desarrollador no dispone de una copia que pueda consultar o eliminar. Los controles de historial y eliminación deben ejercerse en Claude y, cuando corresponda, en los servicios utilizados.

## Contacto

Para consultas sobre el plugin o esta política utiliza el [repositorio de soporte](https://github.com/novanoticia/mindandhealth-publish-v2/issues). Las incidencias son públicas: no incluyas borradores privados, datos personales sensibles ni credenciales.
