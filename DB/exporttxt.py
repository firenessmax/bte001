#!/usr/bin/env python
# -*- coding: utf-8 -*-

from facturas import *

def exportarTxt(fVentas, fCompras, path = "", contabilizar = False, guardarContabilizados = False,  correlativo = 0):
	compra = open(path.strip(".tcv")+"Compras.tcv", 'w')
	for obj in fCompras:
		if guardarContabilizados:
			obj.correlativo = correlativo
			obj.save()
			datos = formatoFacturaTxtCompras(obj)
			linea = ""
			for dato in datos:
				linea += str(dato)+","
			correlativo+=1
			compra.write(linea.strip(",")+"\n")
		elif not guardarContabilizados and obj.contabilizado == 0:
			obj.correlativo = correlativo
			obj.save()
			datos = formatoFacturaTxtCompras(obj)
			linea = ""
			for dato in datos:
				linea += str(dato)+","
			correlativo += 1
			compra.write(linea.strip(",")+"\n")
		if contabilizar:
			obj.contabilizado = 1
			obj.save() 
	compra.close()
	
	venta = open(path.strip(".tcv")+"Ventas.tcv", 'w')
	for obj in fVentas:
		if guardarContabilizados:
			datos = formatoFacturaTxtVentas(obj)
			linea = ""
			for dato in datos:
				linea += str(dato)+","
			venta.write(linea.strip(",")+"\n")
		elif not guardarContabilizados and obj.contabilizado == 0:
			datos = formatoFacturaTxtVentas(obj)
			linea = ""
			for dato in datos:
				linea += str(dato)+","
			venta.write(linea.strip(",")+"\n")
	venta.close()


def formatoFacturaTxtCompras(factura):
	print "llamada a formatear xls de compras"
	datos = []
	datos.append(factura.sucursal)
	datos.append(switch(factura.TipoDocumento, factura.montoExento))
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
	datos.append(factura.montoAfecto + factura.montoExento)#Monto de contracuenta
	datos.append("")#Codigo especial contracuenta
	datos.append("")#Rut nacional contracuenta
	datos.append("")#Rut de contracuenta
	datos.append("")#Nombre rut contracuenta
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
	
def formatoFacturaTxtVentas(factura):
	print "llamada a formatear xls de ventas"
	datos = []
	datos.append(factura.sucursal)
	datos.append(switch(factura.TipoDocumento, factura.montoExento))
	datos.append(factura.numDocumento)
	if factura.nulo == 0: 
		datos.append("N")
	else:
		datos.append("S")
	datos.append(factura.fecha)
	datos.append("S")
	datos.append(factura.empresaReceptor.rut)
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
	datos.append(factura.montoAfecto + factura.montoExento)#Monto de Contracuenta
	datos.append("")#Codigo especial contracuenta
	datos.append("")#Rut nacional contracuenta
	datos.append("")#Rut de contracuenta
	datos.append("")#Nombre rut contracuenta
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
	
def switch(tipoDocumento, montoExento):
	if tipoDocumento == 33:
		if montoExento > 0:return "FP"
		return "FE"
	elif tipoDocumento == 34:return "FT"
	elif tipoDocumento == 46:
		if montoExento > 0:return "FP"
		return "FE"
	elif tipoDocumento == 56:return "ND"
	elif tipoDocumento == 61:return "NE"
	else:return "N/A"
	
ventas = obtenerVentas()
print "ventas : ", ventas
compras = obtenerCompras()
print "compras : ", compras
exportarTxt(ventas, compras, path = "prueba.tcv", contabilizar = False, guardarContabilizados = False, correlativo = 620)
