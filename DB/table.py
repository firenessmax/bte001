#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re
from tableCreate import *
from itertools import cycle

class tabla(object):
	conexion = None
	consulta = None
	_esNuevo = False
	_listaDeCambio = {}
	_ident = None
	_identValue = None
	def getId(self):pass
	def borrar(self):pass
	def save(self):
		self.conexion = sqlite3.connect(DB)
		self.consulta = self.conexion.cursor()
		if self._esNuevo:
			self.insertar(self._listaDeCambio, self.__class__.__name__)
			self.conexion.commit()
			#self._identValue = self.getId()
		elif self._esNuevo == False and self._listaDeCambio != {}:
			 #print u"Se realizará un Update ..."
			self.update()
			self.conexion.commit()
		self._identValue = self.getId()
		self.consulta.close()
		self.conexion.close()
	
	def insertar(self, datos, nombre):
		argumentos = []
		llaves = []
		 #print u"verificación del formato de los datos ingresados..."
		for key in datos.keys():
			if validarTipo(datos[key][0], datos[key][1]):
				argumentos.append(datos[key][0])
				llaves.append(key)
			else:
				 #print ("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
				raise Exception("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
		 #print u"Verificación exitosa"
		
		ub = ""
		preg = ""
		for llave in llaves:
			ub += llave+","
			preg += "?,"
		ub = ub.strip(",")
		preg = preg.strip(",")
		sql ="INSERT INTO " +nombre+"("+ub+") VALUES ("+preg+")"
		# #print "slq : ", sql
		# #print "args : ", argumentos 
		argumentos = tuple(argumentos)
		
		if (self.consulta.execute(sql, argumentos)):
			pass
			 #print("registro guardado con exito")
		else: 
			raise Exception("ha ocurrido un problema al guardar el registro")
		
	def update(self):
		if not self._listaDeCambio=={}:
			argumentos = []
			llaves = []
			for key in self._listaDeCambio.keys():
				if validarTipo(self._listaDeCambio[key][0], self._listaDeCambio[key][1]):
					argumentos.append(self._listaDeCambio[key][0])
					llaves.append(key)
					# #print "Datos a updatear : ",key, " : ", self._listaDeCambio[key][0]
				else:
					 #print ("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
					raise Exception("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
			
			ub = ""
			for llave in llaves:
				ub += llave+" = ? ,"
			ub = ub.strip(",")
			if type(self._identValue) == str or type(self._identValue) == unicode:
				sql ="UPDATE "+self.__class__.__name__+ " SET "+ub+ " WHERE "+self._ident+"= '"+self._identValue+"'"
			else:
				sql ="UPDATE "+self.__class__.__name__+ " SET "+ub+ " WHERE "+self._ident+"= "+unicode(self._identValue)+""
			 #print "sql : ", sql
			argumentos = tuple(argumentos)
			# #print "args : ", argumentos
			
			if (self.consulta.execute(sql, argumentos)):
				self.conexion.commit()
				 #print("Update realizado con exito")
			else: 
				raise Exception("Se han econtrado problemas al realizar el Update")
				 #print ("Se han econtrado problemas al realizar el Update")
				
				
def digito_verificador( rut):
		reversed_digits = map(int, reversed(str(rut)))
		factors = cycle(range(2, 8))
		s = sum(d * f for d, f in zip(reversed_digits, factors))
		return (-s) % 11
				
def validarTipo(dato, tipo):
	if tipo == "bool":
		try:
			if type(dato) == bool:
				return True
			else:
				 #print "el dato debe ser de tippo boolean"
				return False
		except:
			 #print "el dato debe ser de tippo boolean"
			return False
	if tipo == "text":
		try:
			if type(dato) == str or type(dato) == unicode:
				return True
			else:
				 #print "el dato debe ser de tippo String o Unicode"
				return False
		except:
			 #print "el dato debe ser de tippo String o Unicode"
			return False
	if tipo == "int":
		try:
			if dato != None:
				dato = int(dato)
			else:
				 #print "el dato fue nulo"
				return True
		except ValueError:
			 #print (dato, " no es entero")
			return False
	elif tipo == "float":
		try:
			if dato != None:
				dato = float(dato) or int(dato)
			else:
				 #print "el dato no puede ser nulo"
				return False
		except ValueError:
			 #print (dato, " no es flotante")
			return False
	elif tipo == "rut":
		if dato == "0-0":return True
		if not re.match("\d{1,8}-[0-9k]", dato):
			 #print (dato, " : no coincide con el formato de rut")
			return False
		dato = dato.split("-")
		verificador = '0123456789k'[digito_verificador(dato[0])]
		if not verificador == dato[1]:
			return False
	return True				




