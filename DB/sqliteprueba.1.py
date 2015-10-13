#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re

conexion = sqlite3.connect('prueba.db')

cursor = conexion.cursor()

print u"La base de datos se abrió correctamente"

cursor.execute(''' CREATE TABLE IF NOT EXISTS facturas (   id INTEGER PRIMARY KEY, venta INTEGER  DEFAULT 0, sucursal INTEGER, TipoDocumento INTEGER, numDocumento INTEGER, nulo INTEGER DEFAULT 0, correlativo INTEGER, fecha TEXT, rutEmisor TEXT, nomEmisor TEXT, rutReceptor TEXT, nomReceptor TEXT, montoExento INTEGER , montoAfecto INTEGER, montoIVA INTEGER, montoTotal INTEGER, Glosa TEXT, cuentaProveedores TEXT, codigoEspecial TEXT, fechaVencimiento TEXT, contracuenta INTEGER, centroResultados TEXT, activoFijo INTEGER DEFAULT 0, sinDerechoaCredito INTEGER DEFAULT 0, conCreditoFiscal INTEGER DEFAULT 0, mImpuestoEspecifico1 INTEGER, mImpuestoEspecifico2 INTEGER, impuestoEspecificoFijo INTEGER, impuestoEspecificoVariable INTEGER, M3 TEXT, CodImpuesto2 TEXT, montoImpuesto2 INTEGER, codImpuesto3 TEXT, montoImpuesto3 INTEGER, contabilizado INTEGER DEFAULT 0, idUsuario INTEGER DEFAULT 0)''')

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
			argumentos = tuple(argumentos)
			print "args : ", argumentos
			
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
		print "cambios : ", self._listaDeCambio
	def getId(self):
		return self._rut
	#@rut.setter
	#def rut(self, data):
	#	self._rut = data
	#	super._dicc["rut"] = (data, "rut")
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
					print "no se puede crear porque ya existe el rut en la base de datos"
					self._listaDeCambio = {}
					self._esNuevo = False
			else:
				print "Error en la conexion con la base de datos"
			consulta.close()
			conexion.close()
		else:
			self._ident = "rut"
			self._identValue = rut
			self._listaDeCambio = {}
			self._esNuevo = False

