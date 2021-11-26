from flask import Flask, jsonify, request
from bson import ObjectId
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/employee'

mongo = PyMongo(app)

db = mongo.db.employee

# ROUTES 

######################################################## ALTA ########################################################
@app.route('/employee', methods=['POST'])
def createEmployee():
    print(request.json)
    id = db.employee.insert({
        'nombre': request.json['nombre'],
        'apellido': request.json['apellido'],
        'dni': request.json['dni'],
        'fecha_nacimiento': request.json['fecha_nacimiento'],
		'fecha_ingreso': request.json['fecha_ingreso'],
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
    return jsonify({ "mesage": "All Employees with age {}.".format(edad) })


################################################ FILTRO POR ANTIGUEDAD ###############################################
@app.route('/filter_by_antiquity/<antiguedad>', methods=['GET'])
def employees_by_antiquity(antiguedad):
    return jsonify({ "mesage": "All Employees with antiquity {}.".format(antiguedad)})


# ----------------------- all employees
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

if __name__ == "__main__":
    app.run(debug=True)
