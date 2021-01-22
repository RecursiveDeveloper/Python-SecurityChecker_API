from flask_restful import Resource

class DefaultPage(Resource):
	def get(self):
		return {'Welcome to Python Security Checker API': 'Feel free to use this open source API'}