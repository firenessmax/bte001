from PyQt4 import QtCore
import time
import DB.tableCreate as DB
import DB.facturas as F
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
        
        compras = F.obtenerCompras(empresa)
        
        listaDeCompras = [ [c._contabilizado, c._sucursal, c._TipoDocumento, c._numDocumento, 
                            c._fecha, c._rutEmisor, c._nomEmisor,  c._rutReceptor, c._nomReceptor, c._montoExento,
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
        ventas = F.obtenerVentas(empresa)
        
        listaDeVentas = [ [c._contabilizado, c._sucursal, c._TipoDocumento, c._numDocumento, 
                            c._fecha, c._rutEmisor, c._nomEmisor,  c._rutReceptor, c._nomReceptor, c._montoExento,
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
    empresas = ["17920814-8"]
    return empresas