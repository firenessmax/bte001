
from PyQt4 import QtCore
from lecturacodigo.devices import lectorDevice
from lecturacodigo.reader import *


def iniciarReader(s):
	d = lectorDevice()

	print d.device['frendly_name'],d.device['name']
	ser = serialReader()
	ser.setup(d,.01)

	s.connect(ser, ser.signal, s.enc)
	print "agregado event listener"
	ser.open()
	print "conexion iniciada"
	return ser
