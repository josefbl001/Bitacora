# Bitácora
##Bitácora de Trabajo basada en markdown.

Este script en pyhton permite visualizar un conjunto de archivos
creados en markdown, con el fin navegar notas, comentarios o anotaciones. 

Existen alternativas para llevar una bitacora con problemas inherentes a cada
uno de ellos:

### TextoPlano

* Sin formato.
* No son fáciles de navegar
* Buscar algo depende de que el sistema tenga un buen sistema de búsqueda
  o en su defecto herramientas como **awk**, **grep** ó **sed**.

### Wiki

* Implementación difícil, necesitan un servidor web.
* Mantenimiento complicado.
* Respaldo externo

### Programas Comerciales

* Generalmente de pago.
* Código cerrado
* En algunos casos los archivos son un formato cerrado, solo se pueden abrir 
  con el programa.

### La Nube

* Necesitan conexión a Internet.
* Muchos son de pago.
* La información esta fuera de nuestro equipo.

### Bitácora

En lo personal evito la interfaz gráfica. Ya que el texto plano me permite
tener a mano cualquier archivo en el momento en que reviso mis actividades,
este o no fuera de línea. Solía usar como bitácora
[docuwiki](http://www.docuwiki.org) pero requiere de un servidor como
[nginx](http://nginx.org) y el motor [php](http://es.wikipedia.org/wiki/PHP)
para su uso.  He probado [Evernote](https://evernote.com/intl/es/) y es
poderoso pero...  tambien costoso. Muchos de estos servicios permiten el uso de
[markdown](http://es.wikipedia.org/wiki/Markdown). Este lenguaje permite
escribir y dar formato a el texto sin separar los dedos del teclado. Permite
incluir imagenes, notas, listas, tablas y etiquetas de manera sencilla en texto
plano.

Otro servicio que uso al programar es [Git](https://git-scm.com/), este permite
llevar un control de las versiones<sup>[1](#vers)</sup> de mis archivos y al usarse en conjunto
con un servicio como github, bitbucket o un servidor propio. Es una alternativa
interesante al respaldo las notas.

En un intento por agregar visualización  e indices a este flujo de trabajo, el
script  **Bitácora** hace uso del programa
[GRIP](https://github.com/joeyespo/grip), que permite visualizar archivos
markdown<sup>[2](#mgithub)</sup> . Ademas crea la pagina **index.md**, así como **notas.md**, que
agrupa el número de línea y la primera línea que sigue al tag ``Nota:`` dentro
de cada archivo. Además crea un archivo que enlista los archivos por mes. El
archivo **index.md**, contiene los primeros 5 archivos que se modificarón
recientemente, enlaces a los archivos por mes y enlace al archivo de notas.

## Instalación

De momento el script funciona para systemas Linux con Python 2.7. Requiere del
archivo **grip**. Que se puede instalar usando
[pip](https://pypi.python.org/pypi/pip) en linux mediante:

    pip install -U grip

En el caso de sistemas derivados de Debian se puede usar precedido con un
``sudo``.

Luego el script se ejecuta en la misma carpeta donde se encuentran los archivos
markdown.  Para mejorar el uso, el script puede hacerse ejecutable y colocarse
en un path de execución del sistema o agregarse el path de este script al path
de ejecución.


<a name="vers">1</a>: Este permite tanto un control de cambios como un sistema de respaldos.
<a name="mgithub">2</a>: La versión markdown de [github](https://help.github.com/articles/github-flavored-markdown/)
