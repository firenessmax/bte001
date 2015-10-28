
from PyQt4 import QtCore
from lecturacodigo.devices import lectorDevice
from lecturacodigo.reader import *
from lecturacodigo.lectores import debug

def iniciarReader(s, d):
	ser = serialReader()
	ser.setup(d,.01)

	s.connect(ser, ser.signal, s.enc)
	ser.open() 
	return ser

def iniciarDevice(s):
	s.ui.label_5.show()
	s.ui.dispositivosComboBox.clear()
	s.ui.dispositivosComboBox.setEnabled(False)
	s.ui.escanearCompra.setEnabled(False)
	s.ui.escanearVenta.setEnabled(False)
	s.ui.pushButtonDevice.setEnabled(False)
	s.ui.statusbar.showMessage("Buscando dispositivos...")
	s.buscador = BuscarLector()
	s.buscador.setup()
	s.connect(s.buscador, s.buscador.signal, s.deviceEncontrado)
	s.connect(s.buscador, s.buscador.signalWarning, s.deviceNoEncontrado)
	s.buscador.start()

class BuscarLector(QtCore.QThread):
	def setup(self):
		self.signal = QtCore.SIGNAL("signal")
		self.signalWarning = QtCore.SIGNAL("signalWarning")
	def run(self):
		d = lectorDevice()
		try:
			d.autoset()
			self.emit(self.signal, d)
		except: 
			if(debug):
				d.list_update()
				self.emit(self.signal, d)
			else:
				self.emit(self.signalWarning)
		#print d.device
		