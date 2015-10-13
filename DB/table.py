#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re


class tabla(object):
	conexion = None
	consulta = None
	_esNuevo = False
	_listaDeCambio = {}
	_ident = None
	_identValue = None
	def getId(self):pass
	def save(self):
		self.conexion = sqlite3.connect('prueba.db')
		self.consulta = self.conexion.cursor()
		if self._esNuevo:
			self.insertar(self._listaDeCambio, self.__class__.__name__)
			self.conexion.commit()
			self._identValue = self.getId()
		elif self._esNuevo == False and self._listaDeCambio != {}:
			print u"Se realizará un Update ..."
			self.update()
			self.conexion.commit()
		self.consulta.close()
		self.conexion.close()
		
	def insertar(self, datos, nombre):
		argumentos = []
		llaves = []
		print u"verificación del formato de los datos ingresados..."
		for key in datos.keys():
			if validarTipo(datos[key][0], datos[key][1]):
				argumentos.append(datos[key][0])
				llaves.append(key)
			else:
				print ("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
				raise Exception("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
		print u"Verificación exitosa"
		
		ub = ""
		preg = ""
		for llave in llaves:
			ub += llave+","
			preg += "?,"
		ub = ub.strip(",")
		preg = preg.strip(",")
		sql ="INSERT INTO " +nombre+"("+ub+") VALUES ("+preg+")"
		
		argumentos = tuple(argumentos)
		
		if (self.consulta.execute(sql, argumentos)):
			print("registro guardado con exito")
		else: ("ha ocurrido un problema al guardar el registro")
		
	def update(self):
		if not self._listaDeCambio=={}:
			argumentos = []
			llaves = []
			for key in self._listaDeCambio.keys():
				if validarTipo(self._listaDeCambio[key][0], self._listaDeCambio[key][1]):
					argumentos.append(self._listaDeCambio[key][0])
					llaves.append(key)
					print "Datos a updatear : ",key, " : ", self._listaDeCambio[key][0]
				else:
					print ("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
					raise Exception("Error al escribir el dato: ", datos[key][0],", no posee el formato : ", datos[key][1])
			
			ub = ""
			for llave in llaves:
				ub += llave+" = ? ,"
			ub = ub.strip(",")
			if type(self._identValue) == str or type(self._identValue) == unicode:
				sql ="UPDATE "+self.__class__.__name__+ " SET "+ub+ " WHERE "+self._ident+"= '"+self._identValue+"'"
			else:
				sql ="UPDATE "+self.__class__.__name__+ " SET "+ub+ " WHERE "+self._ident+"= "+str(self._identValue)+""
			print "sql : ", sql
			argumentos = tuple(argumentos)
			print "args : ", argumentos
			
			if (self.consulta.execute(sql, argumentos)):
				self.conexion.commit()
				print("Update realizado con exito")
			else: 
				print ("Se han econtrado problemas al realizar el Update")
				
				
				
def validarTipo(dato, tipo):
	if tipo == "bool":
		try:
			if type(dato) == bool:
				return True
			else:
				print "el dato debe ser de tippo boolean"
				return False
		except:
			print "el dato debe ser de tippo boolean"
			return False
	if tipo == "text":
		try:
			if type(dato) == str or type(dato) == unicode:
				return True
			else:
				print "el dato debe ser de tippo String o Unicode"
				return False
		except:
			print "el dato debe ser de tippo String o Unicode"
			return False
	if tipo == "int":
		try:
			if dato != None:
				dato = int(dato)
			else:
				print "el dato fue nulo"
				return True
		except ValueError:
			print (dato, " no es entero")
			return False
	elif tipo == "float":
		try:
			if dato != None:
				dato = float(dato) or int(dato)
			else:
				print "el dato no puede ser nulo"
				return False
		except ValueError:
			print (dato, " no es flotante")
			return False
	elif tipo == "rut":
		if not re.match("\d{1,8}-[0-9k]", dato):
			print (dato, " : no coincide con el formato de rut")
			return False
		dato = dato.split("-")
		verificador = '0123456789k'[
			11 - sum(
				[int(digit) * factor
				for digit, factor in zip(dato[0][::-1], 2 * range(2,8))]
			) % 11
		]
		if not verificador == dato[1]:
			return False
	return True				





def obtenerCompras(rutReceptor):
	conexion = sqlite3.connect('prueba.db')
	consulta = conexion.cursor()
	listaFacturas=[]
	if rutReceptor == None:
		for row in consulta.execute("SELECT * FROM facturas WHERE venta = 0"):
			listaFacturas.append(facturas(venta = row[1], numDocumento = row[4], rutReceptor = row[10],
											rutEmisor = row[8], esNuevo = False))
	else:
		#consulta sql donde rutReceptor
		for row in consulta.execute("SELECT * FROM facturas WHERE rutReceptor = ? AND venta = 0", (rutReceptor,)):
			#row[0] = id
			#row[1] = venta
			#row[2] = sucursal
			#row[3] = TipoDocumento
			#row[4] = numDocumento
			#row[5] = nulo
			#row[6] = correlativo
			#row[7] = fecha
			#row[8] = rutEmisor
			#row[9] = nomEmisor
			#row[10] = rutReceptor
			#row[11] = nomReceptor
			#row[12] = montoExento
			#row[13] = montoAfecto
			#row[14] = montoIVA
			#row[15] = montoTotal
			#row[16] = Glosa
			#row[17] = cuentaProveedores
			#row[18] = codigoEspecial
			#row[19] = fechaVencimiento
			#row[20] = contracuenta
			#row[21] = centroResultados
			#row[22] = activoFijo
			#row[23] = sinDerechoaCredito
			#row[24] = conCreditoFiscal
			#row[25] = mImpuestoEspecifico1
			#row[26] = mImpuestoEspecifico2
			#row[27] = impuestoEspecificoFijo
			#row[28] = impuestoEspecificoVariable
			#row[29] = M3
			#row[30] = codImpuesto2
			#row[31] = montoImpuesto2
			#row[32] = codImpuesto3
			#row[33] = montoImpuesto3
			#row[34] = contabilizado
			#row[35] = idUsuario
			#factura(venta, numDocumento, rutReceptor, esNuevo)
			listaFacturas.append(facturas(venta = row[1], numDocumento = row[4], rutReceptor = row[10],
											rutEmisor = row[8], esNuevo = False))
		#f = factura(..., evNuevo = False)-> lista de facturas
	consulta.close()
	conexion.close()
	return listaFacturas
	
	

def obtenerVentas(rutEmisor):
	conexion = sqlite3.connect('prueba.db')
	consulta = conexion.cursor()
	listaFacturas=[]
	if rutEmisor == None:
		for row in consulta.execute("SELECT * FROM facturas WHERE venta = 1"):
			listaFacturas.append(facturas(venta = row[1], numDocumento = row[4], rutReceptor = row[10],
											rutEmisor = row[8], esNuevo = False))
	else:
		#consulta sql donde rutEmisor
		for row in consulta.execute("SELECT * FROM facturas WHERE rutEmisor = ? AND venta = 1", (rutEmisor,)):
			listaFacturas.append(facturas(venta = row[1], numDocumento = row[4], rutReceptor = row[10],
											rutEmisor = row[8], esNuevo = False))
		#f = factura(..., evNuevo = False)-> lista de facturas
	consulta.close()
	conexion.close()
	return listaFacturas

