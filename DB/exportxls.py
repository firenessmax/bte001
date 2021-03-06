#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
from facturas import *
from datetime import *
from empresas import *

TITLESC = ["Sucursal", "Tipo de Documento", u"Nº de Documento", "Documento Nulo", "Correlativo", 
			"Fecha", "Rut Nacional", "Rut", "Nombre Proveedor", "", "Monto Exento", "Monto Neto", 
			"Monto Iva", "Monto Total",	"Glosa General de Detalle", "",	"Cuenta de Proveedores", 
			u"Código Especial", "Fecha de Venciemiento", "Contracuenta", "Centro de Resultado", 
			"Glosa de Contracuenta", "Monto de Contracuenta", u"Código especial Contracuenta",
			"Rut Nacional Contracuenta", "Rut de Contracuenta",	"Nombre Rut Contracuenta", 
			"Es Compra de Activo Fijo", "Contracuenta 2", "Centro de Resultado 2",
			"Golsa de Contracuenta 2", "Monto de Contracuenta 2", u"Código Especial 2",
			"Rut Nacional Contracuenta 2", "Rut de Contracuenta 2", "Nombre Rut Contracuenta 2", 
			"Contracuenta 3", "Centro de Resultado 3", "Glosa Contracuenta 3", 
			"Monto de Contracuenta3", u"Código Especial 3", "Rut Nacional Contracuenta 3", 
			"Rut Contracuenta 3", "Nombre Rut Contracuenta 3",
			"Es Compra de Activo Fijo ", u"Documento sin Derecho a Crédito",	
			u"Documento con Crédito Fiscal Proporcional", u"Monto Impuesto Específico Recuperable", u"Monto impuesto Específico no Recuperable",	
			u"Impuesto Específico Fijo", u"Impuesto Específico Variable", "M3",	
			u"Código impuesto 2", "Monto Impuesto 2", u"Código Impuesto 3", "Monto Impuesto 3", 
			u"Código Impuesto 4", "Monto de Impuesto 4", u"Código Impuesto 5", "Monto de Impuesto 5"]

TITLESV = ["Sucursal", "Tipo de Documento", u"Nº de Documento", "Documento Nulo", "", "Fecha", "Rut Nacional",
			"Rut", "", "Nombre Cliente", "Monto Exento", "Monto Neto", "Monto Iva", "Monto Total",	
			"Glosa General de Detalle",	"Cuenta de Clientes", "", "Codigo Especial", "Fecha de Venciemiento",	
			"Contracuenta",	"Centro de Resultado", "Glosa de Contracuenta",	"Monto de Contracuenta", 
			u"Código especial Contracuenta", "Rut Nacional Contracuenta", "Rut de Contracuenta", 
			"Nombre Rut Contracuenta",
			"Contracuenta 2", "Centro de Resultado 2", "Glosa de ContraCuenta 2", "Monto de Contracuenta 2",
			u"Código Especial 2", "Rut Nacional Contracuenta 2", "Rut de Contracuenta 2",
			"Nombre Rut Contracuenta 2", "Contracuenta 3", "Centro de Resultado 3", "Glosa Contracuenta 3",
			"Monto Contracuenta 3", u"Código Especial 3", "Rut Nacional Contracuenta 3",
			"Rut Contracuenta 3", "Nombre Rut Contracuenta 3", u"Impuesto Específico Fijo",
			u"Impiuesto Específico Variable", "M3", u"Código de Impuesto 2",
			"Monto Impuesto 2", "Codigo Impuesto 3", "Monto Impuesto 3", u"Código de Impuesto 4",
			"Monto de Impuesto 4", u"Código de Impuesto 5", "Monto de Impuesto 5"]

