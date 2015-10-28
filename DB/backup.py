#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os.path

def dump_to_file(nombre = 'dump.sql'):
	conexion = sqlite3.connect('prueba.db')
	with open(nombre, 'w') as f:
		for line in conexion.iterdump():
			f.write('%s\n' % line)


def restore_db( db_file = 'prueba.db', nombre = 'dump.sql'):
	conexion = sqlite3.connect(db_file)
	with open(nombre, 'r') as f:
		sql = f.read()
	conexion.executescript(sql)
	conexion.commit()
	conexion.close()
	
restore_db()