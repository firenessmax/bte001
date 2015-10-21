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


fact = obtenerCompras("17920814-8")[0]
print facturaToDicCompras(fact)