# IA.md — Registro de uso de Inteligencia Artificial

**Proyecto:** EcoEnergy
**Asignatura:** Programación Back End · TI3041
**Evaluación:** Sumativa I
**Estudiante:** Esteban Torres Rivera 
**Fecha:** 30 de Agosto 2026

---

## 1. Herramienta utilizada

- **Herramienta:** Claude
- **Tipo de uso:** Explicación, asistencia de codigo y visor de errores.

---

## 2. Registro de interacciones

> Una ficha por cada tema en que usaste IA. Deja solo las que correspondan a tu proceso real.

### Interacción 
Bloques de plantilla

"este es catalogo por ejemplo" + el archivo con {% block title %} / {% block content %}

en esta sección yo tenia combinado escritura en español y en inglés por lo tanto no me mostraba el contenido del bloque del medio del inicio, y ahí me ayudo corriendo ese error en donde habia lenguaje combinado. 
---

### Interacción 

- **Prompt / consulta realizada:**
  "No se encontró la función inversa para 'inicio'…"
"ahora tengo este error… No se encontró la función inversa para 'detalle_zona'…"

aquí le preguntaba porque no me generaba la conexión con las urls ya que me daba esos errores al momento de cargar la pagina, ya luego en la conversación y revisando el codigo es porque el namespace fue declarado como dispositivo:inicio y yo solo estaba dandole la sentencia de "inicio", asi que tuve que cambiar todo donde tuviese %urls....% con dispositivo:inicio. 

---

### Interacción 

- **Prompt / consulta realizada:**
 TemplateDoesNotExist
"si corre la pagina pero estoy en el problema pasado que aun no puedo solucionar" + traceback
"Esa es la carpeta del proyecto pero au, ve la estructura si existe un archivo llamado inicio.html"
"ya lo correji ahora me arroja lo siguiente" + análisis post mortem del cargador
"en vscode no puedo colocar guion bajo por lo tanto a zonas_listado le he puesto zonas-listado…
--- en esta sección tenia el problema de la forma en que le daba nombre a los documentos, ya que en mi vscode no me muestra cuando coloco el guión bajo, pero descubri que me genera el espacio, le doy enter y si aparece, así que debi renombrar los archivos en los cuales nombre con guión medio. 

---

### Interacción  

- **Prompt / consulta realizada:**
Ubicación de templates y estructura de carpetas

"los json deben crearse en la carpeta dispositivos?"
"pero tengo 2 carpetas dispositivos, una general y una dentro de templates, en cual irian y porque?"
"pero la solución más adecuada es la que me das o deberia estar dentro de dispositivos?"
"vamos con la opción A entonces"

--- En esta sección estaba confundido respecto de como se organizaba la carpeta templates y como quedaba la estructura por lo tanto solicitaba ayuda para ir ordenando y así no me siguiera dando errores en el front. 

---

### Interacción

python decouple 

esto me lo sugirio por la sección de : "Usar un paquete externo pertinente y justificarlo en requirements.txt y Instalar un paquete externo y justificarlo. Algo simple y útil. Instálalo, agrégalo a requirements.txt, y explica en ANALISIS.md o README por qué lo usaste.

use eso para separar las SECRET_KEY, tenerlas en .env que no se suben al proyecto. 




## 3. Partes desarrolladas sin asistencia de IA

todo lo que hicimos en clases y con ayuda de las guías. 

---

## 4. Declaración

La ia me ayudo a comprender en que fase me podía equivocar, reviso que las carpetas estuviesen bien estructuradas, pero aún así cometi errores que me ayudo a resolver, no de inmediato, si no que tuve que ir entendiendo de que forma estaba fallando y aprender a leer los errores. 

