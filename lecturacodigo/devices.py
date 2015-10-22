import serial.tools.list_ports as lp
from lectores import *
import re, time


class lectorDevice(object):
	_device=({'frendly_name':'Puerto serial virtual Modo Debug','name':'COM4'},{'frendly_name':'No hay lectores conectados','name':'COMX'})[not debug]
	_device_list=[]
	@property
	def device(self):
	    return self._device
	@device.setter
	def device(self,value):
		#print "almenos lo intento"
		self._device=self._device_list[value]

	@property
	def device_list(self):
	    return self._device_list
	'''selecciona automaticamente la primera pistola que sea compatible y la deja como seleccionada'''
	def autoset(self):
		for i in range(5):
			if len(self._device_list) > 0:
				break
			self.list_update()
			if len(self._device_list) < 1:
				if i == 4:
					raise Exception("Se agotaron los intentos, no se encontraron lectores conectados")
				time.sleep(1)
		self._device=self._device_list[0]
	def list_update(self):
		#primero reseteamos en caso de que lo cambie de puerto
		self._device_list=[]
		#luego agregamos los lectores validos
		for p in list(lp.comports()):
			print p
			if self.lector_valido(p[1]):
				self._device_list.append({'frendly_name':p[1],'name':p[0]})
		if len(self._device_list)==0:
			self._device=({'frendly_name':'Puerto serial virtual Modo Debug','name':'COM4'},{'frendly_name':'No hay lectores conectados','name':'COMX'})[not debug]
	def lector_valido(self,frendly_name):
		for lector in LISTA_LECTORES:
			if re.match(lector,frendly_name):
				return True
		return False 
