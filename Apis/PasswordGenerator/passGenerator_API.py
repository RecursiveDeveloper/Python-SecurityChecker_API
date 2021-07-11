from flask_restful import Resource, reqparse
from Apis.PasswordGenerator import passGenerator

class passwordGeneratorAPI(Resource):
	def get(self, passlength, capitalLetter, lowCaseLetter, specialCharacters):
		
		parser = reqparse.RequestParser()

		parser.add_argument('passlength', type=int, help='Password Length')
		parser.add_argument('capitalLetter', type=int, help='Option to allow or deny capital letters')
		parser.add_argument('lowCaseLetter', type=int, help='Option to allow or deny low case letters')
		parser.add_argument('specialCharacters', type=int, help='Option to allow or deny special characters')
		args = parser.parse_args()

		verify = [0,1]
		try:
			if verify.__contains__(capitalLetter) and verify.__contains__(lowCaseLetter) and verify.__contains__(specialCharacters):
				passwordClass = passGenerator.passgen(passlength, capitalLetter, lowCaseLetter, specialCharacters)
				try:
					passString = passwordClass.generatePass()
					return {'GeneratedPassword' : passString}
				except Exception as e:
					print('An error has occurred during the password generating process, please verify your params data type or conexion.\nError info: {}'.format(e))
			else:
				raise Exception('An error has occurred, please verify your params data type, they must be int type, 0 or 1 . Otherwise, an error is raised')
		except Exception as e:
			print('An error has occurred, please verify your params data type or conexion.\nError info: {}'.format(e))
			return {'GeneratedPassword' : 'Error'}