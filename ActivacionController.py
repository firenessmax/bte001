import re, time
from PyQt4 import QtCore
from activacion.activate import *
def enviarDatos(mail, pas):
	print mail, pas
def verificarMail(mail):
	return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mail)
def verificarPassword(passw):
	return len(passw) > 0
def iniciar(s, mail, passw):
	s.activador = Activar()
	s.activador.setup(mail, passw)
	s.connect(s.activador, s.activador.signal, s.activado)
	s.connect(s.activador, s.activador.signalMensaje, s.estado)
	s.connect(s.activador, s.activador.signalError, s.rechazado)
	s.activador.start()
def valido():
	try:
		if Activacion.activador.verificar():
			return True
		else:
			# Warning?
			return False
	except Exception as e:
		print e
		return False
class Activar(QtCore.QThread):
	def setup(self):
		self.signal = QtCore.SIGNAL("signal")
		self.signalMensaje = QtCore.SIGNAL("signalMensaje")
		self.signalError = QtCore.SIGNAL("signalError")
	def run(self):
		try:
			Activacion.activador.validar(user,password)
		except Exception as e:
			self.emit(self.signalError)
			print e
		
		for i in range(5):
			time.sleep(1.0)
			self.emit(self.signalMensaje, "Intento: %d"%i)
		self.emit(self.signal)