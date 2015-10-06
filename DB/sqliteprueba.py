#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import re

conexion = sqlite3.connect('prueba.db')

cursor = conexion.cursor()

print u"La base de datos se abrió correctamente"

cursor.execute(''' CREATE TABLE IF NOT EXISTS facturas (   venta INTEGER  DEFAULT 0, sucursal INTEGER, TipoDocumento INTEGER, numDocumento INTEGER, nulo INTEGER DEFAULT 0, correlativo INTEGER, fecha TEXT, rutEmisor TEXT, nomEmisor TEXT, rutReceptor TEXT, nomReceptor TEXT, montoExento INTEGER , montoAfecto INTEGER, montoIVA INTEGER, montoTotal INTEGER, Glosa TEXT, cuentaProveedores TEXT, codigoEspecial TEXT, fechaVencimiento TEXT, contracuenta INTEGER, centroResultados TEXT, activoFijo INTEGER DEFAULT 0, sinDerechoaCredito INTEGER DEFAULT 0, conCreditoFiscal INTEGER DEFAULT 0, mImpuestoEspecifico1 INTEGER, mImpuestoEspecifico2 INTEGER, impuestoEspecificoFijo INTEGER, impuestoEspecificoVariable INTEGER, M3 TEXT, CodImpuesto2 TEXT, montoImpuesto2 INTEGER, codImpuesto3 TEXT, montoImpuesto3 INTEGER, contabilizado INTEGER DEFAULT 0, idUsuario INTEGER DEFAULT 0)''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS usuario ( id INTEGER PRIMARY KEY, username TEXT, pass TEXT, activo INTEGER DEFAULT 1)  ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS empresas ( rut TEXT, razonSocial TEXT) ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS bitacora ( id INTEGER PRIMARY KEY, fecha TEXT,tipo INTEGER, evento TEXT, so TEXT, idUsuario INTEGER DEFAULT 0) ''')

#cursor.execute("INSERT INTO usuario (username, pass) VALUES ('cristian', '1234')")
#cursor.execute("INSERT INTO usuario (username, pass) VALUES ('nestor', 'ewerqwef')")
#con.commit()
conexion.close()

class tabla(object):
	conexion = None
	consulta = None
	_esNuevo = False
	_listaDeCambio = {}
	_ident = None
	_identValue = None
	def save(self):
		print self._esNuevo	
		if self._esNuevo:
			self.insertar(self._listaDeCambio, self.__class__.__name__)
		else:
			self.update()
		self.consulta.close()
		self.conexion.commit()
		self.conexion.close()
		
	def insertar(self, datos, nombre):
		argumentos = []
		llaves = []
		for key in datos.keys():
			if validarTipo(datos[key][0], datos[key][1]):
				argumentos.append(datos[key][0])
				llaves.append(key)
				print datos[key][0]
			else:
				print ("error al escribir ", key)
				raise Exception("Error al escribir el dato")
		
		self.conexion = sqlite3.connect('prueba.db')
		self.consulta = self.conexion.cursor()
		
		ub = ""
		preg = ""
		for llave in llaves:
			ub += llave+","
			preg += "?,"
		ub = ub.strip(",")
		preg = preg.strip(",")
		print "ub = ", ub
		print "preg = ", preg
		sql ="INSERT INTO " +nombre+"("+ub+") VALUES ("+preg+")"
		
		argumentos = tuple(argumentos)
		
		if (self.consulta.execute(sql, argumentos)):
			print("registro guardado con exito")
		else: ("ha ocurrido un problema al guardar el registro")
		
	def update(self):
		argumentos = []
		llaves = []
		for key in self._listaDeCambio.keys():
			if validarTipo(self._listaDeCambio[key][0], self._listaDeCambio[key][1]):
				argumentos.append(self._listaDeCambio[key][0])
				llaves.append(key)
				print self._listaDeCambio[key][0]
			else:
				print ("error al escribir ", key)
				raise Exception("El dato : ", self._listaDeCambio[key][0], "no tiene el formato : ", self._listaDeCambio[key][1])
		
		self.conexion = sqlite3.connect('prueba.db')
		self.consulta = self.conexion.cursor()
		
		ub = ""
		for llave in llaves:
			ub += llave+" = ? ,"
		ub = ub.strip(",")
		print "ub = ", ub
		sql ="UPDATE "+self.__class__.__name__+ " SET "+ub+ " WHERE "+self._ident+"= '"+self._identValue+"'"
		print sql
		argumentos = tuple(argumentos)
		print "args ", argumentos
		
		if (self.consulta.execute(sql, argumentos)):
			self.conexion.commit()
			print("Update realizado con exito")
		else: 
			print ("Se han econtrado problemas al realizar el Update")


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
		print self._listaDeCambio
	#@rut.setter
	#def rut(self, data):
	#	self._rut = data
	#	super._dicc["rut"] = (data, "rut")
	def __init__(self, rut, rs):
		self._rut = rut
		self._rS = rs
		conexion = sqlite3.connect('prueba.db')
		consulta = conexion.cursor()
		exist = '''
		SELECT COUNT(*) FROM empresas
		WHERE rut=(?)
		'''
		lista = []
		lista.append(rut)
		lista = tuple(lista)
		if (consulta.execute(exist, lista)):
			count = consulta.fetchone()
			self._ident = "rut"
			self._identValue = rut
			if count[0] == 0:
				self._listaDeCambio={"rut":(rut, "rut"), "razonSocial":(rs,"text")}
				self._esNuevo = True
			else:
				print "no se puede crear porque ya existe el rut en la base de datos"
				self._listaDeCambio = {}
				self._esNuevo = False
		else:
			print "Error en la conexion con la base de datos"
		consulta.close()
		conexion.close()

