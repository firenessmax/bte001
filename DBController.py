from PyQt4 import QtCore
import time
import DB.tableCreate as DB
import DB.facturas as F
def obtenerLista(tabla, empresa):
    # Devolver lista de facturas con el formato
    # [Contabilizado, Sucursal, Tipo Documento, Numero Documento, Fecha, Emisor, RS Emisor, Receptor, RS Receptor', Monto Exento, Monto Afecto, Monto IVA, Monto Total, Glosa, Contracuenta, id]
    print "Tabla: %s"%tabla
    print tabla
    
    if(tabla == "tableWidget_Compras"):
        # consulta Compras
        #DB.iniciarDB()
        #prueba = F.facturas(1,1,"17920814-8","8953221-3", nomEmisor = "Mami")
        #prueba.nomEmisor="mamaita ta ta"
        #prueba = facturas(0,9,"19144519-8","17920814-8", nomEmisor = "Rodri", nomReceptor = "cris")
        #obtenerVentas(prueba)
        print F.obtenerCompras(None)
        #prueba.save()
        
    elif(tabla == "tableWidget_Ventas"):
        # consulta Ventas
        pass
    print "Filtro Empresa: %s"%empresa
    
    
    fac = [['Si', 'Maipu', 'Factura', '90182309', '2002-6-12', '1898123-k', 'Luchos','a', '2', '3', '4', '5', '6', '7', '8', '1'],
            ['No', 'Cerrillos', 'Boletita', '12383', '2011-11-12', '9281923-0', 'Pablos','a', '2', '3', '4', '5', '6', '7', '8', '2'],
            ['Si', 'Estacion Central', 'Factura', '982389', '2014-12-12', '22929213-3', 'Nestors','a', '2', '3', '4', '5', '6', '7', '8', '3'],
            ['No', 'Cerro Navia', 'Boleta', '3482834', '2013-02-11', '00029123-7', 'Cristian-chan','a', '2', '3', '4', '5', '6', '7', '8', '4'],
            ['Si', 'Maipu', 'Factura', '90182309', '2002-6-12', '1898123-k', 'Luchos','a', '2', '3', '4', '5', '6', '7', '8', '5'],
            ['Si', 'Cerrillos', 'Boletita', '12383', '2011-11-12', '9281923-0', 'Pablos','a', '2', '3', '4', '5', '6', '7', '8', '6'],
            ['No', 'Estacion Central', 'Factura', '982389', '2014-12-12', '22929213-3', 'Nestors','a', '2', '3', '4', '5', '6', '7', '8', '7'],
            ['Si', 'Cerro Navia', 'Boleta', '3482834', '2013-02-11', '00029123-7', 'Cristian-chan','a', '2', '3', '4', '5', '6', '7', '8', '8'],
            ['No', 'Maipu', 'Factura', '90182309', '2002-6-12', '1898123-k', 'Luchos', 'a', '2', '3', '4', '5', '6', '7', '8','9'],
            ['Si', 'Cerrillos', 'Boletita', '12383', '2011-11-12', '9281923-0', 'Pablos','a', '2', '3', '4', '5', '6', '7', '8', '10'],
            ['Si', 'Estacion Central', 'Factura', '982389', '2014-12-12', '22929213-3', 'Nestors','a', '2', '3', '4', '5', '6', '7', '8', '11'],
            ['No', 'Cerro Navia', 'Boleta', '3482834', '2013-02-11', '00029123-7', 'Cristian-chan','a', '2', '3', '4', '5', '6', '7', '8', '12'],
            ['Si', 'Maipu', 'Factura', '90182309', '2002-6-12', '1898123-k', 'Luchos','a', '2', '3', '4', '5', '6', '7', '8', '13'],
            ['No', 'Cerrillos', 'Boletita', '12383', '2011-11-12', '9281923-0', 'Pablos','a', '2', '3', '4', '5', '6', '7', '8', '14'],
            ['No', 'Estacion Central', 'Factura', '982389', '2014-12-12', '22929213-3', 'Nestors','a', '2', '3', '4', '5', '6', '7', '8', '15'],
            ['Si', 'Cerro Navia', 'Boleta', '3482834', '2013-02-11', '00029123-7', 'Cristian-chan', 'a', '2', '3', '4', '5', '6', '7', '8', '16'],
            ]
    
    if(empresa == "Empresa1"):
        return [['Si', 'Maipu', 'Factura', '90182309', '2002-6-12', '1898123-k', 'Luchos','a', '2', '3', '4', '5', '6', '7', '8', '1'],
        ]
    elif(empresa == "Empresa2"):
        return [['Nai', 'Maipu', 'Factura', '90182309', '2002-6-12', '1898123-k', 'Luchos','a', '2', '3', '4', '5', '6', '7', '8', '1'],
        ]
    else:
        return fac
    return fac