import re, time
from PyQt4 import QtCore
import activacion.activate as Activacion

def enviarDatos(mail, pas):
	print mail, pas
def verificarUser(user):
	#return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", user)
	return len(user) > 0
def verificarPassword(passw):
	return len(passw) > 0
def iniciar(s, user, passw):
	s.activador = Activar()
	s.activador.setup(user, passw)
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
	def setup(self, user, password):
		self.user = user
		self.password = password
		self.signal = QtCore.SIGNAL("signal")
		self.signalMensaje = QtCore.SIGNAL("signalMensaje")
		self.signalError = QtCore.SIGNAL("signalError")
	def run(self):
		try:
			Activacion.activador.validar(self.user,self.password)
			time.sleep(1.0)
			self.emit(self.signalMensaje, "Activado")
			self.emit(self.signal)
		except Exception as e:
			self.emit(self.signalError)
			print e