#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os.path
from tableCreate import *

def dump_to_file(nombre = 'dump.sql'):
	conexion = sqlite3.connect(DB)
	with open(nombre, 'w') as f:
		for line in conexion.iterdump():
			f.write('%s\n' % line)
	conexion.close()


def restore_db( db_file = DB, nombre = 'dump.sql'):
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

#dump_to_file()
restore_db()