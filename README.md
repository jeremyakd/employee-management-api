# employee-management-api

## Api crud built in Flask


## *Getting started!*

### Clonar el repo

    git clone git@github.com:jeremyakd/employee-management-api.git

    cd employee-management-api

# Metodo de deploy by docker-compose
El repo cuenta con un compose con imagenes ya pusheadas a mi dockerhub.
Instalar docker & docker-compose.
- [Instalar docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)
- [Instalar docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-es
)
## Run pulleando las imagenes
    docker-compose -f docker-compose.yml up -d

## Run buildeando las imagenes
    docker-compose -f docker-compose-build.yml up -d --build

# Run artesanal
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

### Modelo de datos de la API

**empleado**
- Id
- Nombre
- Apellido
- DNI
- Fecha_Nacimiento
- Fecha_Ingreso

## Build docker image
    docker build --tag employee-management-api:1.0.0 .

## Run on docker image
    docker run --publish 5000:5000 employee-management-api:1.0.0