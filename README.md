# employee-management-api

## Api crud built in Flask


## *Getting started!*

### Clonar el repo

    git clone git@github.com:jeremyakd/employee-management-api.git

    cd employee-management-api

### Instalar dependencias 
<small>Se entiende que se cuenta con virtualenv ya instalado. De lo contrario visitar => https://j2logo.com/virtualenv-pip-librerias-python/</small>

    virtualenv env --python=python3
    source env/bin/activate
    pip insttall -r requirements.txt

### Run

    flask run

### Test

    nosetests --verbose

### Documentacio Swagger
:link: http://localhost:5000/swagger/ :link:

<hr>
<br>

### Comando para obtener graficos.

- <small>En terminal python</small>:

        python scripts/graphics.py

- <small>Ejecutado con docker-compose</small>:

        docker-compose exec employee-management-api python /app/scripts/graphics.py


