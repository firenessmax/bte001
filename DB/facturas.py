#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re
from table import *
from empresas import *


# esta clase sirve para insertar, updatear y deletear(no esta lista)
# para facturas
# instanciamiento:
# f = facturas(venta, numDocumento, rutReceptor, rutEmisor, sucursal=1, id=0,
#	 TipoDocumento=1, nulo=0, fecha="2015-10-02",
#	 nomEmisor="", nomReceptor="", montoExento=0, montoTotal=0,
#	 Glosa="", cuentaProveedores=0, contracuenta=0, contabilizado=0, idUsuario=0, esNuevo = True)
# f = facturas(venta = 0, numDocumento = 1, rutReceptor = "17920814-8", rutEmisor = "1-9")
# funciones y metodos:
# f.save()
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
		if(self.consulta.execute(ident, tupla)):
			return self.consulta.fetchone()[0]
		
	def __init__(self, venta, numDocumento, rutReceptor, rutEmisor, sucursal=1, id=0,
	 TipoDocumento=1, nulo=0, fecha="2015-10-02",
	 nomEmisor="", nomReceptor="", montoExento=0, montoTotal=0,
	 Glosa="", cuentaProveedores=0, contracuenta=0, contabilizado=0, idUsuario=0, esNuevo = True):
		print "Creando nueva tabla en facturas..."
		
		self._venta = venta
		self._numDocumento = numDocumento
		self._rutReceptor = rutReceptor	
		self._rutEmisor = rutEmisor
		try:
			empresaEmisor = empresas(rutEmisor, nomEmisor)
			empresaEmisor.save()
			print u'Se creo la empresa : ', rutEmisor, ' razonSocial : ', nomEmisor
		except:
			print u'La empresa con el rut : ', rutEmisor, u' ya existe en la base de datos'
		try:
			empresaReceptor = empresas(rutReceptor, nomReceptor)
			empresaReceptor.save()
			print u'Se creo la empresa : ', rutReceptor, ' razonSocial : ', nomReceptor
		except:
			print u'La empresa con el rut : ', rutReceptor, u' ya existe en la base de datos'
		if esNuevo:
			conexion = sqlite3.connect('prueba.db')
			consulta = conexion.cursor()
			exist = '''
			SELECT COUNT(*) FROM facturas
			WHERE venta = ? AND numDocumento = ? AND rutEmisor = ? AND rutReceptor = ?
			'''
			tupla = tuple([venta, numDocumento, rutEmisor, rutReceptor])
			if (consulta.execute(exist, tupla)):
				count = consulta.fetchone()
				self._ident = "id"
				if count[0] == 0:
					self._id = id
					self.fecha = fecha
					#se calcula
					self._listaDeCambio={"venta":(self._venta, "int"),
							"sucursal":(sucursal,"int"),
							"TipoDocumento":(TipoDocumento, "int"),
							"numDocumento":(self._numDocumento, "int"),
							"nulo":(nulo, "int"),
							"correlativo":(self._correlativo, "int"),
							"fecha":(self._fecha, "fecha"),
							"rutEmisor":(self._rutEmisor, "rut"),
							"nomEmisor":(nomEmisor, "text"),
							"rutReceptor":(self._rutReceptor, "rut"),
							"nomReceptor":(nomReceptor, "text"),
							"montoExento":(montoExento, "int"),
							"montoAfecto":(self._montoAfecto, "int"),
							"montoIVA":(self._montoIVA, "int"),
							"montoTotal":(montoTotal, "int"),
							"Glosa":(Glosa, "text"),
							"cuentaProveedores":(cuentaProveedores, "int"),
							"codigoEspecial":(self._codigoEspecial,"text"),
							"fechaVencimiento":(self._fechaVencimiento, "fecha"),
							"contracuenta":(contracuenta, "int"),
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
							"contabilizado":(contabilizado, "int"),
							"idUsuario":(idUsuario, "int")
							}
					self._esNuevo = True
				
				else:
					self._listaDeCambio = {}
					self._esNuevo = False
					raise Exception(u"Ya esxiste esta factura, no debe pistolearla denuevo")
		
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
				self._identValue = self._id
					
				self._listaDeCambio = {}
				self._esNuevo = False
			consulta.close()
			conexion.close()
			
			
prueba = facturas(0,9,"17920814-8","8953221-3", nomEmisor = "Mami", esNuevo = False)
prueba.nomEmisor="mamaita ta ta"
#prueba = facturas(0,9,"19144519-8","17920814-8", nomEmisor = "Rodri", nomReceptor = "cris")
#obtenerVentas(prueba)

prueba.save()