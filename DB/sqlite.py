#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('prueba.db')

cursor = con.cursor()

print u"La base de datos se abrió correctamente"

cursor.execute(''' CREATE TABLE IF NOT EXISTS facturas (   venta INTEGER  DEFAULT 0, sucursal INTEGER, TipoDocumento INTEGER, numDocumento INTEGER, nulo INTEGER DEFAULT 0, correlativo INTEGER, fecha TEXT, rutEmisor TEXT, nomEmisor TEXT, rutReceptor TEXT, nomReceptor TEXT, montoExento INTEGER , montoAfecto INTEGER, montoIVA INTEGER, montoTotal INTEGER, Glosa TEXT, cuentaProveedores TEXT, codigoEspecial TEXT, fechaVencimiento TEXT, contracuenta INTEGER, centroResultados TEXT, activoFijo INTEGER DEFAULT 0, sinDerechoaCredito INTEGER DEFAULT 0, conCreditoFiscal INTEGER DEFAULT 0, mImpuestoEspecifico1 INTEGER, mImpuestoEspecifico2 INTEGER, impuestoEspecificoFijo INTEGER, impuestoEspecificoVariable INTEGER, M3 TEXT, CodImpuesto2 TEXT, montoImpuesto2 INTEGER, codImpuesto3 TEXT, montoImpuesto3 INTEGER, contabilizado INTEGER DEFAULT 0, idUsuario INTEGER DEFAULT 0)''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS usuario ( id INTEGER PRIMARY KEY, username TEXT, pass TEXT, activo INTEGER DEFAULT 1)  ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS empresas ( rut TEXT, razonSocial TEXT) ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS bitacora ( id INTEGER PRIMARY KEY, fecha TEXT,tipo INTEGER, evento TEXT, so TEXT, idUsuario INTEGER DEFAULT 0) ''')

#cursor.execute("INSERT INTO usuario (username, pass) VALUES ('cristian', '1234')")
#cursor.execute("INSERT INTO usuario (username, pass) VALUES ('nestor', 'ewerqwef')")
#con.commit()
con.close()

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
		print lista
		lista = tuple(lista)
		print lista
		if (consulta.execute(exist, tuple(lista))):
			count = consulta.fetchone()
			print "count :", count
			if count[0] == 0:
				sql = ''' 
				INSERT INTO empresas(rut, razonSocial)
				VALUES (?,?)
				'''
				self.insertar([(rut, "rut"),(rs, "text")], sql)
			else:
				print "no se puede crear porque ya existe el rut en la base de datos"
class bitacora(tabla):
	print "holi"
	


# Faltan agregar carias restriccione
# ejemplos: la del rut		
		
def validarTipo(dato, tipo):
	if tipo == "int":
		try:
			dato = int(dato)
		except ValueError:
			print (dato, " no es entero")
			return False
	elif tipo == "float":
		try:
			dato = float(dato) or int(dato)
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
				print (dato[1], " : el digito verificador no puede ser distinto de k ni mayot que 9 o menor que 0")
				return False
			if not validarTipo(dato[0], "int"):
				print (dato[0], " : no puede introducir carteres que no sean numéricos")
				return False
			verificador = (range(10) + ['k'])[
				11 - sum(
					[int(digit) * factor
					for digit, factor in zip(dato[0][::-1], 2 * range(2,8))]
				) % 11
			]
			if not verificador == int(dato[1]):
				print type(verificador)," vs ", type(dato[1])
				print (dato, " el rut no es correcto")
				return False
		except ValueError:
			print (dato, " no respeta el formato de rut o no es correcto")
			return False
			
	return True
		


var = empresas("17920814-8", "entero pollo lo oe zii")