def exportarxls(fVentas, fCompras, path = u"", contabilizar = False, guardarContabilizados = False, correlativo = 1, aceptaBoleta = False, codigoEspecial = "", centroResultado = ""): #false, las no contabilizadas, True todas
	print "CORRELATIVO", correlativo
	try:
		libro = xlwt.Workbook(encoding="UTF-8")
	except:
		raise Exception ("No se puede guardar")
	paginaCompra = libro.add_sheet("Compras")
	num = 0
	for i, e in enumerate(TITLESC):
		paginaCompra.row(0).write(i, e)
	for obj in fCompras:
		obj.correlativo = correlativo
		correlativo += 1
		fila = paginaCompra.row(num)
		if guardarContabilizados:
			datos = formatoFacturaXlsCompras(obj, codigoEspecial, centroResultado)
			if aceptaBoleta:#datos[1] != "NA":
				fila = paginaCompra.row(num+1)
				for index, dato in enumerate(datos):
					fila.write(index, dato)
				num += 1
			elif aceptaBoleta == False and datos[1] != "NA":
				fila = paginaCompra.row(num+1)
				for index, dato in enumerate(datos):
					fila.write(index, dato)
				num += 1
		elif not guardarContabilizados and obj.contabilizado == 0:
			datos = formatoFacturaXlsCompras(obj, codigoEspecial, centroResultado)
			if aceptaBoleta:#datos[1] != "NA":
				fila = paginaCompra.row(num+1)
				for index, dato in enumerate(datos):
					fila.write(index, dato)
				num += 1
			elif aceptaBoleta == False and datos[1] != "NA":
				fila = paginaCompra.row(num+1)
				for index, dato in enumerate(datos):
					fila.write(index, dato)
				num += 1
		if contabilizar:
			obj.contabilizado=1
		
		obj.save()
	#hoja = paginaCompra.col(9)
	#hoja.width = 100
	#hoja = paginaCompra.col(16)
	#hoja.width = 100
			
	paginaVenta = libro.add_sheet("Ventas")
	for i, e in enumerate(TITLESV):
		paginaVenta.row(0).write(i, e)
	num = 0
	fila = paginaVenta.row(1)
	for obj in (fVentas):
		fila = paginaVenta.row(num)
		datos = formatoFacturaXlsVentas(obj, codigoEspecial, centroResultado)
		if True:#datos[1] != "NA":
			if guardarContabilizados:
				fila = paginaVenta.row(num+1)
				for index, dato in enumerate(datos):
					fila.write(index, dato)
				num += 1
			elif not guardarContabilizados and obj.contabilizado == 0:
				fila = paginaVenta.row(num+1)
				for index, dato in enumerate(datos):
					fila.write(index, dato)
				num += 1
		if contabilizar:
			obj.contabilizado=1
			obj.save()
	#hoja = paginaVenta.col(4)
	#hoja.width = 100
	#hoja = paginaVenta.col(8)
	#hoja.width = 100
	#hoja = paginaVenta.col(16)
	#hoja.width = 100
	try:
		libro.save(unicode(path))
	except:
		raise Exception ("No se puede guardar")



#
#	funcion que se utiliza para pasar de un objeto factura a una lista
#	con los datos que se necesitan para exportar a .xls en comrpas
#
def formatoFacturaXlsCompras(factura, codigoEspecial, centroResultado):
	#print "llamada a formatear xls de compras"
	datos = []
	datos.append(factura.sucursal)
	datos.append(switch(factura.TipoDocumento, factura.montoExento,factura.empresaReceptor))
	datos.append(factura.numDocumento)
	if factura.nulo == 0: 
		datos.append("N")
	else:
		datos.append("S")
	datos.append(factura.correlativo)
	datos.append(factura.fecha)
	datos.append("S")
	datos.append(factura.empresaEmisor.rut)
	datos.append(factura.empresaEmisor.rS)
	datos.append("")#es espacio en blanco
	datos.append(factura.montoExento)
	datos.append(factura.montoAfecto)
	datos.append(factura.montoIVA)
	datos.append(factura.montoTotal)
	datos.append(factura.Glosa)
	datos.append("")#es espacio en blanco
	datos.append(factura.cuentaProveedores)
	datos.append(codigoEspecial)
	datos.append(factura.fecha)
	datos.append(factura.contracuenta)
	datos.append(centroResultado)
	datos.append(factura.Glosa)
	datos.append(factura.montoAfecto + factura.montoExento)#Monto de contracuenta
	datos.append("")#Codigo especial contracuenta
	datos.append("S")#Rut nacional contracuenta
	datos.append(factura.empresaEmisor.rut)#Rut de contracuenta
	datos.append(factura.empresaEmisor.rS)#Nombre rut contracuenta
	datos.append("")
	datos.append("")#Contracuenta 2
	datos.append("")#Centro de resultado 2
	datos.append("")#Glosa de contracuenta 2
	datos.append("")#Monto de Contracuenta 2
	datos.append("")#Codigo Especial 2
	datos.append("")#Rut Nacional Contracuenta 2
	datos.append("")#Rut de Contracuenta 2
	datos.append("")#Nombre Rut Contracuenta 2
	datos.append("")
	datos.append("")#Contracuenta 3
	datos.append("")#Centro de Resultado 3
	datos.append("")#Glosa Contracuenta 3
	datos.append("")#Monto de Contracuenta3
	datos.append("")#Codigo Especial 3
	datos.append("")#Rut Nacional Contracuenta 3
	datos.append("")#Rut Contracuenta 3
	datos.append("")#Nombre Rut Contracuenta 3
	if factura.activoFijo == 0:
		datos.append("N")
	else:
		datos.append("S")
		
	from datetime import *
	today = datetime.today()
	formato = "%d/%m/%Y" 
	fecha = datetime.strptime(factura.fecha, formato)
	if (today - timedelta((90 + fecha.day))) > fecha:
		datos.append("S")
	else:
		datos.append("N")
	
	if factura.conCreditoFiscal == 0:
		datos.append("N")
	else:
		datos.append("S")
	datos.append("")
	datos.append(0)#Monto impuesto Específico no Recuperable
	datos.append(factura.impuestoEspecificoFijo)
	datos.append(factura.impuestoEspecificoVariable)
	datos.append(factura.M3)
	datos.append(factura.codImpuesto2)
	datos.append(factura.montoImpuesto2)
	datos.append(factura.codImpuesto3)
	datos.append(factura.montoImpuesto3)
	datos.append("")#codigo impuesto 4
	datos.append(0)#monto impuesto 4
	datos.append("")#codigo impuesto 5
	datos.append(0)#monto impuesto 5
	
	return datos

