from decouple import config as config_decouple
from config import config
from flask import Flask
from flask_restful import Api
from Apis.PasswordGenerator.passGenerator_API import passwordGeneratorAPI
from Apis.defaultPage import DefaultPage

app = Flask(__name__)
api = Api(app)

environment = config['development']
if config_decouple('PRODUCTION', default=False):
    environment = config['production']

app.config['TESTING'] = False
app.config.from_object(environment)

###############	Routes
api.add_resource(
	DefaultPage,
	'/'
)

api.add_resource(
	passwordGeneratorAPI,
	'/passGen/<int:passlength>/<int:capitalLetter>/<int:lowCaseLetter>/<int:puntuation>/<int:specialCharacters>/'
)

api.add_resource()
###############

if __name__ == '__main__':
    app.run(debug=True)

