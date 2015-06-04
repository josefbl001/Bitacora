# Bitacora
##Bitácora de Trabajo basada en markdown.

Este script en pyhton es un intento para visualizar un aglomerado de archivos
markdown, con el fin navegar notas, comentarios o anotaciones. 

Las alternativas para generar una bitacora pueden agruparse en 
**Texto Simple**, **Wiki's**, **Programas Comerciales**  y la **Nube**.

Cada una de estas alternativas, tienen puntos a favor o en contra:

### TextoPlano
Pro:

* Su acceso no requiere programa alguno.
* Son pequeños
* Disponibles offline

Contra:

* Son simples sin existir un formato o un acceso rapido 
* No son faciles de navegar
* Buscar algo depende de que el systema tenga un buen sistema de busqueda
  o en su defecto herramientas como **awk**, **grep** ó **sed**.

### Wiki

Pro:

* Formato bien mantenido.
* Incluyen Imagenes y multimedia
* Indices, busquedas.

Contra:

* Implementación difícil, necesitan un servidor web.
* Mantenimiento complicado.
* Para exportar el documento son necesarios plugins.

### Programas Comerciales

Pro:

* Muchas funcionalidades
* Interfaz cuidada
* Busquedas, indices, multimedia.

Contra:

* Generalmente de pago.
* Codigo cerrado
* En algunos casos los archivos son un formato extraño, cerrado.

### La Nube

Pro:

* Son accesibles en cualquier lugar.
* Busqueda, Indices y multimedia
* La información se respalda

Contra:

* Necesitan conexión a internet.
* Muchos son de pago.
* La información esta fuera de nuestro equipo.

### Bitacora

En lo personal prefiero evitar la interfaz gráfica. Y el texto plano me permite
tener a la mano cualquier archivo en el momento en que reviso mis actividades,
este o no fuera de linea. Antes de este script solía usar
[docuwiki](http://www.docuwiki.org) pero requiere de un servidor
[nginx](http://nginx.org) y el motor [php](http://es.wikipedia.org/wiki/PHP)
para su uso.  He probado [Evernote](https://evernote.com/intl/es/) y es
poderoso pero...  tambien costoso. Muchos de estos servicios usan
[markdown](http://es.wikipedia.org/wiki/Markdown), que permite escribir y dar
formato a el texto sin separar los dedos del teclado. Lo que a largo plazo es
un descanso para la muñeca.

Por lo tanto con el fin de usar archivos de texto plano, el formato markdown e
incluso un sistema de control de versiones[^1] me decline por el uso de
archivos de texto markdown. Con el fin de obtener formato, diponibilidad y
respaldo.

Para ademas agregar visualización  e indices este script hace uso del programa
[GRIP](https://github.com/joeyespo/grip). Que permite visualizar archivos
markdown con la versión markdown de
(github)[https://help.github.com/articles/github-flavored-markdown/].

Una vez descargado se puede ejecutar y genera un servidor para visualizar la
pagina **index.md** que genera el programa así como las paginas **notas.md** y
archivos por mes que agrupan a las notas tomadas durante el mes.  La pagina
**notas.md** contiene las anotaciones que se colocan con la palabra **Nota:** y
la primera línea de las mismas.  El archivo index.md, contiene los primeros 5
archivos que se modificarón recientemente, enlaces a los documentos que
aglomeran los archivos por mes y enlace al archivo de notas.

[^1]: Este permite tanto un control de cambios como un sistema de respaldos.
