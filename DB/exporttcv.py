#!/usr/bin/env python
# -*- coding: utf-8 -*-

from facturas import *
import datetime

def exportarTxt(fVentas, fCompras, path = "", contabilizar = False, guardarContabilizados = False):
	fac = open(path.strip(".tcv")+"facturas.tcv", 'w')
	for obj in fCompras:
		if guardarContabilizados:
			datos = formatoFacturaTxtCompras(obj)
			if datos[2] != "N/A":
				linea = "1"
				linea += "," + str(datetime.datetime.now().month)
				linea += "," + str(datetime.datetime.now().year)
				if datos[1] == 46:linea += ",4"
				else:linea += ",2"
				linea += ''',"%s"'''%datos[2]
				linea += "," + str(atributoDoc(datos[1], datos[10], datos[13]))
				linea += "," + str(datos[3])
				linea += ''',"N"'''
				linea += ''', "%s'''%datos[8].split("-")[0] + '''%s"'''%datos[8].split("-")[1]
				linea += ''', "%s"'''%datos[9]
				formato1 = "%d/%m/%Y" 
				formato2 = "%d%m%Y" 
				fecha = datetime.datetime.strptime(datos[6], formato1)
				fecha = fecha.strftime(formato2)
				linea += "," + fecha
				linea += "," + fecha
				linea += "," + str(datos[11]) #dudas, puse el afecto, no se cual es aqui va el neto
				linea += "," + str(datos[10])
				linea += "," + str(datos[13])
				linea += "," + str(datos[15])
				linea += "," + str(datos[0])
				linea += ",,,,,,,,,"
				linea += "," + str(datos[42])
				linea += ''',"F"'''
				linea += ",0,0"
				linea += "," + str(datos[18])
				linea += ''',"N","N","N"'''
				linea += ''',"%s"''' % datos[14]
				linea += ",0,0,0,0,0"
				fac.write(linea.strip(",")+"\n")
		elif not guardarContabilizados and obj.contabilizado == 0:
			datos = formatoFacturaTxtCompras(obj)
			if datos[2] != "N/A":
				linea = "1"
				linea += "," + str(datetime.datetime.now().month)
				linea += "," + str(datetime.datetime.now().year)
				if datos[1] == 46:linea += ",4"
				else:linea += ",2"
				linea += ''',"%s"'''%datos[2]
				linea += "," + str(atributoDoc(datos[1], datos[10], datos[13]))
				linea += "," + str(datos[3])
				linea += ''',"N"'''
				linea += ''', "%s'''%datos[8].split("-")[0] + '''%s"'''%datos[8].split("-")[1]
				linea += ''', "%s"'''%datos[9]
				formato1 = "%d/%m/%Y" 
				formato2 = "%d%m%Y" 
				fecha = datetime.datetime.strptime(datos[6], formato1)
				fecha = fecha.strftime(formato2)
				linea += "," + fecha
				linea += "," + fecha
				linea += "," + str(datos[11]) #dudas, puse el afecto, no se cual es aqui va el neto
				linea += "," + str(datos[10])
				linea += "," + str(datos[13])
				linea += "," + str(datos[15])
				linea += "," + str(datos[0])
				linea += ",,,,,,,,,"
				linea += "," + str(datos[42])
				linea += ''',"F"'''
				linea += ",0,0"
				linea += "," + str(datos[18])
				linea += ''',"N","N","N"'''
				linea += ''',"%s"''' % datos[14]
				linea += ",0,0,0,0,0"
				fac.write(linea.strip(",")+"\n")
		if contabilizar:
			if datos[2] != "N/A":
				obj.contabilizado = 1
				obj.save() 
	for obj in fVentas:
		if guardarContabilizados:
			datos = formatoFacturaTxtCompras(obj)
			if datos[2] != "N/A":
				linea = "1"
				linea += "," + str(datetime.datetime.now().month)
				linea += "," + str(datetime.datetime.now().year)
				if datos[1] == 46:linea += ",3"
				else:linea += ",1"
				linea += ''',"%s"'''%datos[2]
				linea += "," + str(atributoDoc(datos[1], datos[10], datos[13]))
				linea += "," + str(datos[3])
				linea += ''',"N"'''
				linea += ''', "%s'''%datos[8].split("-")[0] + '''%s"'''%datos[8].split("-")[1]
				linea += ''', "%s"'''%datos[9]
				formato1 = "%d/%m/%Y" 
				formato2 = "%d%m%Y" 
				fecha = datetime.datetime.strptime(datos[6], formato1)
				fecha = fecha.strftime(formato2)
				linea += "," + fecha
				linea += "," + fecha
				linea += "," + str(datos[11]) #dudas, puse el afecto, no se cual es aqui va el neto
				linea += "," + str(datos[10])
				linea += "," + str(datos[13])
				linea += "," + str(datos[15])
				linea += "," + str(datos[0])
				linea += ",,,,,,,,,"
				linea += "," + str(datos[42])
				linea += ''',"F"'''
				linea += ",0,0"
				linea += "," + str(datos[18])
				linea += ''',"N","N","N"'''
				linea += ''',"%s"''' % datos[14]
				linea += ",0,0,0,0,0"
				fac.write(linea.strip(",")+"\n")
		elif not guardarContabilizados and obj.contabilizado == 0:
			datos = formatoFacturaTxtCompras(obj)
			if datos[2] != "N/A":
				linea = "1"
				linea += "," + str(datetime.datetime.now().month)
				linea += "," + str(datetime.datetime.now().year)
				if datos[1] == 46:linea += ",3"
				else:linea += ",1"
				linea += ''',"%s"'''%datos[2]
				linea += "," + str(atributoDoc(datos[1], datos[10], datos[13]))
				linea += "," + str(datos[3])
				linea += ''',"N"'''
				linea += ''', "%s'''%datos[8].split("-")[0] + '''%s"'''%datos[8].split("-")[1]
				linea += ''', "%s"'''%datos[9]
				formato1 = "%d/%m/%Y" 
				formato2 = "%d%m%Y" 
				fecha = datetime.datetime.strptime(datos[6], formato1)
				fecha = fecha.strftime(formato2)
				linea += "," + fecha
				linea += "," + fecha
				linea += "," + str(datos[11]) #dudas, puse el afecto, no se cual es aqui va el neto
				linea += "," + str(datos[10])
				linea += "," + str(datos[13])
				linea += "," + str(datos[15])
				linea += "," + str(datos[0])
				linea += ",,,,,,,,,"
				linea += "," + str(datos[42])
				linea += ''',"F"'''
				linea += ",0,0"
				linea += "," + str(datos[18])
				linea += ''',"N","N","N"'''
				linea += ''',"%s"''' % datos[14]
				linea += ",0,0,0,0,0"
				fac.write(linea.strip(",")+"\n")
		if contabilizar:
			if datos[2] != "N/A":
				obj.contabilizado = 1
				obj.save() 
	fac.close()


def atributoDoc(tipoDocumento, montoExento, montoTotal):
	if tipoDocumento == 33 or tipoDocumento == 46:
		if montoExento == 0: return 1
	if tipoDocumento == 34 or tipoDocumento == 46:
		if montoExento == montoTotal:return 2
		return 3
	if tipoDocumento == 110:return 4
	if tipoDocumento == 56:
		if montoExento == montoTotal:return 7
		elif montoExento != montoTotal: return 6
		else: return 8
	if tipoDocumento == 61:
		if montoExento == montoTotal:return 10
		elif montoExento != montoTotal: return 9
		else: return 11
	if tipoDocumento == 111:return 12
	if tipoDocumento == 112:return 13
	else:return 16

def formatoFacturaTxtCompras(factura):
	#print "llamada a formatear xls de compras"
	datos = []
	datos.append(factura.sucursal)
	datos.append(factura.TipoDocumento)
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
exportarTxt(ventas, compras, path = "", contabilizar = False, guardarContabilizados = True)
