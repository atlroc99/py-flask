from flask import Flask, request, jsonify
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os
import json

# init app
app = Flask(__name__)


# absPath = os.path.abspath()
# print(f"absPath : {absPath}")

@app.route('/')
@app.route('/home')
def home():
    return "hello home page.."


@app.route('/employees', methods=['GET'])
def get_employees():
    mohammad = {"first_name": "mohammad", "last_name": "Zaman",
                "profession": "developer", "religion": "Islam"}
    jon = {"first_name": "Jon", "last_name": "Doe",
           "profession": "developer II", "religion": "Christain"}
    tri = {"first_name": "Tri", "last_name": "Astuti",
           "profession": "Devops Engineer", "religion": "Islam"}
    employees = [mohammad, jon, tri]
    return Response(json.dumps(employees), mimetype='application/json')


@app.route('/os-module', methods=['GET'])
def getOSModule():
    availableFunction = dir(os)
    functionDictionary = {"availableFunction": availableFunction}
    return functionDictionary


@app.route('/useful-functions')
def useful_functions():
    useful_functions = {}
    getcwd = os.getcwd()

    environ = os.environ
    home = environ.get('HOME')
    SDKMAN_VERSION = environ['SDKMAN_VERSION']

    useful_functions["curDir"] = f"{getcwd} : print current working directory we are in now"
    useful_functions['os.environ.get(home)'] = f"{home} : get one of many environtment variables of the operatign system"
    useful_functions['SDKMAN_VERSION'] = SDKMAN_VERSION

    # useful_functions['environ'] = environ

    return useful_functions


@app.route('/envrionment-vars', methods=['GET'])
def get_envrionment_variables():
    environ_vars = {}
    keys = os.environ.keys()
    print(f"keys: {keys}")
    for key in keys:
        val = os.environ.get(key)
        environ_vars[key] = val
    return environ_vars


# run server
if __name__ == '__main__':
    app.run(debug=True)
