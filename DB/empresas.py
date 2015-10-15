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
	_id = 0
	_rut = ""
	_rS = ""
	@property
	def id(self):
		return self._id
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
		if(self.consulta.execute("SELECT id FROM empresas WHERE rut = ?", (self._rut,))):
			self._id = self.consulta.fetchone()[0]
			return self._id
	def __init__(self, rut, rs="", esNuevo = True, id = 0):
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
				print "contador <<<<<<<<<<<: ", count[0]
				self._ident = "id"
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
			conexion = sqlite3.connect('prueba.db')
			consulta = conexion.cursor()
			if(consulta.execute("SELECT * FROM empresas WHERE rut = ?", (self.rut,))): 	
				row = consulta.fetchone()
				self._id = row[0]
				self._rut = row[1]
				self._rS = row[2]
				
				
				self._ident = "id"
				self._identValue = self._id
				self._listaDeCambio = {}
				self._esNuevo = False

			consulta.close()
			conexion.close()
			

def obtenerEmpresas():
	conexion = sqlite3.connect('prueba.db')
	consulta = conexion.cursor()
	listaEmpresas = []
	for row in consulta.execute("SELECT * FROM empresas"):
		listaEmpresas.append(empresas(row[1], esNuevo = False))
	consulta.close()
	conexion.close()
	return listaEmpresas
	