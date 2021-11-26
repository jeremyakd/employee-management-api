from flask import Flask, jsonify, request

app = Flask(__name__)

# ROUTES 

######################################################## ALTA ########################################################
@app.route('/employee', methods=['POST'])
def createEmployee():
    print(request.json)
    return jsonify({ "mesage": "Employee Created!" })


######################################################## BAJA ########################################################
@app.route('/employee/<id>', methods=['DELETE'])
def deleteEmployee(id):
    return jsonify({ 'message': ("Employee Deleted "+ id )})


#################################################### MODIFICACION ####################################################
@app.route('/employee/<id>', methods=['PUT'])
def updateEmployee(id):
    print(request.json)
    return jsonify({ 'message': 'Employee {} Updated!'.format(id) })


#################################################### CONSULTA POR ID #################################################
@app.route('/employee/<id>', methods=['GET'])
def getEmployee(id):
    print(id)
    return jsonify({ "mesage": "Employee {}.".format(id) })


#################################################### FILTRO POR EDAD #################################################
@app.route('/filter_by_age/<edad>', methods=['GET'])
def employees_by_age(edad):
    return jsonify({ "mesage": "All Employees with age {}.".format(edad) })


################################################ FILTRO POR ANTIGUEDAD ###############################################
@app.route('/filter_by_antiquity/<antiguedad>', methods=['GET'])
def employees_by_antiquity(antiguedad):
    return jsonify({ "mesage": "All Employees with antiquity {}.".format(antiguedad)})



if __name__ == "__main__":
    app.run(debug=True)
