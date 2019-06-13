# Darth_Searcher
Aplicación Web basada en swapi (https://swapi.co)

Instrucciones de instalación

Descargamos Git (en el caso de algunas distribuciones Linux, ya lo tendremos instalado):
https://git-scm.com/

Clonamos el proyecto en la ruta deseada con el comando:
git clone https://github.com/AlvaroOrellana/Darth_Searcher.git

Descargamos e instalamos Python y Pip (en el caso de algunas distribuciones Linux, ya lo tendremos instalado):
https://www.python.org/
https://www.w3schools.com/python/python_pip.asp (Tutorial de W3Schools acerca de Python-Pip)

Instalamos las dependencias necesarias utilizando el fichero requirements.txt presente, normalmente estará en la ruta 
Darth_Searcher/Darth_Searcher/requirements.txt mediante pip.
(pip install -r requirements.txt)

Lanzaremos el servidor indicando la ruta del fichero manage.py (normalmente Darth_Searcher/manage.py) mediante el comando:
python manage.py runserver

Abrimos en el navegador la dirección http://127.0.0.1:8000 y ya podremos usar la aplicación.

NOTA: todas las consultas son realizadas a swapi.co, ésto quiere decir que para el buen funcionamiento de la aplicación es necesario que el dominio swapi.co se encuentre activo.

NOTA 2: durante la realización de esta aplicación tuve severos problemas dada la inestabilidad durante algunos días del dominio, de ahí estas notas.

Créditos para IMDB, swapi.co y autores de las imágenes utilizadas sin ánimo de lucro.
