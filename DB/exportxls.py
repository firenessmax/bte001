#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
from facturas import *

def exportarxls(fVentas, fCompras, path = "", contabilizar = False, guardarContabilizados = False):
	libro = xlwt.Workbook()
	paginaVenta = libro.add_sheet("Ventas")
	for num, obj in enumerate(fVentas):
		fila = paginaVenta.row(num)
		datos = formatoFacturaXls(obj)
		if contabilizar:
			obj.contabilizado=1
			obj.save()
		for index, dato in enumerate(datos):
			fila.write(index, dato)
	paginaCompra = libro.add_sheet("Compras")
	for num, obj in enumerate(fCompras):
		fila = paginaCompra.row(num)
		datos = formatoFacturaXls(obj)
		if contabilizar:
			obj.contabilizado=1
			obj.save()
		for index, dato in enumerate(datos):
			fila.write(index, dato)
	print path+"prueba.xls"
	libro.save(path+"prueba.xls")
	


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
	print datos
	return datos
	
#ob = obtenerCompras("18598138-k")
#for e in ob:
#	print formatoFacturaXls(e)

ventas = obtenerVentas()
print "ventas : ", ventas
compras = obtenerCompras()
print "compras : ", compras
exportarxls(ventas, compras, path = "C:/proyectos BTE/", contabilizar = True)
