from flask import Flask, request, jsonify
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os
import json

# init app
app = Flask(__name__)

# Request Query String


@app.route('/test-client')
def method_name():
    return "success...200 OK"


@app.route('/query-example', methods=['GET'])
def query_example():
    language = request.args.get('language')
    framework = request.args.get('framework')
    website = request.args.get('website')

    return """
        <h1>language: {}</h1>
        <h1>framework: {} </h1>
        <h1>website: {} </h1>
    """.format(language, framework, website)


@app.route('/form-data-example', methods=['GET', 'POST'])
def process_form_data():
    form = '''
            <form method="POST">
                <p>
                    <lable for="lang">Language</lable>
                    <input id="lang" type="text" name="language">
                </p>
                <p>
                    <label for="fmwk">Framework</label>
                    <input id="fmwk" type="text" name="framework">
                </p>
                <p>
                    <label for="website">Website</label>
                    <input id="website" type="text" name="website">
                </p>
                <input type="submit" value="submit">
            </form>
        '''

    if request.method != 'POST':
        return form

    language = request.form.get('language')
    framework = request.form.get('framework')
    website = request.form.get('website')

    return '''
        Form Submitted and received  
        <h5> language {} </h5>
        <h5> website {} </h5>
        <h5>frameowrk: {} </h5>
    '''.format(language, website, framework)


# {
#     "language" : "Python",
#     "framework" : "Flask",
#     "website" : "Scotch",
#     "version_info" : {
#         "python" : 3.4,
#         "flask" : 0.12
#     },
#     "examples" : ["query", "form", "json"],
#     "boolean_test" : true
# }
@app.route('/json-example', methods=['POST'])
def json_example():
    req_data = request.get_json()

    language = req_data.get('language')
    framework = req_data.get('framework')
    website = req_data.get('website')
    version_info_dict = req_data.get('version_info')
    py_version = version_info_dict['python']
    flask_version = version_info_dict['flask']
    examples = req_data['examples']
    boolean_test = req_data.get('boolean_test')

    data_extracted = '''
        <h4>language: {}</h4>
        <h4>framework: {}</h4>
        <h4>website: {}</h4>
        <h4>python version: {}</h4>
        <h4>flask version: {}</h4>
        <h4>Boolean test: {}</h4>
        <h4>Examples: {}</h4>
    '''.format(language, framework, website, py_version, flask_version, boolean_test,examples)

    return data_extracted


@app.route('/json-boolean-example', methods=['POST'])
def test_json_boolean():
    json = request.get_json()
    boolean_test = json.get('boolean_test')
    print("Found booelan test: {}".format(boolean_test))

    return '''boolean_test: {}'''.format(boolean_test)


@app.route('/json-list-test', methods=['POST'])
def test_json_list():
    json = request.get_json()
    print("json data: {}".format(json) )
    examples = json['examples']
    print("examples list: {}".format(examples))

    return "example: {}".format(examples)


# run server
if __name__ == '__main__':
    app.run(debug=True)
