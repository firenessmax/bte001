from PyQt4 import QtCore
import time
import DB.tableCreate as DB
import DB.facturas as Facturas
import DB.empresas as Empresas
import DB.exportxls as ExportarExcel
import DB.exporttcv as ExportarTCV
import DB.backup as Backup
def obtenerLista(tabla, empresa):
    # Devolver lista de facturas con el formato
    # [Contabilizado, Sucursal, Tipo Documento, Numero Documento, Fecha, Emisor, RS Emisor, Receptor, RS Receptor', Monto Exento, Monto Afecto, Monto IVA, Monto Total, Glosa, Contracuenta, id]
     #print "Tabla: %s"%tabla
     #print tabla
     #print empresa
    
    DB.iniciarDB()
    if(empresa == "Todas"):
        empresa = None
    if(tabla == "tableWidget_Compras"):
        # Consulta Compras}
        compras = Facturas.obtenerCompras(empresa)
        
        listaDeCompras = [ [c._contabilizado, c._sucursal, c._TipoDocumento, c._numDocumento, 
                            c._fecha, c.empresaEmisor.rut, c.empresaEmisor.rS,  c.empresaReceptor.rut, c.empresaReceptor.rS, c._montoExento,
                            c._montoAfecto,c._montoIVA ,c._montoTotal, c._Glosa, c._contracuenta, c._activoFijo, c._id] for c in compras]
        for i in range(0, len(listaDeCompras)):
            for j in range(0, len(listaDeCompras[i])):
                if(j==0 or j==15):
                    if(listaDeCompras[i][j]==0):
                        listaDeCompras[i][j] = "No"
                    else:
                        listaDeCompras[i][j] = "Si"
                listaDeCompras[i][j] = str(listaDeCompras[i][j])                
         #print "Lista de comrpas:",listaDeCompras
        return listaDeCompras
        #prueba.save()
        
    elif(tabla == "tableWidget_Ventas"):
        # consulta Ventas
        ventas = Facturas.obtenerVentas(empresa)
        
        listaDeVentas = [ [c._contabilizado, c._sucursal, c._TipoDocumento, c._numDocumento, 
                            c._fecha, c.empresaEmisor.rut, c.empresaEmisor.rS,  c.empresaReceptor.rut, c.empresaReceptor.rS, c._montoExento,
                            c._montoAfecto,c._montoIVA ,c._montoTotal, c._Glosa, c._contracuenta, c._activoFijo, c._id] for c in ventas]
        for i in range(0, len(listaDeVentas)):
            for j in range(0, len(listaDeVentas[i])):
                if(j==0 or j==15):
                    if(listaDeVentas[i][j]==0):
                        listaDeVentas[i][j] = "No"
                    else:
                        listaDeVentas[i][j] = "Si"
                listaDeVentas[i][j] = str(listaDeVentas[i][j])                
        return listaDeVentas
     #print "Filtro Empresa: %s"%empresa
    return fac
    
def getEmpresas():
    emp = Empresas.obtenerEmpresas()
    empresas = [[e.rut, e.rS] for e in emp]
    return empresas

