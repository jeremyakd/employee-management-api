import mongoengine
import pandas as pd
import matplotlib.pyplot as plt
import plotext
import pymongo
import termplotlib as tpl
import os

collection = False

MONGO_URL = os.environ.get("MONGO_URL", 'localhost')
MONGO_PORT = os.environ.get("MONGO_PORT", '27017')
MONGO_DB = os.environ.get("MONGO_DB", 'employee')

def conect_mongo():
    """
    Connect to DB and return the db and collections object.
    """
    client = mongoengine.connect(host='mongodb://' + MONGO_URL + ':' +  MONGO_PORT + '/' + MONGO_DB)
    db = client.employee
    collection = db.employee
    data = pd.DataFrame(list(collection.find()))
    return data, collection


def extract_data(data, column):
    """
    Extrae de la DB las colunmas enviadas por parametro y
    devuelve una lista de el año actual menos la fecha de la columna.
    """
    col_list = data[column].tolist()
    return [ ( 2021 - d.to_pydatetime().year ) for d in col_list ]

def get_quantity(ages):
    """
    Esta funcion recibe una lista de edades y las fitra
    por rango etario.
    """
    q = [0,0,0,0,0]
    for a in ages:
        if a < 29:
            q[0]+=1
        elif a < 39:
            q[1]+=1
        elif a < 49:
            q[2]+=1
        elif a < 59:
            q[3]+=1
        else:
            q[4]+=1
    return q

def get_employees_dates_and_antiquty(collections):
    """
    Recibe una coleccion y devuelve una lista con 2 elementos.
    - Una lista con las edades.
    - Una lista con la antigüedad.
    La lista devuelta está ordenada por edad de forma ascendente.
    """
    np_array = [[],[]]
    for c in collections.find().sort('fecha_nacimiento',pymongo.DESCENDING):
        np_array[0].append(2021 - c['fecha_ingreso'].year)
        np_array[1].append(2021 - c['fecha_nacimiento'].year)
    return np_array


def print_graphic_age_bar(ages):
    """
    Recibe una lista de datetimes, Las filtra
    y luego imprime en consola un grafico de barras relacionando
    edad y entigüedad.
    """
    plotext.bar(['20-29', '30-39', '40-49', '50-59', '60-69'], get_quantity(ages))
    plotext.title("Personas por rango etario")
    plotext.show()

def get_graphic_age(ages):
    """
    Recibe una lista de datetimes, Las filtra
    y luego muestra un grafico de barras relacionando
    edad y entigüedad.
    """
    fig, ax = plt.subplots()
    ax.bar(['20-29', '30-39', '40-49', '50-59', '60-69'], get_quantity(ages))
    plt.title("Personas por rango etario")
    plt.show()



def print_graphic_age(entrys):
    """
    Recibe una lista de ordenadas de 2 listas de valores.
    Luego imprime en consola un grafico relacionando edad
    y antiguedad en la empresa.
    """
    fig = tpl.figure()
    fig.plot(entrys[1], entrys[0], width=150, height=20)
    fig.show()

def get_graphic_antiquity(entrys):
    """
    Recibe una lista de ordenadas de 2 listas de valores
    para dibujar un grafico en consola.
    """
    fig, ax = plt.subplots()
    ax.plot(entrys[1], entrys[0])
    plt.show()

mongo_data, collection = conect_mongo()
ages_and_antiquities = get_employees_dates_and_antiquty(collection)

edades = extract_data( mongo_data, 'fecha_nacimiento', )
ingresos = extract_data( mongo_data, 'fecha_ingreso' )


# Gráfico que permita visualizar a los empleados por rango etario
print_graphic_age_bar(edades)
# -------------------------------------------------------------------------
# Gráfico que relacione edad con antigüedad en la empresa 
print_graphic_age(ages_and_antiquities)
# -------------------------------------------------------------------------

get_graphic_age( edades )
get_graphic_antiquity(ages_and_antiquities)


