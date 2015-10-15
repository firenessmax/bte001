#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
from facturas import *
TITLES = ["Sucursal", "Tipo de Documento", u"Nº  de Documento", "Documento Nulo", "Correlativo	Fecha", "Rut Nacional",
			"Rut", "Nombre Proveedor", "Nombre Cliente", "Monto Exento", "Monto Neto", "Monto Iva", "Monto Total",	
			"Glosa General de Detalle",	"Cuenta de Proveedores", "Codigo Especial",	"Fecha de Venciemiento",	
			"Contracuenta",	"Centro de Resultado", "Glosa de Contracuenta",	"Monto de Contracuenta", "Codigo especial Contracuenta",	
			"Rut Nacional Contracuenta", "Rut de Contracuenta",	"Nombre Rut Contracuenta", "Es Compra de Activo Fijo ",	
			"Documento sin Derecho a Credito",	"Documento con Credito Fiscal",	"Monto impuesto Especifico",	
			"Monto Impuesto Especifico", "Impuesto Especifico Fijo", "Impuesto Especifico Variable", "M3",	
			"Codigo impuesto 2", "Monto Impuesto 2", "Codigo Impuesto 3", "Monto Impuesto 3"]


def exportarxls(fVentas, fCompras, path = "", contabilizar = False, guardarContabilizados = False, correlativo = 0): #false, las no contabilizadas, True todas
	libro = xlwt.Workbook()
	paginaVenta = libro.add_sheet("Ventas")
	for i, e in enumerate(TITLES):
		paginaVenta.row(0).write(i, e)
	for num, obj in enumerate(fVentas):
		fila = paginaVenta.row(num+1)
		datos = formatoFacturaXls(obj)
		if guardarContabilizados:
			for index, dato in enumerate(datos):
				fila.write(index, dato)
		elif not guardarContabilizados and obj.contabilizado == 0:
			for index, dato in enumerate(datos):
				fila.write(index, dato)
		if contabilizar:
			obj.contabilizado=1
			obj.save()
		
	paginaCompra = libro.add_sheet("Compras")
	for i, e in enumerate(TITLES):
		paginaCompra.row(0).write(i, e)
	for num, obj in enumerate(fCompras):
		fila = paginaCompra.row(num+1)
		if guardarContabilizados:
			obj.correlativo = correlativo
			obj.save()
			datos = formatoFacturaXls(obj)
			for index, dato in enumerate(datos):
				fila.write(index, dato)
			correlativo+=1
		elif not guardarContabilizados and obj.contabilizado == 0:
			obj.correlativo = correlativo
			obj.save()
			datos = formatoFacturaXls(obj)
			for index, dato in enumerate(datos):
				fila.write(index, dato)
			correlativo+=1
		if contabilizar:
			obj.contabilizado=1
			obj.save()
	libro.save(path)


def formatoFacturaXls(factura):
	print "llamada a formatear xls"
	datos = []
	datos.append(factura.sucursal)
	datos.append(factura.TipoDocumento)
	datos.append(factura.numDocumento)
	if factura.nulo == 0: 
		datos.append("N")
	else:
		datos.append("S")
	datos.append(factura.correlativo)
	datos.append(factura.fecha)
	datos.append("S")
	if factura.venta == 0:#compra
		datos.append(factura.empresaEmisor.rut)
	else:#venta
		datos.append(factura.empresaReceptor.rut)
	datos.append(factura.empresaEmisor.rS)
	datos.append(factura.empresaReceptor.rS)
	datos.append(factura.montoExento)
	datos.append(factura.montoAfecto)
	datos.append(factura.montoIVA)
	datos.append(factura.montoTotal)
	datos.append(factura.Glosa)
	datos.append(factura.cuentaProveedores)
	datos.append(factura.codigoEspecial)
	datos.append(factura.fechaVencimiento)
	datos.append(factura.contracuenta)
	datos.append(factura.centroResultados)
	datos.append(factura.Glosa)
	datos.append(factura.montoAfecto + factura.montoExento)
	datos.append("")
	datos.append("")
	datos.append("")
	datos.append("")
	if factura.activoFijo == 0:
		datos.append("N")
	else:
		datos.append("S")
	if factura.sinDerechoaCredito == 0:
		datos.append("N")
	else:
		datos.append("S")
	if factura.conCreditoFiscal == 0:
		datos.append("N")
	else:
		datos.append("S")
	datos.append(factura.mImpuestoEspecifico1)
	datos.append(factura.mImpuestoEspecifico2)
	datos.append(factura.impuestoEspecificoFijo)
	datos.append(factura.impuestoEspecificoVariable)
	datos.append(factura.M3)
	datos.append(factura.codImpuesto2)
	datos.append(factura.montoImpuesto2)
	datos.append(factura.codImpuesto3)
	datos.append(factura.montoImpuesto3)
	return datos
	
#ob = obtenerCompras("18598138-k")
#for e in ob:
#	print formatoFacturaXls(e)

ventas = obtenerVentas()
compras = obtenerCompras()
exportarxls(ventas, compras, path = "prueba.xls", contabilizar = False, guardarContabilizados = False, correlativo = 620)
