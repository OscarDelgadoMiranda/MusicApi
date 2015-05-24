# MusicApi
Trabajo del grupo 3 de SD

Componentes del grupo:

**Óscar Delgado Miranda**    
**Miguel Ángel Pérez García**  
**Ildefonso de la Cruz Romero**  
**David Blanco Fuentes**  
  
---

En este proyecto trabajamos con las Apis de Soundcloud, Dropbox y Twitter, así como con los lenguajes python, html, css y javascript.

En este proyecto lo que hacemos es dar una funcionalidad a una página web utilizando la nueva api que hemos creado(MusicApi) para que podamos realizar una búsqueda a través de soundcloud, ya sea de un artista, un álbum o una canción, y que, en la misma página, nos muestre los resultados de las búsquedas, en función de si queremos escucharla, vía streaming, y/o descargarla, así como compartir en Twitter y poder subir a la nube usando dropbox.

Toda la música que nos proporciona la api de Soundcloud respeta los derechos de autor.

---

El programa python principal, la API en si, es el llamado ***MusicApi.py***, al ejecutar este programa te da el enlace de la página web donde se realizan las pruebas.

La forma de realizar las busquedas, que esta más detallado en la documentación, es buscar la canción, decidir que tipo de búsqueda quieres, si solo el streaming para escucharla, o además también descargarla.

Luego aparecerá una lista con las canciones, si has elegido la de descargar y streaming(***Buscar***) puedes bajarte la musica que quieras.

Una vez que te la hayas descargado, si la quieres subir a tu dropbox, primero tienes que elegir la opción de autentificar dropbox,esto te abrirá una pestaña nueva para que le des ha aceptar e inicies sesión en dropbox si no tenenías una sesión abierta.

Luego vuelve a la página y le das a subir a dropbix, esto te creará una carpeta en tu dropbox llamada Music con la músuca que te hayas descargado. Tardará un ratillo dependiendo de lo que te hayas descargado. Te recomiendo que no tengas más canciones en tu carpeta de descargas.

Hay tres ficheros más de python,dos de ellos corresponden a cada API que se ha utilizado(Dropbox y Souncloud) los cuales tienen implementadas funciones que usamos en ***MusicAPi.py***. El tecero es donde guardamos las keys de las APIs utilizadas.

En cualquier momento puedes compartir con twitter la canción que estes escuchando o te hayas descagado con la opción correspondiente.
