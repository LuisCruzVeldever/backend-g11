# Entornos virtuales python

## Crear un entorno virtual

..
python -m venv venv
..

## Activar el enytorno virtual

...

venv\Scripts\activate   (cmd)
source venv/Scripts/activate  (git)
source venv/bin/activate      (mac)

## Descativar el entorno virtual

...
desactivate 
...

# Flask
##  Instalar Flask

...
pip install Flask
...

## Verificamos que flask se haya instalado

... 
pip freeze
...

## Listar las librerias en el archivo 
'requirements.txt'

...
pip freeze > requirements.txt
...