class facturas(tabla):
	_id = 0
	_venta = 0				# obligatorio cuando se instancia
	_sucursal = 0
	_TipoDocumento = 0
	_numDocumento = 0		# obligatorio cuando se instancia
	_nulo = 0
	_correlativo = 0
	_fecha = ""
	_rutEmisor = ""			# obligatorio cuando se instancia
	_nomEmisor = ""
	_rutReceptor = ""		# obligatorio cuando se instancia
	_nomReceptor = ""
	_montoExento = 0
	_montoAfecto = 0
	_montoIVA = 0
	_montoTotal = 0
	_Glosa = ""
	_cuentaProveedores = ""
	_codigoEspecial = ""
	_fechaVencimiento = ""
	_contracuenta = 0
	_centroResultados = ""
	_activoFijo = 0
	_sinDerechoaCredito = 0
	_conCreditoFiscal = 0
	_mImpuestoEspecifico1 = 0
	_mImpuestoEspecifico2 = 0
	_impuestoEspecificoFijo = 0
	_impuestoEspecificoVariable = 0
	_M3 = ""
	_codImpuesto2 = ""
	_montoImpuesto2 = 0
	_codImpuesto3 = ""
	_montoImpuesto3 = 0
	_contabilizado = 0
	_idUsuario = 0
	@property
	def id(self):
		return self._id
	@property
	def venta(self):
		return self._venta
	@property
	def sucursal(self):
		return self._sucursal
	@sucursal.setter
	def sucursal(self, data):
		self._sucursal = data
		self._listaDeCambio['sucursal'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def TipoDocumento(self):
		return self._TipoDocumento
	@TipoDocumento.setter
	def TipoDocumento(self, data):
		self._TipoDocumento = data
		self._listaDeCambio['TipoDocumento'] = (data, 'int')
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
		self._listaDeCambio['nulo'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def correlativo(self):
		return self._correlativo
	@correlativo.setter
	def correlativo(self, data):
		self._correlativo = data
		self._listaDeCambio['correlativo'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def fecha(self):
		formato1 = "%Y-%m-%d" # aaaa-mm-dd
		formato2 = "%d/%m/%Y" # dd/mm/aaaa
		
		fecha = datetime.strptime(self._fecha, formato1)
		print "fehca : ", fecha
		fechaFromateada = fecha.strftime(formato2)
		print "fechaFromateada : ", fechaFromateada
		
		self.fechaVencimiento = (fecha + timedelta(days=30)).strftime(formato1)
		return fechaFromateada
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
		afecto = (self._montoTotal - data)/1.19
		self.montoAfecto=(int(round(afecto, 2)))
		self.montoIVA=(int(round(self._montoAfecto*.19)))
		self._listaDeCambio['montoExento'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoAfecto(self):
		return self._montoAfecto
	@montoAfecto.setter
	def montoAfecto(self, data):
		self._montoAfecto = data
		self._listaDeCambio['montoAfecto'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoIVA(self):
		return self._montoIVA
	@montoIVA.setter
	def montoIVA(self, data):
		self._montoIVA = data
		self._listaDeCambio['montoIVA'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoTotal(self):
		return self._montoTotal
	@montoTotal.setter
	def montoTotal(self, data):
		self._montoTotal = data
		afecto = (data - self._montoExento)/1.19
		self.montoAfecto=(int(round(afecto, 2)))
		self.montoIVA=(int(round(self._montoAfecto*.19)))
		self._listaDeCambio['montoTotal'] = (data, 'int')
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
		formato1 = "%Y-%m-%d" # aaaa-mm-dd
		formato2 = "%d/%m/%Y" # dd/mm/aaaa
		
		fecha = datetime.strptime(self._fecha, formato1)
		print "fehcaVencimiento : ", fecha
		fechaFromateada = fecha.strftime(formato2)
		print "fechaVencimientoFromateada : ", fechaFromateada
		
		return self._fechaVencimiento
	@fechaVencimiento.setter
	def fechaVencimiento(self, data):
		self._fechaVencimiento = data
		self._listaDeCambio['fechaVencimiento'] = (data, 'fecha')
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
		self._listaDeCambio['activoFijo'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def sinDerechoaCredito(self):
		return self._sinDerechoaCredito
	@sinDerechoaCredito.setter
	def sinDerechoaCredito(self, data):
		self._sinDerechoaCredito = data
		self._listaDeCambio['sinDerechoaCredito'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def conCreditoFiscal(self):
		return self._conCreditoFiscal
	@conCreditoFiscal.setter
	def conCreditoFiscal(self, data):
		self._conCreditoFiscal = data
		self._listaDeCambio['conCreditoFiscal'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def mImpuestoEspecifico1(self):
		return self._mImpuestoEspecifico1
	@mImpuestoEspecifico1.setter
	def mImpuestoEspecifico1(self, data):
		self._mImpuestoEspecifico1 = data
		self._listaDeCambio['mImpuestoEspecifico1'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def mImpuestoEspecifico2(self):
		return self._mImpuestoEspecifico2
	@mImpuestoEspecifico2.setter
	def mImpuestoEspecifico2(self, data):
		self._mImpuestoEspecifico2 = data
		self._listaDeCambio['mImpuestoEspecifico2'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def impuestoEspecificoFijo(self):
		return self._impuestoEspecificoFijo
	@impuestoEspecificoFijo.setter
	def impuestoEspecificoFijo(self, data):
		self._impuestoEspecificoFijo = data
		self._listaDeCambio['impuestoEspecificoFijo'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def impuestoEspecificoVariable(self):
		return self._impuestoEspecificoVariable
	@impuestoEspecificoVariable.setter
	def impuestoEspecificoVariable(self, data):
		self._impuestoEspecificoVariable = data
		self._listaDeCambio['impuestoEspecificoVariable'] = (data, 'int')
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
	def codImpuesto2(self):
		return self._codImpuesto2
	@codImpuesto2.setter
	def codImpuesto2(self, data):
		self._codImpuesto2 = data
		self._listaDeCambio['codImpuesto2'] = (data, 'text')
		print 'cambio: ',self._listaDeCambio
	@property
	def montoImpuesto2(self):
		return self._montoImpuesto2
	@montoImpuesto2.setter
	def montoImpuesto2(self, data):
		self._montoImpuesto2 = data
		self._listaDeCambio['montoImpuesto2'] = (data, 'int')
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
		self._listaDeCambio['montoImpuesto3'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def contabilizado(self):
		return self._contabilizado
	@contabilizado.setter
	def contabilizado(self, data):
		self._contabilizado = data
		self._listaDeCambio['contabilizado'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	@property
	def idUsuario(self):
		return self._idUsuario
	@idUsuario.setter
	def idUsuario(self, data):
		self._idUsuario = data
		self._listaDeCambio['idUsuario'] = (data, 'int')
		print 'cambio: ',self._listaDeCambio
	
	def getId(self):
		ident = "SELECT id FROM facturas WHERE venta = ? AND numDocumento = ? AND rutEmisor = ?"
		tupla = (self._venta, self._numDocumento, self._rutEmisor)
		if(super.consulta.execute(ident, lista)):
			return super.consulta.fetchone()[0]
		
	def __init__(self, venta, numDocumento, rutReceptor, rutEmisor, sucursal=1, id=0,
	 TipoDocumento=1, nulo=0, fecha="2015-10-02",
	 nomEmisor="", nomReceptor="", montoExento=0, montoTotal=0,
	 Glosa="", cuentaProveedores=0, contracuenta=0, contabilizado=0, idUsuario=0, esNuevo = True):
		print "Creando nueva tabla en facturas..."
		
		self._venta = venta
		self._numDocumento = numDocumento
		self._rutReceptor = rutReceptor	
		self._rutEmisor = rutEmisor
		if esNuevo:
			conexion = sqlite3.connect('prueba.db')
			consulta = conexion.cursor()
			exist = '''
			SELECT COUNT(*) FROM facturas
			WHERE venta = ? AND numDocumento = ? AND rutEmisor = ?
			'''
			lista = tuple([venta, numDocumento, rutEmisor])
			if (consulta.execute(exist, lista)):
				count = consulta.fetchone()
				self._ident = "id"
				if count[0] == 0:
					self._sucursal = sucursal
					self._id = id
					self._TipoDocumento = TipoDocumento
					self._nulo = nulo
					self._fecha = fecha
					self._nomEmisor = nomEmisor
					self._nomReceptor = nomReceptor
					self.montoExento = montoExento	#setter
					self.montoTotal = montoTotal  	#setter
					self._Glosa = Glosa
					#revisar se llama solo cuenta, puede ser cliente o proveedores
					self._cuentaProveedores = cuentaProveedores
					#se calcula
					self._fechaVencimiento = fecha
					self._contracuenta = contracuenta
					self._contabilizado = contabilizado
					self._idUsuario = idUsuario
					self._listaDeCambio={"venta":(self._venta, "int"),
							"sucursal":(self._sucursal,"int"),
							"TipoDocumento":(self._TipoDocumento, "int"),
							"numDocumento":(self._numDocumento, "int"),
							"nulo":(self._nulo, "int"),
							"correlativo":(self._correlativo, "int"),
							"fecha":(self._fecha, "fecha"),
							"rutEmisor":(self._rutEmisor, "rut"),
							"nomEmisor":(self._nomEmisor, "text"),
							"rutReceptor":(self._rutReceptor, "rut"),
							"nomReceptor":(self._nomReceptor, "text"),
							"montoExento":(self._montoExento, "int"),
							"montoAfecto":(self._montoAfecto, "int"),
							"montoIVA":(self._montoIVA, "int"),
							"montoTotal":(self._montoTotal, "int"),
							"Glosa":(self._Glosa, "text"),
							"cuentaProveedores":(self._cuentaProveedores, "int"),
							"codigoEspecial":(self._codigoEspecial,"text"),
							"fechaVencimiento":(self._fechaVencimiento, "fecha"),
							"contracuenta":(self._contracuenta, "int"),
							"centroResultados":(self._centroResultados, "text"),
							"activoFijo":(self._activoFijo, "int"),
							"sinDerechoaCredito":(self._sinDerechoaCredito, "int"),
							"conCreditoFiscal":(self._conCreditoFiscal, "int"),
							"mImpuestoEspecifico1":(self._mImpuestoEspecifico1, "int"),
							"mImpuestoEspecifico2":(self._mImpuestoEspecifico2, "int"),
							"impuestoEspecificoFijo":(self._impuestoEspecificoFijo, "int"),
							"impuestoEspecificoVariable":(self._impuestoEspecificoVariable, "int"),
							"M3":(self._M3, "text"),
							"codImpuesto2":(self._codImpuesto2, "text"),
							"montoImpuesto2":(self._montoImpuesto2, "int"),
							"codImpuesto3":(self._codImpuesto3, "text"),
							"montoImpuesto3":(self._montoImpuesto3, "int"),
							"contabilizado":(self._contabilizado, "int"),
							"idUsuario":(self._idUsuario, "int")
							}
					self._esNuevo = True
				else:
					raise Exception(u"xuala")
					print "no se puede crear porque esta factura ya existe en la base de atos"
					print "Datos de la factura existente (venta, numCuenta, rutEmisor): ", lista
					self._listaDeCambio = {}
					self._esNuevo = False
		
			consulta.close()
			conexion.close()
		else:
			conexion = sqlite3.connect('prueba.db')
			consulta = conexion.cursor()
			sql = "SELECT * FROM facturas WHERE venta = ? AND numDocumento = ? AND rutEmisor = ?"
			tupla = (venta, numDocumento, rutEmisor)
			if (consulta.execute(sql, tupla)):
				row = consulta.fetchone()
				print row
				self._id = row[0]
				self._venta = row[1]
				self._sucursal = row[2]
				self._TipoDocumento = row[3]
				self._numDocumento = row[4]
				self._nulo = row[5]
				self._correlativo = row[6]
				self._fecha = row[7]
				self._rutEmisor =row[8] 
				self._nomEmisor =row[9] 
				self._rutReceptor =row[10]
				self._nomReceptor =row[11]
				self._montoExento =row[12] 
				self._montoAfecto =row[13]
				self._montoIVA =row[14]
				self._montoTotal =row[15]
				self._Glosa =row[16]
				self._cuentaProveedores =row[17] 
				self._codigoEspecial =row[18] 
				self._fechaVencimiento = row[19] 
				self._contracuenta =row[20]
				self._centroResultados =row[21] 
				self._activoFijo =row[22] 
				self._sinDerechoaCredito =row[23]
				self._conCreditoFiscal =row[24]
				self._mImpuestoEspecifico1 =row[25]
				self._mImpuestoEspecifico2 =row[26] 
				self._impuestoEspecificoFijo =row[27] 
				self._impuestoEspecificoVariable =row[28] 
				self._M3 =row[29] 
				self._codImpuesto2 =row[30] 
				self._montoImpuesto2 =row[31]
				self._codImpuesto3 =row[32]
				self._montoImpuesto3 =row[33]
				self._contabilizado =row[34] 
				self._idUsuario =row[35] 
			
				self._ident = "id"
				self._identVale = self._id
					
				self._listaDeCambio = {}
				self._esNuevo = False
			consulta.close()
			conexion.close()
			
			
	

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

def obtenerCompras(empresa):
	conexion = sqlite3.connect('prueba.db')
	consulta = conexion.cursor()
	listaFacturas=[]
	#consulta sql donde rutReceptor
	for row in consulta.execute("SELECT * FROM facturas WHERE rutReceptor = ?", (empresa.rut,)):
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
	
	

def obtenerVentas(empresa):
	conexion = sqlite3.connect('prueba.db')
	consulta = conexion.cursor()
	listaFacturas=[]
	#consulta sql donde rutEmisor
	for row in consulta.execute("SELECT * FROM facturas WHERE rutEmisor = ?", (empresa.rut,)):
		listaFacturas.append(facturas(venta = row[1], numDocumento = row[4], rutReceptor = row[10],
										rutEmisor = row[8], esNuevo = False))
	#f = factura(..., evNuevo = False)-> lista de facturas
	consulta.close()
	conexion.close()
	
	
	

prueba = empresas("17920814-8","mi mami")
obtenerVentas(prueba)
#prueba.rS=u"la empresa del Cristián"		
#prueba = facturas(venta = 0, numDocumento = 8,rutEmisor = "17849210-1", rutReceptor = "8953221-3", esNuevo = False)
#prueba.fecha="2015-12-17"
#prueba.Glosa="aqui va la glosa"
#prueba.nomEmisor=u"Cristián"
#prueba.montoTotal=200000
prueba.save()
	