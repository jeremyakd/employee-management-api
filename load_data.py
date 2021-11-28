from faker import Factory
import mongoengine
import datetime

client = mongoengine.connect(host='mongodb://localhost:27017/employee')

db = client.employee


def create_names(fake):
    for x in range(40):
        fake_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_dni = fake.job()
        fake_f_nacimiento = fake.date_between_dates(
            datetime.datetime.strptime('1961-01-01', '%Y-%m-%d'),
            datetime.datetime.strptime('2003-01-01', '%Y-%m-%d'),
        )
        fake_f_ingreso = fake.date_between_dates(
            datetime.datetime.strptime('2011-01-01', '%Y-%m-%d')
        )
        result = db.employee.insert_one(
            {
            'nombre': fake_name,
            'apellido': fake_last_name,
            'dni': fake_dni,
            'fecha_nacimiento': datetime.datetime.combine(fake_f_nacimiento, datetime.datetime.min.time()),
            'fecha_ingreso': datetime.datetime.combine(fake_f_ingreso, datetime.datetime.min.time()),
            }
        )
        print('id: ' + str(result.inserted_id) + ' name: ' + fake_name)


if __name__ == '__main__':
    fake = Factory.create()
    create_names(fake)
