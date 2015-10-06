import os, pty, serial, time
from devices import lectorDevice
from reader import *
from xmlLib import XMLprocessor

class eventHandler(serialEventListener):
	counter = 0
	def handle(self,data,disp):
		self.counter=self.counter+1
		xmlp= XMLprocessor(data)
		print xmlp.TD, xmlp.F, xmlp.RS, xmlp.RSR
		if self.counter==5:
			print 'prueba finalizada'
			disp.close()

print "Prueba de conexion virtual"
d = lectorDevice()
el=eventHandler()

print d.device['frendly_name'],d.device['name']


#master, slave = pty.openpty()
#s_name = os.ttyname(slave)
#s_name = "/dev/ttys003"
#ser = serial.Serial(s_name,9600,timeout=.01)
ser = serialReader(d,.01)

ser.addEventListener(el)

print "agregado event listener"

ser.open()
print "conexion iniciada"