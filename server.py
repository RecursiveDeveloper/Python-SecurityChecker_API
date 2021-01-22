from flask import Flask
from flask_restful import Resource, Api, reqparse
from Apis import passGenerator

app = Flask(__name__)
api = Api(app)

#todos = {}

class passwordGeneratorAPI(Resource):
	def get(self, passlength, capitalLetter, lowCaseLetter, puntuation, specialCharacters):
		
		parser = reqparse.RequestParser()

		parser.add_argument('passlength', type=int, help='Password Length')
		parser.add_argument('capitalLetter', type=int, help='Option to allow or deny capital letters')
		parser.add_argument('lowCaseLetter', type=int, help='Option to allow or deny low case letters')
		parser.add_argument('puntuation', type=int, help='Option to allow or deny puntuation')
		parser.add_argument('specialCharacters', type=int, help='Option to allow or deny special characters')
		args = parser.parse_args()

		try:
			passwordClass = passGenerator.passgen(passlength, capitalLetter, lowCaseLetter, puntuation, specialCharacters)
			try:
				passString = passwordClass.generatePass()
				return {'GeneratedPassword' : passString}
			except Exception as e:
				raise Exception
		except Exception as e:
			print('An error has occurred, please verify your params data type or conexion.\nError info: ',e)
			return {'GeneratedPassword' : 'Error'}

api.add_resource(
	passwordGeneratorAPI,
	'/passGen/<int:passlength>/<int:capitalLetter>/<int:lowCaseLetter>/<int:puntuation>/<int:specialCharacters>/'
)

if __name__ == '__main__':
    app.run(debug=True)

