#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os

dir_path = '%s\\CAMDE\\' %  os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

DB = '%sprueba.db' % dir_path

def iniciarDB():
	print "PATH",DB
	conexion = sqlite3.connect(DB)
	cursor = conexion.cursor()
	#print u"La base de datos se abrió correctamente"
	
	cursor.execute(''' CREATE TABLE IF NOT EXISTS facturas(id INTEGER PRIMARY KEY,
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
								)''')
	
	cursor.execute(''' CREATE TABLE IF NOT EXISTS usuario(id INTEGER PRIMARY KEY, 
								username TEXT, 
								pass TEXT, 
								activo INTEGER DEFAULT 1
								)''')
	
	cursor.execute(''' CREATE TABLE IF NOT EXISTS empresas(id INTEGER PRIMARY KEY,
								rut TEXT, 
								razonSocial TEXT
								)''')
	
	cursor.execute(''' CREATE TABLE IF NOT EXISTS bitacora(id INTEGER PRIMARY KEY, 
								fecha TEXT,
								tipo INTEGER, 
								evento TEXT, 
								so TEXT, 
								idUsuario INTEGER DEFAULT 0
								) ''')
	
	conexion.close()

iniciarDB()