import string
import random

class passgen:
	def __init__(self, passlength, capitalLetter, lowCaseLetter, puntuation, specialCharacters):
		self.__passlength = passlength # Private __  # Protected _
		self.__capitalLetter = capitalLetter
		self.__lowCaseLetter = lowCaseLetter
		self.__puntuation = puntuation
		self.__specialCharacters = specialCharacters

	def get_passlength(self):
		return self.__passlength

	def get_capitalLetter(self):
		return self.__capitalLetter

	def get_lowCaseLetter(self):
		return self.__lowCaseLetter

	def get_puntuation(self):
		return self.__puntuation

	def get_specialCharacters(self):
		return self.__specialCharacters

	def get_asciiList(self):
		delete = ['\t','\x0c','\x0b','\n','\r']
		asciis = [x for x in string.printable if delete.__contains__(x) == False]
		return asciis

	def cleanCapitalLetters(self, lista):
		capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		cleanList = [x for x in lista if capitalLetters.__contains__(x) == False]
		return cleanList

	def cleanLowerCaseLetters(self, lista):
		lowerCaseLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		cleanList = [x for x in lista if lowerCaseLetters.__contains__(x) == False]
		return cleanList

	def cleanPuntuation(self, lista):
		puntuations = ['!', '"' , "'" ,',' , '-' , '.' , ':', ';' , '?' , '^' , '_' , '`' , '~']
		cleanList = [x for x in lista if puntuations.__contains__(x) == False]
		return cleanList

	def cleanSpecialCharacters(self,lista):
		specialCharacters = ['#', '$', '%', '&', '(', ')', '*', '+', '/', '<', '=', '>', '@', '[', 
		'\\', ']', '{', '|', '}','!', '"' , "'" ,',' , '-' , '.' , ':', ';' , '?' , '^' , '_' , '`' , '~']
		cleanList = [x for x in lista if specialCharacters.__contains__(x) == False]
		return cleanList

	def joinListValues(self,lista):
		join = ''
		for x in lista:
			join += str(x)
		return join

	def generatePass(self):
		password = list()
		asciis = passgen.get_asciiList(self)
		
		if passgen.get_capitalLetter(self) == False:
			asciis = passgen.cleanCapitalLetters(self,asciis)
		if passgen.get_lowCaseLetter(self) == False:
			asciis = passgen.cleanLowerCaseLetters(self,asciis)
		if passgen.get_puntuation(self) == False:
			asciis = passgen.cleanPuntuation(self,asciis)
		if passgen.get_specialCharacters(self) == False:
			asciis = passgen.cleanSpecialCharacters(self,asciis)
		#print('\n')
		#print('Tamaño de la lista Ascii: ', len(asciis))
		#print(asciis)
		#print('\n')
		while len(asciis) <= passgen.get_passlength(self):
			asciis.extend(asciis)
		for word in range(passgen.get_passlength(self)):
			randomNumb = random.randint(0,len(asciis)-1)
			#print(str(randomNumb))
			#print(str(randomNumb) +' ----> ' + str(asciis[randomNumb]))
			password.append(asciis[randomNumb])
		#print(passgen.get_asciiList(self))
		#print('\n')
		#print(password)
		return passgen.joinListValues(self,password)

def main():
	try:
		passSize = int(input('Longitud de la contraseña (número de caracteres): '))
		if passSize > 30:
			raise Exception
		print('\n')
		print('Si su respuesta es sí, digite -> 1, de lo contrario digite -> 0 .\nCualquier otro caracter será tomado como -> 0 o se notificará como error')
		print('\n')

		respuestas = list()
		try:
			capitalLetter = int(input('Incluir letras en mayúscula: '))
			if capitalLetter == 1:
				respuestas.append(True)
			elif capitalLetter == 0 or capitalLetter != 0:
				respuestas.append(False)
		except ValueError as e:
			respuestas.append(False)
		
		try:
			lowCaseLetter = int(input('Incluir letras en minúscula: '))
			if lowCaseLetter == 1:
				respuestas.append(True)
			elif lowCaseLetter == 0 or lowCaseLetter != 0:
				respuestas.append(False)
		except Exception as e:
			respuestas.append(False)
		
		try:
			puntuation = int(input('Incluir signos de puntuación: '))
			if puntuation == 1:
				respuestas.append(True)
			elif puntuation == 0 or puntuation != 0:
				respuestas.append(False)
		except Exception as e:
			respuestas.append(False)

		try:
			specialCharacters = int(input('Incluir caracteres especiales: '))
			if specialCharacters == 1:
				respuestas.append(True)
			elif specialCharacters == 0 or specialCharacters != 0:
				respuestas.append(False)
		except Exception as e:
			respuestas.append(False)
		
		print(respuestas)
		password = passgen(passSize,respuestas[0],respuestas[1],respuestas[2],respuestas[3])
		print('\n')
		print(password.generatePass())
	except Exception as e:
		print('El programa ha finalizado debido a un error, certifique los datos ingresados.\nError info: '+str(e))

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print('El programa ha finalizado debido a un error, certifique los datos ingresados.\nError info: '+str(e))
