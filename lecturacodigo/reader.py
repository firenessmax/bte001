import serial, threading, time, signal, re
from PyQt4 import QtCore
from devices import lectorDevice
class serialEventListener():
	def handle(self,data,disp):pass
class serialReader(QtCore.QThread):
	pn='COM0'
	to=None
	_lector=None
	listeners=[]
	def setup(self,device,time_out):
		self.signal = QtCore.SIGNAL("signal")
		self.error = QtCore.SIGNAL("error")
		self.codError = QtCore.SIGNAL("errorCodigo")
		if isinstance(device,lectorDevice):
			self._lector=device
		else:
			raise Exception('el parametro device debe ser de tipo lectorDevice')
		self.to=time_out
	def dispatch(self,text):
		for l in self.listeners:
			#print "L"
			l.handle(text,self)
	def run(self):
		if self._lector.device['name'] == 'COMX':
			raise Exception('puerto no valido, revise coneccion')
		try:
			ser= serial.Serial(self._lector.device['name'],9600,timeout=self.to)
		except:
			self.emit(self.error)
		init=False
		bufer='';
		print self._isAlive
		while self._isAlive:
			#time.sleep(10)
			buf = ser.readline()
			if(buf!=''):
				bufer=bufer+buf
				init=True
			elif(bufer!='' and init):
				if re.match('<TED (.*)',bufer[2:]):
					self.emit(self.signal, bufer[2:], self)
					ser.close()
				else:
					self.emit(self.codError, "el codigo no es valido", self)
				bufer=''
				
				break
	def open(self):
		self._isAlive=True
		self.start()
	def close(self):
		if self._isAlive:
			self._isAlive=False
			#self.ser.close()

	def addEventListener(self,lst):
		
		if isinstance(lst,serialEventListener):
			self.listeners.append(lst)
		else:
			raise Exception('el objeto no es una instancia de serialEventListener')

# f=serialReader('/dev/ttys003',.01)
# class escuchante(serialEventListener):
# 	cont=0
# 	def handle(self,data,disp):
# 		print data
# 		'''
# 		se recomienda cerrar y reabrir al terminar el ingreso
# 		de ese modo nos evitamos problemas con procesos atrapados y
# 		el tener que pausar y capturar mas de una a la vez
# 		'''
# 		disp.close()
# e=escuchante()
# f.addEventListener(e)
# f.open()
