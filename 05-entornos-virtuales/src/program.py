# Para crear un entorno virtual
# python3 -m venv env

# Active el entorno virtual:
# source env/bin/activate

# Desactivar un entorno virtual
# deactivate

# Para instalar un paquete
# pip install python-dateutil

# PAra visualizar los paquetes en un entorno virtuales
# pip freeze

# Más formas de instalar un paquete

# Tener un conjunto de archivos en la máquina e instalar desde ese origen:
# cd <to where the package is on your machine>
# python3 -m pip install .

# Instalar desde un repositorio de GitHub que proporciona control de versiones:
# git+https://github.com/your-repo.git

# Instalar desde un archivo comprimido:
# python3 -m pip install package.tar.gz


# Uso de un paquete instalado
# Ahora tiene un paquete instalado. ¿Cómo se usa en el código?

# Asegúrese de que tiene un directorio para los archivos. Se recomienda llamar al directorio src y agregar un archivo de Python de punto de entrada denominado app.py. Ahora agregue código para llamar a pipdate:


# Crear una lista de paquetes que el programa utilizará
# pip freeze > requirements.txt

# Instalar la lista de paquetes por medio de pip
# pip install -r requirements.txt