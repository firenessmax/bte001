from PyQt4 import QtCore
import time
import DB.tableCreate as DB
import DB.facturas as Facturas
import DB.empresas as Empresas
def obtenerLista(tabla, empresa):
    # Devolver lista de facturas con el formato
    # [Contabilizado, Sucursal, Tipo Documento, Numero Documento, Fecha, Emisor, RS Emisor, Receptor, RS Receptor', Monto Exento, Monto Afecto, Monto IVA, Monto Total, Glosa, Contracuenta, id]
    print "Tabla: %s"%tabla
    print tabla
    print empresa
    
    DB.iniciarDB()
    if(empresa == "Todas"):
        empresa = None
    if(tabla == "tableWidget_Compras"):
        # Consulta Compras
        
        compras = Facturas.obtenerCompras(empresa)
        
        listaDeCompras = [ [c._contabilizado, c._sucursal, c._TipoDocumento, c._numDocumento, 
                            c._fecha, c.empresaEmisor.rut, c.empresaEmisor.rS,  c.empresaReceptor.rut, c.empresaReceptor.rS, c._montoExento,
                            c._montoAfecto,c._montoIVA ,c._montoTotal, c._Glosa, c._contracuenta, c._id] for c in compras]
        for i in range(0, len(listaDeCompras)):
            for j in range(0, len(listaDeCompras[i])):
                if(j==0):
                    if(listaDeCompras[i][j]==0):
                        listaDeCompras[i][j] = "No"
                    else:
                        listaDeCompras[i][j] = "Si"
                listaDeCompras[i][j] = str(listaDeCompras[i][j])                
        return listaDeCompras
        #prueba.save()
        
    elif(tabla == "tableWidget_Ventas"):
        # consulta Ventas
        ventas = Facturas.obtenerVentas(empresa)
        
        listaDeVentas = [ [c._contabilizado, c._sucursal, c._TipoDocumento, c._numDocumento, 
                            c._fecha, c.empresaEmisor.rut, c.empresaEmisor.rS,  c.empresaReceptor.rut, c.empresaReceptor.rS, c._montoExento,
                            c._montoAfecto,c._montoIVA ,c._montoTotal, c._Glosa, c._contracuenta, c._id] for c in ventas]
        for i in range(0, len(listaDeVentas)):
            for j in range(0, len(listaDeVentas[i])):
                if(j==0):
                    if(listaDeVentas[i][j]==0):
                        listaDeVentas[i][j] = "No"
                    else:
                        listaDeVentas[i][j] = "Si"
                listaDeVentas[i][j] = str(listaDeVentas[i][j])                
        return listaDeVentas
    print "Filtro Empresa: %s"%empresa
    return fac
    
def getEmpresas():
    emp = Empresas.obtenerEmpresas()
    empresas = [e.rut for e in emp]
    return empresas

def guardarFactura(datos, venta):
    f = Facturas.facturas(venta = venta, numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Receptor"], rutEmisor = datos["Emisor"],
    nomReceptor="PePe", nomEmisor="Lucho")
    f.save()
    f = Facturas.facturas(venta = venta, numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Receptor"], rutEmisor = datos["Emisor"],
    nomReceptor="PePe", nomEmisor="Lucho", esNuevo = False)
    f.fecha = datos["Fecha"]
    f.sucursal = datos["Sucursal"]
    f.Glosa = datos["Glosa"]
    f.montoExento = int(float(datos["Monto Exento"]))
    f.cuentaProveedores = datos["Cuenta"]
    f.contracuenta = datos["Contracuenta"]
    f.save()
    
    print datos