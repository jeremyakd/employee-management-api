"""
The tests to run in this project.
To run the tests type,
$ nosetests --verbose
"""

from nose.tools import assert_true
import requests, os

BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')

class NewUUID():
    """
    The new uuid created when creating a new employee.
    The NewUUID is used for further tests.
    """
    def __init__(self, value):
        self.value = value


def test_get_individual_request_404():
    "Test getting a non existent request"
    response = requests.get('%s/employee/an_incorrect_id' % (BASE_URL))
    assert_true(response.status_code == 404)


def test_add_new_employee():
    "Test adding a new employee"
    payload = {
        'nombre': 'Joe',
        'apellido': 'Doe',
        'dni': '11223344',
        'fecha_nacimiento': '13-09-1984',
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee' % (BASE_URL), json=payload)
    NewUUID.value = str(response.json()['id'])
    assert_true(response.status_code == 201)


def test_get_new_employee():
    "Test getting the new employee"
    url = '%s/employee/%s' % (BASE_URL, NewUUID.value)
    response = requests.get(url)
    assert_true(response.ok)


def test_edit_new_employee_nombre():
    "Test editing the new employee name"
    payload = {
        'nombre': 'Juan',
        'apellido': 'Doe',
        'dni': '11223344',
        'fecha_nacimiento': '13-09-1984',
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee/%s' %
                            (BASE_URL, NewUUID.value), json=payload)
    assert_true(response.json()['nombre'] == "Juan")


def test_edit_new_employee_apellido():
    "Test editing the new employee apellido"
    payload = {
        'nombre': 'Joe',
        'apellido': 'Perez',
        'dni': '11223344',
        'fecha_nacimiento': '13-09-1984',
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee/%s' %
                            (BASE_URL, NewUUID.value), json=payload)
    assert_true(response.json()['apellido'] == "Perez")


def test_add_new_employee_bad_name_key():
    "Test adding a new employee with a bad name key"
    payload = {
        'bad_key': 'Joe',
        'apellido': 'Doe',
        'dni': '11223344',
        'fecha_nacimiento': '13-09-1984',
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_employee_bad_date_format():
    "Test adding a new employee with a bad date format"
    payload = {
        'nombre': 'Joe' ,
        'apellido': 'Doe',
        'dni': '11223344',
        'fecha_nacimiento': 888888,
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee' % (BASE_URL), json=payload)
    print("response", response)
    assert_true(response.status_code == 400)


def test_add_new_employee_no_name_key():
    "Test adding a new employee without name"
    payload = {
        'apellido': 'Doe',
        'dni': '11223344',
        'fecha_nacimiento': '13-09-1984',
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_employee_no_apellido_key():
    "Test adding a new employee without apellido"
    payload = {
        'nombre': 'Joe',
        'dni': '11223344',
        'fecha_nacimiento': '13-09-1984',
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_employee_unicode_name():
    "Test adding a new employee with a unicode title"
    payload = {
        'nombre': '▚Ⓜ⌇⇲',
        'apellido': 'Doe',
        'dni': '11223344',
        'fecha_nacimiento': '13-09-1984',
        'fecha_ingreso': '20-03-2010'
    }
    response = requests.post('%s/employee' % (BASE_URL), json=payload)
    assert_true(response.ok)


def test_add_new_employee_no_payload():
    "Test adding a new employee with no payload"
    payload = None
    response = requests.post('%s/employee' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)


def test_delete_new_employee():
    "Test deleting the new employee"
    response = requests.delete('%s/employee/%s' % (BASE_URL, NewUUID.value))
    assert_true(response.status_code == 204)


def test_delete_new_employee_404():
    "Test deleting the new employee that was already deleted"
    response = requests.delete('%s/employee/%s' % (BASE_URL, NewUUID.value))
    assert_true(response.status_code == 404)
