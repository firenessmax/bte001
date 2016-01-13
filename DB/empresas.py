#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re
from table import *
from tableCreate import *

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
		#print "cambios : ", self._listaDeCambio
	def getId(self):
		if(self.consulta.execute("SELECT id FROM empresas WHERE rut = ?", (self._rut,))):
			self._id = self.consulta.fetchone()[0]
			return self._id
	def __init__(self, rut, rs="", esNuevo = True, id = 0):
		self._rut = rut
		self._rS = rs
		if esNuevo:
			conexion = sqlite3.connect(DB)
			consulta = conexion.cursor()
			exist = '''
			SELECT COUNT(*) FROM empresas
			WHERE rut=(?)
			'''
			tuplaRut = (rut,)

			if (consulta.execute(exist, tuplaRut)):	
				count = consulta.fetchone()
				self._ident = "id"

				if count[0] == 0:
					self._listaDeCambio={"rut":(rut, "rut"), "razonSocial":(rs,"text")}
					self._esNuevo = True
				else:
					self._listaDeCambio = {}
					self._esNuevo = False
					raise Exception(u"No se puede crear porque ya existe esta empresa : ", rut)	
			else:
				raise Exception("Error en la conexion con la base de datos")
				#print "Error en la conexion con la base de datos"
			consulta.close()
			conexion.close()
		else:
			conexion = sqlite3.connect(DB)
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
	conexion = sqlite3.connect(DB)
	consulta = conexion.cursor()
	listaEmpresas = []
	idEmpresas = []
	rutEmpresas= []
	for row in consulta.execute('''SELECT rut 
									FROM empresas, facturas
									WHERE (empresas.id = facturas.idReceptor AND facturas.venta = 0) 
									OR (empresas.id = facturas.idEmisor AND facturas.venta = 1) GROUP BY rut'''):
		rutEmpresas.append(row[0])
	for rut in rutEmpresas:#list(set(idEmpresas())):
		#if(consulta.execute("SELECT rut FROM empresas WHERE id = ?", (id,))): 	
		#	row = consulta.fetchone()
		listaEmpresas.append(empresas(rut, esNuevo = False))
	consulta.close()
	conexion.close()
	return listaEmpresas
class codigosDocumento(tabla):
	_id = 0
	_empresa = None
	_33  = "FE" #factura electronica
	_33p = "FP" #factura parcial electronica
	_34  = "FT"
	 #factura excenta electronica
	_46  = "FE" #factura de compra electronica
	_46p = "FP" #factura de compra parcial electronica
	_56  = "ND" #nota debito electronica

	_56p = "ND" #nota debito parcial electronica
	_61  = "NE" #nota credito electronica
	_61p = "NE" #nota credito parcial electronica
	#** yo dejaria esto para una especie de segunda parte
	_39  = "" #boleta electronica TODO: preguntar si hay parcial
	_41  = "" #boleta electronica excenta
	_43  = "" #Liquidacion Factura Electronica
	_101 = "" #factura exportación
	_111 = "" #Nota de Debito de Exportacion Electronica
	_112 = "" #Nota de Credito Exportacion Electronica

	@property
	def c33 (self):
		return self._33 
	@c33.setter
	def c33 (self,data):
		self._33  =data
		self._listaDeCambio["c33"] = (data,"text")   
	@property
	def c33p(self):
		return self._33p
	@c33p.setter
	def c33p(self,data):
		self._33p =data
		self._listaDeCambio["c33p"] = (data,"text")   
	@property
	def c34 (self):
		return self._34 
	@c34.setter
	def c34 (self,data):
		self._34  =data
		self._listaDeCambio["c34"] = (data,"text")   
	@property
	def c46 (self):
		return self._46 
	@c46.setter
	def c46 (self,data):
		self._46  =data
		self._listaDeCambio["c46"] = (data,"text")   
	@property
	def c46p(self):
		return self._46p
	@c46p.setter
	def c46p(self,data):
		self._46p =data
		self._listaDeCambio["c46p"] = (data,"text")   
	@property
	def c56 (self):
		return self._56 
	@c56.setter
	def c56 (self,data):
		self._56  =data
		self._listaDeCambio["c56"] = (data,"text")   
	@property
	def c56p(self):
		return self._56p
	@c56p.setter
	def c56p(self,data):
		self._56p =data
		self._listaDeCambio["c56p"] = (data,"text")   
	@property
	def c61 (self):
		return self._61 
	@c61.setter
	def c61 (self,data):
		self._61  =data
		self._listaDeCambio["c61"] = (data,"text")   
	@property
	def c61p(self):
		return self._61p
	@c61p.setter
	def c61p(self,data):
		self._61p =data
		self._listaDeCambio["c61p"] = (data,"text")   
