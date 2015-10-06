#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

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

#
#		sql = ''' 
#		INSERT INTO empresas(rut, razonSocial)
#		VALUES (?,?)
#		'''

#		sql = ''' 
#		INSERT INTO empresas(fecha, tipo, evento. so, idUsuario)
#		VALUES (?,?,?,?,?)
#		'''

class tabla:
	def insertar(self, datos, sql):
		argumentos = []
		for dato in datos:
			if validarTipo(dato[0], dato[1]):
				argumentos.append(dato[0])
			else:
				print ("error al escribir ", dato)
				#aqui pondría un rollback
				exit()
		
		conexion = sqlite3.connect('prueba.db')
		consulta = conexion.cursor()
		
		argumentos = tuple(argumentos)
		
		if (consulta.execute(sql, argumentos)):
			print("registro guardado con exito")
		else: ("ha ocurrido un problema al guardar el registro")
		consulta.close()
		conexion.commit()
		conexion.close()


class empresas(tabla):
	def __init__(self, rut, rs):
		conexion = sqlite3.connect('prueba.db')
		consulta = conexion.cursor()
		exist = '''
		SELECT COUNT(*) FROM empresas
		WHERE rut LIKE (?)
		'''
		lista = []
		lista.append(rut)
		lista = tuple(lista)
		if (consulta.execute(exist, tuple(lista))):
			count = consulta.fetchone()
			if count[0] == 0:
				sql = ''' 
				INSERT INTO empresas(rut, razonSocial)
				VALUES (?,?)
				'''
				self.insertar([(rut, "rut"),(rs, "text")], sql)
				conexion.commit()
			else:
				print "no se puede crear porque ya existe el rut en la base de datos"
		else:
			print "No se pudo guardar en la base de datos"
		consulta.close()
		conexion.close()
		
		
		
class bitacora(tabla):
	def __init__(self, fecha, tipo, evento, so, idUsuario):
		conexion = sqlite3.connect('prueba.db')
		consulta = conexion.cursor()
		sql = ''' 
		INSERT INTO bitacora(fecha, tipo, evento, so, idUsuario)
		VALUES (?,?,?,?,?)
		'''
		self.insertar([(fecha,"text"),(tipo,"text"),(evento,"text"),(so,"text"),(idUsuario,"int")],sql)
		consulta.close()
		conexion.commit()
		conexion.close()
		
		
class facturas(tabla):
	def __init__(self, venta, sucursal, TiopDocumento, numDocumento, nulo, correlativo, fecha,
	 rutEmisor, nomEmisor, rutReceptor, nomReceptor, montoExento, montoAfecto, montoIVA, montoTotal,
	 Glosa, cuentaProveedores, codigoEspecial, fechaVencimiento, contracuenta, centroResultados,
	 activoFijo, sinDerechoaCredito, conCreditoFiscal, mImpuestoEspecifico1, mImpuestoEspecifico2,
	 impuestoEspecificoFijo, impuestoEspecificoVariable, M3, montoImpuesto2, codImpuesto3, montoImpuesto3,
	 contabilizado, idUsuario):
		print "numDocumento, rutEmisor"
		

# Faltan agregar varias restricciones
# ejemplos: la del rut		
		
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
		try:
			dato = dato.split("-")
			if not len(dato) == 2:
				print "debe escribir el rut con este formato 17920814-8"
				return False
			if not (dato[1] == "k" or (int(dato[1])<10 and int(dato[1])>0)):
				print (dato[1], " : el digito verificador no puede ser distinto de k ni mayor que 9 o menor que 0")
				return False
			if not validarTipo(dato[0], "int"):
				print (dato[0], " : no puede introducir carteres que no sean numericos")
				return False
			verificador = (range(10) + ['k'])[
				11 - sum(
					[int(digit) * factor
					for digit, factor in zip(dato[0][::-1], 2 * range(2,8))]
				) % 11
			]
			if not verificador == int(dato[1]):
				print (dato, " el rut no es correcto")
				return False
		except ValueError:
			print (dato, " no respeta el formato de rut o no es correcto")
			return False
			
	return True
		


#var = empresas("17966491-7", "la vane")	
bitacora = bitacora("27/12/1991","tipo1","evento","so?nose que es",None)




