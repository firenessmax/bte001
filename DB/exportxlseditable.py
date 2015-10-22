#!/usr/bin/env python
# -*- coding: utf-8 -*-

from facturas import *
from exportxls import *


def facturaToDicCompras(factura):
	dic = {}
	datos = formatoFacturaXlsCompras(factura)
	for i, title in enumerate(TITLESC):
		dic[unicode(title)] = datos[i]
	return dic
		
def agregarHoja(libro, nombre):
	hoja = libro.add_sheet(nombre)
	
class exportXls():
	_paginas = []
	_nombre = ""
	
	@property
	def paginas(self):
		return self._paginas
	@paginas.setter
	def paginas(self, dato):
		self._paginas = dato
	@property
	def nombre(self):
		return self._nombre
	@nombre.setter
	def nombre(self, dato):
		self._nombre = dato
	
	def __init__(self, paginas = [], nombre = ""):
		self._paginas = paginas
		self._nombre = nombre

class pagina():
	_nombre = ""
	_datos = []
	
	@property
	def nombre(self):
		return self._nombre
	@nombre.setter
	def nombre(self, dato):
		self._nombre = dato
	@property
	def datos(self):
		return self._datos
	@datos.setter
	def datos(self, dato):
		self._datos = dato
	
	def __init__(self, nombre = "", datos = []):
		self._nombre = nombre
		self._datos = datos
	
class campo():
	_contenido = ""
	_estilo = ""
	_row = 0
	_columna = 0
	
	@property
	def contenido(self):
		return self._contenido
	@contenido.setter
	def contenido(self, dato):
		self._contenido = dato
	@property
	def estilo(self):
		return self._estilo
	@estilo.setter
	def estilo(self, dato):
		self._estilo = estilo
	@property
	def row(self):
		return self._row
	@row.setter
	def row(self, dato):
		self._row = dato
	@property
	def columna(self):
		return self._columna
	@columna.setter
	def columna(self, dato):
		self._columna = dato
	
	def __init__(self, contenido = "", estilo = "", row = 0, columna = 0):
		self._contenido = contenido
		self._estilo = estilo
		self._row = row
		self._columna = columna


fact = obtenerCompras("17920814-8")[0]
print facturaToDicCompras(fact)