#para mas despues
	@property
	def c39 (self):
		return self._39 
	@c39.setter
	def c39 (self,data):
		self._39  =data
		self._listaDeCambio["c39"] = (data,"text")   
	@property
	def c41 (self):
		return self._41 
	@c41.setter
	def c41 (self,data):
		self._41  =data
		self._listaDeCambio["c41"] = (data,"text")   
	@property
	def c43 (self):
		return self._43 
	@c43.setter
	def c43 (self,data):
		self._43  =data
		self._listaDeCambio["c43"] = (data,"text")   
	@property
	def c101(self):
		return self._101
	@c101.setter
	def c101(self,data):
		self._101 =data
		self._listaDeCambio["c101"] = (data,"text")   
	@property
	def c111(self):
		return self._111
	@c111.setter
	def c111(self,data):
		self._111 =data
		self._listaDeCambio["c111"] = (data,"text")   
	@property
	def c112(self):
		return self._112
	@c112.setter
	def c112(self,data):
		self._112 =data
		self._listaDeCambio["c112"] = (data,"text")   
	def __init__(self, empresa):
		self._empresa=empresa
		conexion = sqlite3.connect(DB)
		consulta = conexion.cursor()
		exist = '''
		SELECT COUNT(*) FROM codigosDocumento
		WHERE empresaId=(?)
		'''
		tuplaEmpresa = (empresa.id,)
		if (consulta.execute(exist, tuplaEmpresa)):	
			count = consulta.fetchone()
			self._ident = "id"
			if count[0] == 0:
				self._listaDeCambio={"empresaId":(empresa.id, "int"), 
					"c33"  :(self._33 ,"text"),
					"c33p" :(self._33p,"text"),
					"c34"  :(self._34 ,"text"),
					"c46"  :(self._46 ,"text"),
					"c46p" :(self._46p,"text"),
					"c56"  :(self._56 ,"text"),
					"c56p" :(self._56p,"text"),
					"c61"  :(self._61 ,"text"),
					"c61p" :(self._61p,"text"),
					"c39"  :(self._39 ,"text"),
					"c41"  :(self._41 ,"text"),
					"c43"  :(self._43 ,"text"),
					"c101" :(self._101,"text"),
					"c111" :(self._111,"text"),
					"c112" :(self._112,"text")}
				self._esNuevo = True
			else:
				self._listaDeCambio = {}
				self._esNuevo = False
				conexion = sqlite3.connect(DB)
				consulta = conexion.cursor()
				if(consulta.execute("SELECT * FROM codigosDocumento WHERE empresaId = ?", (empresa.id,))): 	
					row = consulta.fetchone()
					self._id = row[0]
					#self._empresa.id = row[1]
					self._33  = row[2];  self._33p = row[3]
					self._34  = row[4];  self._46  = row[5]
					self._46p = row[6];  self._56  = row[7]
					self._56p = row[8];  self._61  = row[9]
					self._61p = row[10]; self._39  = row[11]
					self._41  = row[12]; self._43  = row[13]
					self._101 = row[14]; self._111 = row[15]
					self._112 = row[16]

					self._ident = "id"
					self._identValue = self._id
					self._listaDeCambio = {}
					self._esNuevo = False
		else:
			raise Exception("Error en la conexion con la base de datos")
		consulta.close()
		conexion.close()



for empresa in obtenerEmpresas():
	print empresa.rut
	print empresa.rS