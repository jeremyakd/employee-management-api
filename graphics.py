import mongoengine
import pandas as pd
import matplotlib.pyplot as plt
import plotext
import pymongo
import termplotlib as tpl


collection = False

def conect_mongo():
    client = mongoengine.connect(host='mongodb://mongo:27017/employee')
    db = client.employee
    collection = db.employee
    data = pd.DataFrame(list(collection.find()))
    return data, collection

def extract_data(data, column):
    col_list = data[column].tolist()
    ages = [ ( 2021 - d.to_pydatetime().year ) for d in col_list ]
    return ages

def get_quantity(ages):
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

def print_graphic_age(ages):
    plotext.bar(['20-29', '30-39', '40-49', '50-59', '60-69'], get_quantity(ages))
    plotext.title("Personas por rango etario")
    plotext.show()

def get_graphic_age(ages):
    fig, ax = plt.subplots()
    ax.bar(['20-29', '30-39', '40-49', '50-59', '60-69'], get_quantity(ages))
    plt.title("Personas por rango etario")
    plt.show()

def get_columns(entries):
    entries.sort()
    #print("entries", entries)
    _set = set(entries)
    #print("_set", _set)
    _count = len(_set)
    #print("_count", _count)
    pass

def get_graphic_antiquity(entrys):
    fig, ax = plt.subplots()
    ax.plot(entrys[1], entrys[0])
    plt.show()

def print_graphic_age(entrys):
    fig = tpl.figure()
    fig.plot(entrys[1], entrys[0], width=60, height=20)
    fig.show()

    #plt.plot(entrys[1], entrys[0])
    #plt.show()

    #plotext.scatter(entrys[1], entrys[0])
    ##plotext.bar
    #plotext.ylim(0, 10)
    #plotext.xlim(0, 65)
    #plotext.title("Personas por rango etario")
    #plotext.show()

def get_array(collections):
    np_array = [[],[]]
    for c in collections.find().sort('fecha_nacimiento',pymongo.DESCENDING):
        np_array[0].append(2021 - c['fecha_ingreso'].year)
        np_array[1].append(2021 - c['fecha_nacimiento'].year)
    print(np_array)
    return np_array


mongo_data, collection = conect_mongo()



pepe = get_array(collection)

edades = extract_data( mongo_data, 'fecha_nacimiento', )
ingresos = extract_data( mongo_data, 'fecha_ingreso' )

# print("ingresos", ingresos)

#get_columns(ingresos)

#get_graphic_antiquity(pepe)
print_graphic_age(pepe)
#print_graphic_age( edades )
#get_graphic_age( edades )