#
#	funcion que se utiliza para pasar de un objeto factura a una lista
#	con los datos que se necesitan para exportar a .xls en ventas
#
def formatoFacturaXlsVentas(factura, codigoEspecial, centroResultado):
	#print "llamada a formatear xls de ventas"
	datos = []
	datos.append(factura.sucursal)
	datos.append(switch(factura.TipoDocumento, factura.montoExento,factura.empresaEmisor))
	datos.append(factura.numDocumento)
	if factura.nulo == 0: 
		datos.append("N")
	else:
		datos.append("S")
	datos.append("")#es espacio en blanco
	datos.append(factura.fecha)
	datos.append("S")
	datos.append(factura.empresaReceptor.rut)
	datos.append("")#es espacio en blanco
	datos.append(factura.empresaReceptor.rS)
	datos.append(factura.montoExento)
	datos.append(factura.montoAfecto)
	datos.append(factura.montoIVA)
	datos.append(factura.montoTotal)
	datos.append(factura.Glosa)
	datos.append(factura.cuentaProveedores)
	datos.append("")#es espacio en blanco
	datos.append(codigoEspecial)
	datos.append(factura.fecha)
	datos.append(factura.contracuenta)
	datos.append(centroResultado)
	datos.append(factura.Glosa)
	datos.append(factura.montoAfecto + factura.montoExento)#Monto de Contracuenta
	datos.append("")#Codigo especial contracuenta
	datos.append("S")#Rut nacional contracuenta
	datos.append(factura.empresaReceptor.rut)#Rut de contracuenta
	datos.append(factura.empresaReceptor.rS)#Nombre rut contracuenta
	datos.append("")#Contracuenta 2
	datos.append("")#Centro de resultado 2
	datos.append("")#Glosa de contracuenta 2
	datos.append("")#Monto de Contracuenta 2
	datos.append("")#Codigo Especial 2
	datos.append("")#Rut Nacional Contracuenta 2
	datos.append("")#Rut de Contracuenta 2
	datos.append("")#Nombre Rut Contracuenta 2
	datos.append("")#Contracuenta 3
	datos.append("")#Centro de Resultado 3
	datos.append("")#Glosa Contracuenta 3
	datos.append("")#Monto de Contracuenta3
	datos.append("")#Codigo Especial 3
	datos.append("")#Rut Nacional Contracuenta 3
	datos.append("")#Rut Contracuenta 3
	datos.append("")#Nombre Rut Contracuenta 3
	datos.append("")
	datos.append("")
	datos.append("")
	datos.append("")
	datos.append("")
	datos.append(0)
	datos.append(0)
	datos.append(factura.impuestoEspecificoFijo)
	datos.append(factura.impuestoEspecificoVariable)
	datos.append(factura.M3)
	datos.append(factura.codImpuesto2)
	datos.append(factura.montoImpuesto2)
	datos.append(factura.codImpuesto3)
	datos.append(factura.montoImpuesto3)
	datos.append("")#codigo impuesto 4
	datos.append(0)#monto impuesto 4
	datos.append("")#codigo impuesto 5
	datos.append(0)#monto impuesto 5
	return datos
	
#
#	Funcion para cambiar el tipo de documento
#	desde un int a un str
#	
def switch(tipoDocumento, montoExento,empresa=None):
	codigos = codigosDocumento(empresa)
	if tipoDocumento == 33:
		if montoExento > 0:return codigos.c33p
		return codigos.c33
	elif tipoDocumento == 34:return codigos.c34
	elif tipoDocumento == 46:
		if montoExento > 0:return codigos.c46p
		return codigos.c46
	elif tipoDocumento == 56:return codigos.c56
	elif tipoDocumento == 61:return codigos.c61
	else:return "NA"


#ob = obtenerCompras("18598138-k")
#for e in ob:
#	print formatoFacturaXls(e)

ventas = obtenerVentas()
print ventas
compras = obtenerCompras()
print compras
exportarxls(ventas, compras, path = "prueba.xls", contabilizar = False, guardarContabilizados = False)
