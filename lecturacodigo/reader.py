import serial, threading, time, signal
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
	listeners=[]
	def __init__(self,portname,time_out):
		threading.Thread.__init__(self)
		self._stop = threading.Event()
		self.pn=portname
		self.to=time_out
		
	def dispatch(self,text):
		for l in self.listeners:
			l.handle(text,self)
	def signal_handler(self,signal, frame):
		print 'You pressed Ctrl+C!'
		#sys.exit(0)
		self.close()
	def run(self):
		ser= serial.Serial(self.pn,9600,timeout=self.to)
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
