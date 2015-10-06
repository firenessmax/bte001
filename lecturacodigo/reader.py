import serial, threading, time, signal
from devices import lectorDevice
class serialEventListener():
	def handle(self,data,disp):pass
class serialReader(threading.Thread):
	_busy = False
	@property
	def busy(self):
		return self._busy
	@busy.setter
	def busy(self,val):
		self._busy = val
	pn='COM0'
	to=None
	_lector=None
	listeners=[]
	def __init__(self,device,time_out):
		threading.Thread.__init__(self)
		self._stop = threading.Event()
		if isinstance(device,lectorDevice):
			self._lector=device
		else:
			raise Exception('el parametro device debe ser de tipo lectorDevice')
		self.to=time_out
	def dispatch(self,text):
		for l in self.listeners:
			l.handle(text,self)
	def signal_handler(self,signal, frame):
		print 'You pressed Ctrl+C!'
		self.close()
	def run(self):
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
				self.dispatch(bufer)
				bufer=''
	def open(self):
		signal.signal(signal.SIGINT, self.signal_handler)
		self.start()
	def close(self):
		if self.isAlive():
			self._Thread__stop()
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
