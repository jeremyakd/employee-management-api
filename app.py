from flask import Flask, jsonify, request

from bson import ObjectId
from flask_pymongo import PyMongo

from dateutil.relativedelta import relativedelta
import datetime

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://mongo:27017/employee'

mongo = PyMongo(app)

db = mongo.db

# ROUTES 

######################################################## ALTA ########################################################
@app.route('/employee', methods=['POST'])
def createEmployee():
    print(request.json)
    id = db.employee.insert({
        'nombre': request.json['nombre'],
        'apellido': request.json['apellido'],
        'dni': request.json['dni'],
        'fecha_nacimiento': datetime.datetime.strptime(request.json['fecha_nacimiento'], '%d-%m-%Y'),
		'fecha_ingreso': datetime.datetime.strptime(request.json['fecha_ingreso'], '%d-%m-%Y'),
    })
    return jsonify(str(ObjectId(id)))


######################################################## BAJA ########################################################
@app.route('/employee/<id>', methods=['DELETE'])
def deleteEmployee(id):
	db.employee.delete_one({'_id': ObjectId(id)})
	return jsonify({'message': 'Employee Deleted'})

#################################################### MODIFICACION ####################################################
@app.route('/employee/<id>', methods=['POST'])
def updateEmployee(id):
	print(request.json)
	db.employee.update_one({'_id': ObjectId(id)}, {"$set": {
		'nombre': request.json['nombre'],
		'apellido': request.json['apellido'],
		'dni': request.json['dni'],
		'fecha_nacimiento': request.json['fecha_nacimiento'],
		'fecha_ingreso': request.json['fecha_ingreso'],
	}})
	return jsonify({'message': 'Employee Updated'})


#################################################### CONSULTA POR ID #################################################
@app.route('/employee/<id>', methods=['GET'])
def getEmployee(id):
    print("id", id)
    employee = db.employee.find_one({'_id': ObjectId(id)})
    print(employee)
    if employee is not None:
        return jsonify({
            '_id': str(ObjectId(employee['_id'])),
            'nombre': employee['nombre'],
            'apellido': employee['apellido'],
            'dni': employee['dni'],
            'fecha_nacimiento': employee['fecha_nacimiento'],
            'fecha_ingreso': employee['fecha_ingreso'],
            })
    else:
        return jsonify({ "mesage": "No se encontró empleado." })


#################################################### FILTRO POR EDAD #################################################
@app.route('/filter_by_age/<edad>', methods=['GET'])
def employees_by_age(edad):
    now = datetime.datetime.now()
    # con la fecha seteo el dia limite de busqueda y lo guardo en la variable hasta
    hasta = now - relativedelta(years=int(edad))
    # le resto un año y un dia para setear el umbral de fechas de busqueda
    desde = (hasta - relativedelta(years=1) - datetime.timedelta(days=1)) # bajo lte
    employee_filtered = db.employee.find({"fecha_nacimiento": { "$gte": desde, "$lte": hasta }} )
    employees = []
    for doc in employee_filtered:
        employees.append({
            '_id': str(ObjectId(doc['_id'])),
            'nombre': doc['nombre'],
            'apellido': doc['apellido'],
            'dni': doc['dni'],
            'fecha_nacimiento': doc['fecha_nacimiento'],
			'fecha_ingreso': doc['fecha_ingreso'],
        })
    response = {
        'message': 'Se encontraron {} empleados con {} años.'.format(len(employees), edad),
        'response': employees
    }
    return jsonify(response)


################################################ FILTRO POR ANTIGUEDAD ###############################################
@app.route('/filter_by_antiquity/<antiguedad>', methods=['GET'])
def employees_by_antiquity(antiguedad):
    now = datetime.datetime.now()
    hasta = now - relativedelta(years=int(antiguedad))
    desde = (hasta - relativedelta(years=1) - datetime.timedelta(days=1))
    employee_filtered = db.employee.find({"fecha_ingreso": { "$gte": desde, "$lte": hasta }} )
    employees = []
    for doc in employee_filtered:
        employees.append({
            '_id': str(ObjectId(doc['_id'])),
            'nombre': doc['nombre'],
            'apellido': doc['apellido'],
            'dni': doc['dni'],
            'fecha_nacimiento': doc['fecha_nacimiento'],
			'fecha_ingreso': doc['fecha_ingreso'],
        })
    return jsonify(employees)


############################################### TODOS LOS EMPLEADOS ##################################################
@app.route('/employees', methods=['GET'])
def getEmployees():
    employees = []
    for doc in db.employee.find():
        employees.append({
            '_id': str(ObjectId(doc['_id'])),
            'nombre': doc['nombre'],
            'apellido': doc['apellido'],
            'dni': doc['dni'],
            'fecha_nacimiento': doc['fecha_nacimiento'],
			'fecha_ingreso': doc['fecha_ingreso'],
        })
    return jsonify(employees)

############################################ BORRAR TODOS LOS EMPLEADOS #############################################
@app.route('/employees', methods=['DELETE'])
def deleteEmployees():
    db.employee.delete_many({})
    return jsonify({"message": "droped!"})


################################################ CARGAR EMPLEADOS ###################################################
@app.route('/load-data/<cantidad>', methods=['POST'])
def load_data(cantidad):
    print(request.json)
    from load_data import create_names
    _employees = create_names(cantidad)
    print("_employees", _employees)
    return jsonify({ "mesage": _employees })

if __name__ == "__main__":
    app.run(debug=True)
