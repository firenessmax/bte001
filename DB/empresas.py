#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re
from table import *

# esta clase sirve para insertar, updatear y deletear(no hecho aun)
# elementos de empresas en la base de ddatos
# instanciamiento:
# e = empresas(rut = "1792081-8", razonSocial = "nombre de la empresa")
# funciones y metodos:
# e.save()
class empresas(tabla):
	_rut = None
	_rS = None
	@property
	def rut(self):
		return self._rut
	@property
	def rS(self):
		return self._rS
	@rS.setter
	def rS(self, data):
		self._rS = data
		self._listaDeCambio["razonSocial"] = (data, "text")
		print "cambios : ", self._listaDeCambio
	def getId(self):
		return self._rut
	def __init__(self, rut, rs="", esNuevo = True):
		self._rut = rut
		self._rS = rs
		if esNuevo:
			conexion = sqlite3.connect('prueba.db')
			consulta = conexion.cursor()
			exist = '''
			SELECT COUNT(*) FROM empresas
			WHERE rut=(?)
			'''
			tuplaRut = (rut,)
			if (consulta.execute(exist, tuplaRut)):
				count = consulta.fetchone()
				self._ident = "rut"
				self._identValue = rut
				if count[0] == 0:
					self._listaDeCambio={"rut":(rut, "rut"), "razonSocial":(rs,"text")}
					self._esNuevo = True
				else:
					self._listaDeCambio = {}
					self._esNuevo = False
					raise Exception(u"No se puede crear porque ya existe esta empresa : ", rut)	
			else:
				print "Error en la conexion con la base de datos"
			consulta.close()
			conexion.close()
		else:
			self._ident = "rut"
			self._identValue = rut
			self._listaDeCambio = {}
			self._esNuevo = False