class facturas(tabla):
	_venta = None
	_sucursal = None
	_TiopDocumento = None
	_numDocumento = None
	_nulo = None
	_correlativo = None
	_fecha = None
	_rutEmisor = None
	_nomEmisor = None
	_rutReceptor = None
	_nomReceptor = None
	_montoExento = None
	_montoAfecto = None
	_montoIVA = None
	_montoTotal = None
	_Glosa = None
	_cuentaProveedores = None
	_codigoEspecial = None
	_fechaVencimiento = None
	_contracuenta = None
	_centroResultados = None
	_activoFijo = None
	_sinDerechoaCredito = None
	_conCreditoFiscal = None
	_mImpuestoEspecifico1 = None
	_mImpuestoEspecifico2 = None
	_impuestoEspecificoFijo = None
	_impuestoEspecificoVariable = None
	_M3 = None
	_montoImpuesto2 = None
	_codImpuesto3 = None
	_montoImpuesto3 = None
	_contabilizado = None
	_idUsuario = None
	@property
	def venta(self):
		return self._venta
	@venta.setter
	def venta(self, data):
		self._venta = data
		self._listaDeCambio['venta'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def sucursal(self):
		return self._sucursal
	@sucursal.setter
	def sucursal(self, data):
		self._sucursal = data
		self._listaDeCambio['sucursal'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def TiopDocumento(self):
		return self._TiopDocumento
	@TiopDocumento.setter
	def TiopDocumento(self, data):
		self._TiopDocumento = data
		self._listaDeCambio['TiopDocumento'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def numDocumento(self):
		return self._numDocumento
	@property
	def nulo(self):
		return self._nulo
	@nulo.setter
	def nulo(self, data):
		self._nulo = data
		self._listaDeCambio['nulo'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def correlativo(self):
		return self._correlativo
	@correlativo.setter
	def correlativo(self, data):
		self._correlativo = data
		self._listaDeCambio['correlativo'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def fecha(self):
		return self._fecha
	@fecha.setter
	def fecha(self, data):
		self._fecha = data
		self._listaDeCambio['fecha'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def rutEmisor(self):
		return self._rutEmisor
	@property
	def nomEmisor(self):
		return self._nomEmisor
	@nomEmisor.setter
	def nomEmisor(self, data):
		self._nomEmisor = data
		self._listaDeCambio['nomEmisor'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def rutReceptor(self):
		return self._rutReceptor
	@property
	def nomReceptor(self):
		return self._nomReceptor
	@nomReceptor.setter
	def nomReceptor(self, data):
		self._nomReceptor = data
		self._listaDeCambio['nomReceptor'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoExento(self):
		return self._montoExento
	@montoExento.setter
	def montoExento(self, data):
		self._montoExento = data
		self._listaDeCambio['montoExento'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoAfecto(self):
		return self._montoAfecto
	@montoAfecto.setter
	def montoAfecto(self, data):
		self._montoAfecto = data
		self._listaDeCambio['montoAfecto'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoIVA(self):
		return self._montoIVA
	@montoIVA.setter
	def montoIVA(self, data):
		self._montoIVA = data
		self._listaDeCambio['montoIVA'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoTotal(self):
		return self._montoTotal
	@montoTotal.setter
	def montoTotal(self, data):
		self._montoTotal = data
		self._listaDeCambio['montoTotal'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def Glosa(self):
		return self._Glosa
	@Glosa.setter
	def Glosa(self, data):
		self._Glosa = data
		self._listaDeCambio['Glosa'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def cuentaProveedores(self):
		return self._cuentaProveedores
	@cuentaProveedores.setter
	def cuentaProveedores(self, data):
		self._cuentaProveedores = data
		self._listaDeCambio['cuentaProveedores'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def codigoEspecial(self):
		return self._codigoEspecial
	@codigoEspecial.setter
	def codigoEspecial(self, data):
		self._codigoEspecial = data
		self._listaDeCambio['codigoEspecial'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def fechaVencimiento(self):
		return self._fechaVencimiento
	@fechaVencimiento.setter
	def fechaVencimiento(self, data):
		self._fechaVencimiento = data
		self._listaDeCambio['fechaVencimiento'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def contracuenta(self):
		return self._contracuenta
	@contracuenta.setter
	def contracuenta(self, data):
		self._contracuenta = data
		self._listaDeCambio['contracuenta'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def centroResultados(self):
		return self._centroResultados
	@centroResultados.setter
	def centroResultados(self, data):
		self._centroResultados = data
		self._listaDeCambio['centroResultados'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def activoFijo(self):
		return self._activoFijo
	@activoFijo.setter
	def activoFijo(self, data):
		self._activoFijo = data
		self._listaDeCambio['activoFijo'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def sinDerechoaCredito(self):
		return self._sinDerechoaCredito
	@sinDerechoaCredito.setter
	def sinDerechoaCredito(self, data):
		self._sinDerechoaCredito = data
		self._listaDeCambio['sinDerechoaCredito'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def conCreditoFiscal(self):
		return self._conCreditoFiscal
	@conCreditoFiscal.setter
	def conCreditoFiscal(self, data):
		self._conCreditoFiscal = data
		self._listaDeCambio['conCreditoFiscal'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def mImpuestoEspecifico1(self):
		return self._mImpuestoEspecifico1
	@mImpuestoEspecifico1.setter
	def mImpuestoEspecifico1(self, data):
		self._mImpuestoEspecifico1 = data
		self._listaDeCambio['mImpuestoEspecifico1'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def mImpuestoEspecifico2(self):
		return self._mImpuestoEspecifico2
	@mImpuestoEspecifico2.setter
	def mImpuestoEspecifico2(self, data):
		self._mImpuestoEspecifico2 = data
		self._listaDeCambio['mImpuestoEspecifico2'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def impuestoEspecificoFijo(self):
		return self._impuestoEspecificoFijo
	@impuestoEspecificoFijo.setter
	def impuestoEspecificoFijo(self, data):
		self._impuestoEspecificoFijo = data
		self._listaDeCambio['impuestoEspecificoFijo'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def impuestoEspecificoVariable(self):
		return self._impuestoEspecificoVariable
	@impuestoEspecificoVariable.setter
	def impuestoEspecificoVariable(self, data):
		self._impuestoEspecificoVariable = data
		self._listaDeCambio['impuestoEspecificoVariable'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def M3(self):
		return self._M3
	@M3.setter
	def M3(self, data):
		self._M3 = data
		self._listaDeCambio['M3'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoImpuesto2(self):
		return self._montoImpuesto2
	@montoImpuesto2.setter
	def montoImpuesto2(self, data):
		self._montoImpuesto2 = data
		self._listaDeCambio['montoImpuesto2'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def codImpuesto3(self):
		return self._codImpuesto3
	@codImpuesto3.setter
	def codImpuesto3(self, data):
		self._codImpuesto3 = data
		self._listaDeCambio['codImpuesto3'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoImpuesto3(self):
		return self._montoImpuesto3
	@montoImpuesto3.setter
	def montoImpuesto3(self, data):
		self._montoImpuesto3 = data
		self._listaDeCambio['montoImpuesto3'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def contabilizado(self):
		return self._contabilizado
	@contabilizado.setter
	def contabilizado(self, data):
		self._contabilizado = data
		self._listaDeCambio['contabilizado'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def idUsuario(self):
		return self._idUsuario
	@idUsuario.setter
	def idUsuario(self, data):
		self._idUsuario = data
		self._listaDeCambio['idUsuario'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
		
	def __init__(self, venta, sucursal, TiopDocumento, numDocumento, nulo, correlativo, fecha,
	 rutEmisor, nomEmisor, rutReceptor, nomReceptor, montoExento, montoAfecto, montoIVA, montoTotal,
	 Glosa, cuentaProveedores, codigoEspecial, fechaVencimiento, contracuenta, centroResultados,
	 activoFijo, sinDerechoaCredito, conCreditoFiscal, mImpuestoEspecifico1, mImpuestoEspecifico2,
	 impuestoEspecificoFijo, impuestoEspecificoVariable, M3, montoImpuesto2, codImpuesto3, montoImpuesto3,
	 contabilizado, idUsuario):
		self._venta = venta
		self._sucursal = sucursal
		self._TiopDocumento = TiopDocumento
		self._numDocumento = numDocumento
		self._nulo = nulo
		self._correlativo = correlativo
		self._fecha = fecha
		self._rutEmisor = rutEmisor
		self._nomEmisor = nomEmisor
		self._rutReceptor = rutReceptor
		self._nomReceptor = nomReceptor
		self._montoExento = montoExento
		self._montoAfecto = montoAfecto
		self._montoIVA = montoIVA
		self._montoTotal = montoTotal
		self._Glosa = Glosa
		self._cuentaProveedores = cuentaProveedores
		self._codigoEspecial = codigoEspecial
		self._fechaVencimiento = fechaVencimiento
		self._contracuenta = contracuenta
		self._centroResultados = centroResultados
		self._activoFijo = activoFijo
		self._sinDerechoaCredito = sinDerechoaCredito
		self._conCreditoFiscal = conCreditoFiscal
		self._mImpuestoEspecifico1 = mImpuestoEspecifico1
		self._mImpuestoEspecifico2 = mImpuestoEspecifico2
		self._impuestoEspecificoFijo = impuestoEspecificoFijo
		self._impuestoEspecificoVariable = impuestoEspecificoVariable
		self._M3 = M3
		self._montoImpuesto2 = montoImpuesto2
		self._codImpuesto3 = codImpuesto3
		self._montoImpuesto3 = montoImpuesto3
		self._contabilizado = contabilizado
		self._idUsuario = idUsuario
		conexion = sqlite3.connect('prueba.db')
		consulta = conexion.cursor()
		exist = '''
		SELECT COUNT(*) FROM facturas
		WHERE venta = ?, numDocumento = ?, rutEmisor = ?, rutReceptor = ?
		'''
		lista = tuple([venta, numDocumento, rutEmisor, rutReceptor])
		if (consulta.execute(exist, lista)):
			count = consulta.fetchone()
			if count[0] == 0:
				count = consulta.fetchone()
				#self._ident = "rut"
				#self._identValue = rut
				if count[0] == 0:
					#self._listaDeCambio={"rut":(rut, "rut"), "razonSocial":(rs,"text")}
					#self._esNuevo = True
				else:
					#print "no se puede crear porque ya existe el rut en la base de datos"
					#self._listaDeCambio = {}
					#self._esNuevo = False
			else:
				print "no se puede crear porque ya existe el rut en la base de datos"
	

class bitacora(tabla):
	_fecha = None
	_evento = None
	_so = None
	_idUsuario = None
	@property
	def fecha(self):
		return self._fecha
	@property
	def evento(self):
		return self._evento
	@property
	def so(self):
		return self._so
	@property
	def idUsuario(self):
		return self._idUsuario
	@fecha.setter
	def fecha(self, data):
		self._fecha = data
		self._listaDeCambio["fecha"] = (data, "text")
		print "cambio: ",self._listaDeCambio
	@evento.setter
	def evento(self, data):
		self._evento = data
		self._listaDeCambio["evento"] = (data, "text")
		print "cambio: ",self._listaDeCambio
	@so.setter
	def so(self, data):
		self._so = data
		self._listaDeCambio["so"] = (data, "text")
		print "cambio: ",self._listaDeCambio
	@idUsuario.setter
	def idUsuario(self, data):
		self._idUsuario = data
		self._listaDeCambio["idUsuario"] = (data, "text")
		print "cambio: ",self._listaDeCambio
	def __init__(self, fecha, evento, so):
		self._fecha = fecha
		self._evento = evento
		self._so = so
		


def validarTipo(dato, tipo):
	if tipo == "int":
		try:
			if dato != None:
				dato = int(dato)
			else:
				print "el dato fué nulo"
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


		
prueba = empresas("18598138-k", "holi")
prueba.rS="holi"
prueba.save()