def guardarFactura(datos, venta):
    f = Facturas.facturas(venta = venta, numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Rut Receptor"], rutEmisor = datos["Rut Emisor"])
    #nomReceptor=datos["RS Receptor"], nomEmisor=["RS Emisor"])
    f.save()
    
    f = Facturas.facturas(venta = venta, numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Rut Receptor"], rutEmisor = datos["Rut Emisor"], esNuevo = False)
    if(f.empresaEmisor.rS == ""):
        f.empresaEmisor.rS = datos["RS Emisor"]
        f.empresaEmisor.save()
    if(f.empresaReceptor.rS == ""):
        f.empresaReceptor.rS = datos["RS Receptor"]
        f.empresaReceptor.save()
    f.fecha = datos["Fecha"]
    f.sucursal = datos["Sucursal"]
    f.montoTotal = int(datos["Monto Total"])
    f.Glosa = datos["Glosa"]
    f.montoExento = int(float(datos["Monto Exento"]))
    f.cuentaProveedores = datos["Cuenta"]
    f.contracuenta = datos["Contracuenta"]
    f.TipoDocumento = datos["Tipo Documento"]
    f.activoFijo = datos["Activo Fijo"]
    f.correlativo = int(datos["Correlativo"])
    f.save()
    
     #print datos
def modificarFactura(f, datos, venta):
     #print "MODIFICAR::", datos
    #f = Facturas.facturas(venta = venta, numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Rut Receptor"], rutEmisor = datos["Rut Emisor"],
    #nomReceptor=datos["RS Receptor"], nomEmisor=["RS Emisor"], esNuevo = False)
    
    f.empresaEmisor.rS = datos["RS Emisor"]
    f.numDocumento = int(datos["Numero Documento"])
    f.empresaReceptor.rS = datos["RS Receptor"]
    f.empresaEmisor.save()
    f.empresaReceptor.save()
    f.fecha = datos["Fecha"]
    f.sucursal = datos["Sucursal"]
    f.Glosa = datos["Glosa"]
    f.montoExento = int(float(datos["Monto Exento"]))
    f.cuentaProveedores = datos["Cuenta"]
    f.contracuenta = datos["Contracuenta"]
    f.activoFijo = int(datos["Activo Fijo"])
    f.correlativo = int(datos["Correlativo"])
    f.save()
    
     #print datos
def existeFactura(venta, datos):
    try:
        f = Facturas.facturas(venta = venta, numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Rut Receptor"], rutEmisor = datos["Rut Emisor"])
        return False
    except Exception as e:
         #print "MENSAJE DE ERROR!!OIGO)FBIU: ",e
        return True
def eliminarFactura(id):
    Facturas.deleteFactura(int(id))
     #print "Eliminando Factura ",id
def exportarExcel(filtro, path, cont, guardarCont):
    print "Exportando ", filtro
    if (filtro == "Todas"):
        filtro = None
    ventas = Facturas.obtenerVentas(filtro)
    compras = Facturas.obtenerCompras(filtro)
    ExportarExcel.exportarxls(ventas, compras, path = str(path), contabilizar = cont, guardarContabilizados = guardarCont)
def exportarTCV(filtro, path, cont, guardarCont):
    #print "Exportando ", filtro
    if (filtro == "Todas"):
        filtro = None
    ventas = Facturas.obtenerVentas(filtro)
    compras = Facturas.obtenerCompras(filtro)
    ExportarTCV.exportarTxt(ventas, compras, path = str(path), contabilizar = cont, guardarContabilizados = guardarCont)
def getFactura(datos, venta):
    try:
        return Facturas.facturas(venta = venta,numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Rut Receptor"], rutEmisor = datos["Rut Emisor"], nomReceptor=datos["RS Receptor"], nomEmisor=["RS Emisor"], esNuevo = False)
    except:
        return None
def ultimaFactura(empresa):
    e = Empresas.empresas(rut=empresa, esNuevo = False)
    try:
        return Facturas.ultimosDatosFactura(e)
    except:
        return None
    
def contabilizar(s, venta, contabilizar, lista):
     #print "NASDKLNASD",lista
    for datos in lista:
        f = Facturas.facturas(venta = venta,numDocumento = int(datos["Numero Documento"]), rutReceptor = datos["Rut Receptor"], rutEmisor = datos["Rut Emisor"], nomReceptor=datos["RS Receptor"], nomEmisor=["RS Emisor"], esNuevo = False)
        f.contabilizado = contabilizar
        f.save()
    s.updateTablas()

def contabilizarFacturas(lista, value):
    l = Facturas.obtenerFacturasPorId(lista)
    for f in l:
        f.contabilizado = value
        f.save()
def backup(path):
    Backup.dump_to_file(path)
def verificar(path):
    try:
        Backup.verificacionBackup(path)
        return True
    except:
        return False
    
def restaurar(path):
    Backup.restore_db(nombre = path)
    
    