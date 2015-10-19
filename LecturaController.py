
from PyQt4 import QtCore
from lecturacodigo.devices import lectorDevice
from lecturacodigo.reader import *


def iniciarReader(s, d):
	print d.device['frendly_name'],d.device['name']
	ser = serialReader()
	ser.setup(d,.01)

	s.connect(ser, ser.signal, s.enc)
	print "agregado event listener"
	ser.open()
	print "conexion iniciada"
	return ser

def iniciarDevice(s):
	s.buscador = BuscarLector()
	s.buscador.setup()
	s.connect(s.buscador, s.buscador.signal, s.deviceEncontrado)
	s.buscador.start()

class BuscarLector(QtCore.QThread):
	def setup(self):
		self.signal = QtCore.SIGNAL("signal")
	def run(self):
		d = lectorDevice()
		try:
			d.autoset()
		except: 
			d.list_update()
		self.emit(self.signal, d)