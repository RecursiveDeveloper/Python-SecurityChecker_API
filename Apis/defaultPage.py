from flask_restful import Resource

class DefaultPage(Resource):
	return {'Welcome to Python Security Checker API': 'Feel free to use this open source API'}