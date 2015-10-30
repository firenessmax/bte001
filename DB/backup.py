#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os.path
from tableCreate import *
import sys

dir_path = '%s\\CAMDE\\' %  os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

PATH = '%sdump.sql' % dir_path.decode('latin_1')

def verificacionBackup(path):
	archivo = open(path,'r')
	lineas = archivo.readlines()
	texto = ""
	for linea in lineas:
		texto += linea
	find1 = texto.find('''CREATE TABLE bitacora(id INTEGER PRIMARY KEY, 
								fecha TEXT,
								tipo INTEGER, 
								evento TEXT, 
								so TEXT, 
								idUsuario INTEGER DEFAULT 0
								);''')
	bitacora = "CREATE TABLE bitacora"
	if find1 == -1: raise Excecute("No tiene el formato de Base de Datos correcto, le falta la entidad bitacora")
	texto = texto[:find1] +texto[len(bitacora) + len(texto[:find1]):]
	find2 = texto.find('''CREATE TABLE empresas(id INTEGER PRIMARY KEY,
								rut TEXT, 
								razonSocial TEXT
								);''')
	empresas = "CREATE TABLE empresas"
	if find2 == -1: raise Excecute("No tiene el formato de Base de Datos correcto, le falta la entidad empresas")
	texto = texto[:find2] +texto[len(empresas) + len(texto[:find2]):]
	find3 = texto.find('''CREATE TABLE facturas(id INTEGER PRIMARY KEY,
	 							venta INTEGER  DEFAULT 0,
								sucursal INTEGER, 
								TipoDocumento INTEGER, 
								numDocumento INTEGER, 
								nulo INTEGER DEFAULT 0, 
								correlativo INTEGER, 
								fecha TEXT, 
								idEmisor INTEGER,
								
								idReceptor INTEGER,
								montoExento INTEGER, 
								montoAfecto INTEGER, 
								montoIVA INTEGER, 
								montoTotal INTEGER, 
								Glosa TEXT, 
								cuentaProveedores TEXT, 
								codigoEspecial TEXT, 
								fechaVencimiento TEXT, 
								contracuenta INTEGER, 
								centroResultados TEXT, 
								activoFijo INTEGER DEFAULT 0, 
								sinDerechoaCredito INTEGER DEFAULT 0, 
								conCreditoFiscal INTEGER DEFAULT 0, 
								mImpuestoEspecifico1 INTEGER, 
								mImpuestoEspecifico2 INTEGER, 
								impuestoEspecificoFijo INTEGER, 
								impuestoEspecificoVariable INTEGER, 
								M3 TEXT, 
								CodImpuesto2 TEXT, 
								montoImpuesto2 INTEGER, 
								codImpuesto3 TEXT, 
								montoImpuesto3 INTEGER, 
								contabilizado INTEGER DEFAULT 0, 
								idUsuario INTEGER DEFAULT 0,
								FOREIGN KEY(idEmisor) REFERENCES empresas(id),
								FOREIGN KEY(idReceptor) REFERENCES empresas(id)
								);''');
	facturas = "CREATE TABLE facturas"
	if find3 == -1: raise Excecute("No tiene el formato de Base de Datos correcto, le falta la entidad facturas")
	texto = texto[:find3] +texto[len(facturas) + len(texto[:find3]):]
	find4 = texto.find('''CREATE TABLE usuario(id INTEGER PRIMARY KEY, 
								username TEXT, 
								pass TEXT, 
								activo INTEGER DEFAULT 1
								);''');
	usuario = "CREATE TABLE usuario"
	if find4 == -1: raise Excecute("No tiene el formato de Base de Datos correcto, le falta la entidad usuario")
	texto = texto[:find4] +texto[len(usuario) + len(texto[:find4]):]
	if texto.find("CREATE TABLE") != -1: raise Excecute(u"No tiene el formato de Base de Datos correcto, posee más entidades de lo correcto")
	archivo.close()


def dump_to_file(nombre = PATH):
	conexion = sqlite3.connect(DB)
	with open(nombre, 'w') as f:
		for line in conexion.iterdump():
			f.write('%s\n' % line)
	conexion.close()


def restore_db( db_file = DB, nombre = PATH):
	conexion = sqlite3.connect(db_file)
	cursor = conexion.cursor()
	cursor.execute('drop table if exists facturas')
	cursor.execute('drop table if exists empresas')
	cursor.execute('drop table if exists bitacora')
	cursor.execute('drop table if exists usuario')
	conexion.commit()
	with open(nombre, 'r') as f:
		sql = f.read()
	conexion.executescript(sql)
	conexion.commit()
	conexion.close()


#verificacionBackup(PATH)
#dump_to_file()
#restore_db()