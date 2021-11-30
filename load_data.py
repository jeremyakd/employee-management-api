from faker import Factory
import mongoengine
import datetime

def create_names(cant):
    client = mongoengine.connect(host='mongodb://localhost:27017/employee')
    db = client.employee
    fake = Factory.create()
    for x in range(int(cant)):
        fake_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_dni = str(fake.pyint(min_value=1000000, max_value=99999999))
        fake_f_nacimiento = fake.date_between_dates(
            datetime.datetime.strptime('1961-01-01', '%Y-%m-%d'),
            datetime.datetime.strptime('2003-01-01', '%Y-%m-%d'),
        )
        fake_f_ingreso = fake.date_between_dates(
            datetime.datetime.strptime('2011-01-01', '%Y-%m-%d')
        )
        try:
            result = db.employee.insert_one(
                {
                'nombre': fake_name,
                'apellido': fake_last_name,
                'dni': fake_dni,
                'fecha_nacimiento': datetime.datetime.combine(fake_f_nacimiento, datetime.datetime.min.time()),
                'fecha_ingreso': datetime.datetime.combine(fake_f_ingreso, datetime.datetime.min.time()),
                }
            )
        except Exception as e:
            print("e", e)
            return False
        #print("Se carga empleado {} => {}".format(x, result))
    #if db.employee.count() == int(cant):
    return "Ser cargaron {} empleados.".format(cant)
    #else:
    #    return False
        # print('id: ' + str(result.inserted_id) + ' name: ' + fake_name)
