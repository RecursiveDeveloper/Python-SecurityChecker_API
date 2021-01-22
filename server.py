from decouple import config as config_decouple
from flask import Flask
from flask_restful import Api
from Apis.PasswordGenerator.passGenerator_API import passwordGeneratorAPI

app = Flask(__name__)
api = Api(app)

app.config['TESTING'] = False
#todos = {}
enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

###############	Routes
api.add_resource(
	passwordGeneratorAPI,
	'/passGen/<int:passlength>/<int:capitalLetter>/<int:lowCaseLetter>/<int:puntuation>/<int:specialCharacters>/'
)
###############

if __name__ == '__main__':
    app.run(debug=True)

