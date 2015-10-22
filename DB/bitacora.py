#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re
import sys
from table import *



class bitacora(tabla):
	_id = 0
	_fecha = "aaaa-mm-dd"
	_tipo = ""
	_evento = ""
	_so = ""
	_idUsuario = 0
	@property
	def id(self):
		return self._id
	@property
	def fecha(self):
		formato1 = "%Y-%m-%d" # aaaa-mm-dd
		formato2 = "%d/%m/%Y" # dd/mm/aaaa
		
		fecha = datetime.strptime(self._fecha, formato1)
		#print "fehca : ", fecha
		fechaFromateada = fecha.strftime(formato2)
		#print "fechaFromateada : ", fechaFromateada
		return fechaFromateada
	@fecha.setter
	def fecha(self, data):
		self._fecha = data
		self._listaDeCambio['fecha'] = (data, 'text')
		#print 'cambio: ',self._listaDeCambio
	@property
	def tipo(self):
		return self._tipo
	@tipo.setter
	def tipo(self, data):
		self._tipo = data
		self._listaDeCambio['tipo'] = (data, 'text')
		#print 'cambio: ',self._listaDeCambio
	@property
	def evento(self):
		return self._evento
	@evento.setter
	def evento(self, data):
		self._evento = data
		self._listaDeCambio['evento'] = (data, 'text')
		#print 'cambio: ',self._listaDeCambio
	@property
	def so(self):
		return self._so
	@so.setter
	def so(self, data):
		self._so = data
		self._listaDeCambio['so'] = (data, 'text')
		#print 'cambio: ',self._listaDeCambio
	@property
	def idUsuario(self):
		return self._idUsuario
	@idUsuario.setter
	def idUsuario(self, data):
		self._idUsuario = data
		self._listaDeCambio['idUsuario'] = (data, 'int')
		#print 'cambio: ',self._listaDeCambio
	
		
	
	def __init__(self, tipo = "", evento = "", idUsuario = 0, id = 0, esNuevo = True):
		fecha = datetime.datetime.now()
		#print fecha
		self._fecha = fecha.strftime("%d-%m-%Y %H:%M:%S")
		#print self._fecha
		self._tipo = tipo
		self._evento = evento
		self._so = sys.platform
		self._idUsuario = idUsuario
		self._ident = "id"
		self._listaDeCambio = {
			"fecha":(self._fecha, "fecha"),
			"tipo":(self._tipo, "text"),
			"evento":(self._evento, "text"),
			"so":(self._so, "text"),
			"idUsuario":(self._idUsuario, "int")
		}
		#print self._listaDeCambio
		self._esNuevo = True
			
#prueba = bitacora(tipo = "insertar", evento = "creo una factura")
#prueba.save()