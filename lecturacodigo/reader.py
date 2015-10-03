import serial, threading
class serialReader():
	_busy = False
	@property
	def busy(self):
		return self._busy
	@busy.setter
	def busy(self,val):
		self._busy = val
	pn='COM0'
	to=None
	thread=None
	port=None
	def __init__(self,portname,time_out):
		self.pn=portname
		self.to=time_out
	def serialRead(self):
		print "deberia activar el evento"
		return
	def open(self):
		thread= threading.Thread(target=serialRead)
	def close(self):
		pass

f=serialReader('/dev/ttys003',.01)
f.open()