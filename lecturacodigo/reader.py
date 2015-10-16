import serial, threading, time, signal
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
		if isinstance(device,lectorDevice):
			self._lector=device
		else:
			raise Exception('el parametro device debe ser de tipo lectorDevice')
		self.to=time_out
	def dispatch(self,text):
		for l in self.listeners:
			print "L"
			l.handle(text,self)
	def signal_handler(self,signal, frame):
		print 'You pressed Ctrl+C!'
		self.close()
	def run(self):
		print "CONEXION INICIADA"
		if self._lector.device['name'] == 'COMX':
			raise Exception('puerto no valido, revise coneccion')
		ser= serial.Serial(self._lector.device['name'],9600,timeout=self.to)
		init=False
		bufer='';
		while 1:
			#time.sleep(10)
			buf = ser.readline()
			if(buf!=''):
				bufer=bufer+buf
				init=True
			elif(bufer!='' and init):
				self.emit(self.signal, bufer[2:], self)
				bufer=''
				ser.close()
				break
	def open(self):
		signal.signal(signal.SIGINT, self.signal_handler)
		self.start()
	def close(self):
		if self.isRunning():
			pass
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
