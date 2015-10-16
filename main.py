import sys
from PyQt4 import QtGui, QtCore
from sys import exit
from GUI.mainWindow import *
from GUI.escanearDialog import *
from GUI.nuevoDocumentoDialog import Ui_Dialog as Ui_Dialog_nuevoDocumento
from GUI.editarDocumentoDialog import Ui_Dialog as Ui_Dialog_editarDocumento

import LecturaController
import DBController
from instance import *#para el manejo de multiples instancias
import os
from random import randint

# Para que no use el icono de python
import ctypes
myappid = 'BTE.lector.gui.estable' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#----------------------------------- --- Vistas ------------------------------------ 
# TODO: escrbiendo
# aisjdaojsijd

#       asdasd
# Modal para Agregar documento
debug = True
if not Instance.verificar('main'):#cambiar 
    Instance.traeralfrente()
    exit(0) # Existe la instancia


class EditarDocumentoModal(QtGui.QDialog):
    
    def __init__(self, tipo, datos):
        super(EditarDocumentoModal, self).__init__()
        self.ui=Ui_Dialog_editarDocumento()
        self.ui.setupUi(self)
        # Tipo de documento
        self.tipo = tipo
        titulo = ""
        if(tipo==0):
            titulo = "Editar Documento Compra"
            self.ui.cuentaProveedoresClienteLabel.setText("Cuenta Proveedor")
        elif(tipo==1):
            titulo =  "Editar Documento Venta"
            self.ui.cuentaProveedoresClienteLabel.setText("Cuenta Cliente")
        self.setWindowTitle(titulo)
        #Fecha actual
        self.ui.fechaDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.sucursalLineEdit.setValidator( QtGui.QDoubleValidator(0, 100, 0, self) )

        self.ui.cuentaProveedoresClienteLineEdit.setValidator( QtGui.QDoubleValidator(0, 100, 0, self) )
        self.ui.contracuentaLineEdit.setValidator( QtGui.QDoubleValidator(0, 100, 0, self) )
        
        self.datos = datos
        self.llenarDatos()
        self.resultado = False
        self.exec_()
    def accept(self):
        print "Guardando documento"
        self.datos["Numero Documento"] = str(self.ui.nDocumentoLineEdit.text())
        self.datos["RS Emisor"] = str(self.ui.emisorLineEdit.text())
        self.datos["RS Receptor"] = str(self.ui.receptorLineEdit.text())
        self.datos["Fecha"] = str(self.ui.fechaDateEdit.text())
        self.datos["Sucursal"] =str( self.ui.sucursalLineEdit.text())
        self.datos["Glosa"] = str(self.ui.glosaLineEdit.text())
        self.datos["Monto Exento"] = str(self.ui.montoExcentoSpinBox.value())
        self.datos["Cuenta"] = str(self.ui.cuentaProveedoresClienteLineEdit.text())
        self.datos["Contracuenta"] = str(self.ui.contracuentaLineEdit.text())
        # Si uno de los datos esta vacio
        # TODO: Cambiar color al encontrar error
        fallas = []
        for key, value in self.datos.items():
            print key," : ", value
            if(not ("%s"%value)):
                fallas.append(key)
        error = ""
        for i in fallas:
            error = error+"%s\n"%i
        if(len(fallas)!=0):
            QtGui.QMessageBox.about(self, "Datos incompletos", "Faltan datos a ingresar en los siguientes campos:\n%s"%error)
        else:
            # Guardando
            DBController.modificarFactura(self.datos, self.tipo)
            self.resultado = True
            self.close()
    def llenarDatos(self):
        self.ui.montoExcentoSpinBox.setMaximum(2**53)
        if(self.tipo == 0):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11070100")
        elif(self.tipo == 1):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11040100")
        
        for key, value in self.datos.items():
            print key," : ", value
        self.ui.nDocumentoLineEdit.setText(self.datos["Numero Documento"])
        self.ui.emisorLineEdit.setText(self.datos["RS Emisor"])
        self.ui.receptorLineEdit.setText(self.datos["RS Receptor"])
        self.ui.fechaDateEdit.setDate(QtCore.QDate.fromString(self.datos["Fecha"], "yyyy-MM-dd"))
        self.ui.sucursalLineEdit.setText(self.datos["Sucursal"])
        self.ui.glosaLineEdit.setText(self.datos["Glosa"])
        self.ui.montoExcentoSpinBox.setValue(float(self.datos["Monto Exento"]))
        
        '''
        11070100 "proveedores"->"Compra"
        11040100 "cliente"->"Venta"
        if(xmlp.TD == 34):
            montoExcento = Total
        self.ui.montoExcentoSpinBox.setMax(montoTotal)
        '''
        if(self.tipo == 0):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11070100")
        elif(self.tipo == 1):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11040100")
        self.ui.contracuentaLineEdit.setText(self.datos["Contracuenta"])
        #TODO: Descomentar esta linea
        #self.ui.montoExcentoSpinBox.setMaximum(int(self.datos["Monto Total"]))


class AgregarDocumentoModal(QtGui.QDialog):
    
    def __init__(self, tipo, datos):
        super(AgregarDocumentoModal, self).__init__()
        self.ui=Ui_Dialog_nuevoDocumento()
        self.ui.setupUi(self)
        # Tipo de documento
        self.tipo = tipo
        titulo = ""
        if(tipo==0):
            titulo = "Nuevo Documento Compra"
            self.ui.cuentaProveedoresClienteLabel.setText("Cuenta Proveedor")
        elif(tipo==1):
            titulo =  "Nuevo Documento Venta"
            self.ui.cuentaProveedoresClienteLabel.setText("Cuenta Cliente")
        self.setWindowTitle(titulo)
        #Fecha actual
        self.ui.fechaDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.sucursalLineEdit.setValidator( QtGui.QDoubleValidator(0, 100, 0, self) )

        self.ui.cuentaProveedoresClienteLineEdit.setValidator( QtGui.QDoubleValidator(0, 100, 0, self) )
        self.ui.contracuentaLineEdit.setValidator( QtGui.QDoubleValidator(0, 100, 0, self) )
        
        self.datos = datos
        self.llenarDatos()
        self.resultado = False
        self.exec_()
        
    def accept(self):
        print "Guardando documento"
        # Datos
        # Limitar a numeros o alfanumerico
        
        self.datos["Numero Documento"] = str(self.ui.labelNDocumento.text())
        self.datos["RS Emisor"] = str(self.ui.labelEmisor.text())
        self.datos["RS Receptor"] = str(self.ui.labelReceptor.text())
        self.datos["Fecha"] = str(self.ui.fechaDateEdit.text())
        self.datos["Sucursal"] =str( self.ui.sucursalLineEdit.text())
        self.datos["Glosa"] = str(self.ui.glosaLineEdit.text())
        self.datos["Monto Exento"] = str(self.ui.montoExcentoSpinBox.value())
        self.datos["Cuenta"] = str(self.ui.cuentaProveedoresClienteLineEdit.text())
        self.datos["Contracuenta"] = str(self.ui.contracuentaLineEdit.text())
        
        # Si uno de los datos esta vacio
        # TODO: Cambiar color al encontrar error
        fallas = []
        for key, value in self.datos.items():
            print key," : ", value
            if(not ("%s"%value)):
                fallas.append(key)
        error = ""
        for i in fallas:
            error = error+"%s\n"%i
        if(len(fallas)!=0):
            QtGui.QMessageBox.about(self, "Datos incompletos", "Faltan datos a ingresar en los siguientes campos:\n%s"%error)
        else:
            # Guardando
            
            DBController.guardarFactura(self.datos, self.tipo)
            self.resultado = True
            self.close()
    def llenarDatos(self):
        self.ui.montoExcentoSpinBox.setMaximum(2**53)
        if(self.tipo == 0):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11070100")
        elif(self.tipo == 1):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11040100")
        
        for key, value in self.datos.items():
            print key," : ", value
        self.ui.labelNDocumento.setText(self.datos["Numero Documento"])
        self.ui.labelEmisor.setText(self.datos["RS Emisor"])
        self.ui.labelReceptor.setText(self.datos["RS Receptor"])
        self.ui.fechaDateEdit.setDate(QtCore.QDate.fromString(self.datos["Fecha"], "yyyy-MM-dd"))
        
        '''
        11070100 "proveedores"->"Compra"
        11040100 "cliente"->"Venta"
        if(xmlp.TD == 34):
            montoExcento = Total
        self.ui.montoExcentoSpinBox.setMax(montoTotal)
        '''
        if(self.tipo == 0):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11070100")
        elif(self.tipo == 1):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11040100")
        self.ui.montoExcentoSpinBox.setMaximum(int(self.datos["Monto Total"]))
# Modal para escanear codigo
class EscanearModal(QtGui.QDialog):
    def __init__(self, tipo, window):
        super(EscanearModal, self).__init__()
        self.ui=Ui_Dialog()
        self.encontrado_slot = self.encontrado
        self.reject = self.terminar
        self.tipo = tipo
        self.window = window
        self.ui.setupUi(self)
        self.thread = LecturaController.EscanerThread()
        self.thread.finished.connect(self.terminado)
        self.thread.start()
        self.exec_()
    def terminar(self):
        print "Terminado por usuario"
        self.thread.parar = True
        self.accept()
    def terminado(self):
        print "Terminando thread"
    def encontrado(self):
        #Codigo encontrado, mostrar nuevo escanearDialog
        self.thread.parar = True
        datos = {}
        datos["Numero Documento"] = str(randint(11231231,91231231)) #"31231231"
        datos["Rut Emisor"] = "12544959-k"
        datos["Rut Receptor"] = "18598138-k"
        datos["RS Emisor"] = "Pepito"
        datos["RS Receptor"] = "Lucho"
        datos["Fecha"] = "2013-12-12"
        datos["Monto Total"] = 1000
        if(DBController.existeFactura(self.tipo, datos)):
            print "La factura ya existe!!!"
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Advertencia')
            qm.setText('''Esta factura ya ha sido ingresada.\nDesea editarla?''')
            qm.addButton(QtGui.QMessageBox.Yes).setText("Si")
            qm.addButton(QtGui.QMessageBox.No).setText("No")
            qm.setIcon(QtGui.QMessageBox.Warning)
            reply = qm.exec_()
            
            if reply == QtGui.QMessageBox.Yes:
                # Eliminar de la base de datos
                print "Editar Dilog!!!"
        else:
            agregar = AgregarDocumentoModal(self.tipo, datos)
            if(agregar.resultado):
                self.window.updateTablas()
                self.thread.start()
# Ventana Principal 
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        # Inicializar Ventana
        self.escanear_slot = self.escanear
        self.exportar_slot = self.exportar
        self.cambiarTab_slot = self.cambiarTab
        self.filtrar_slot = self.filtrar
        self.documentoCambiarTab_slot = self.resetFiltro
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.tableWidget_Compras.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableWidget_Compras.customContextMenuRequested.connect(self.clicked)
        self.ui.tableWidget_Ventas.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableWidget_Ventas.customContextMenuRequested.connect(self.clicked)
        self.updateEmpresas()
        self.inicializarDatos(self.ui.tableWidget_Compras)
        self.inicializarDatos(self.ui.tableWidget_Ventas)
        self.ui.labelClose.mousePressEvent = self.cerrar
        self.ui.labelMinimize.mouseReleaseEvent = self.minimizar
        self.moving = False
        self.ui.frame.mousePressEvent = self._mousePressEvent
        self.ui.frame.mouseMoveEvent = self._mouseMoveEvent
        self.ui.tabWidget_4.tabBar().mousePressEvent = self._mousePressEvent
        self.ui.tabWidget_4.tabBar().mouseMoveEvent = self._mouseMoveEvent
        
        
        
        self.show()
        
    def cerrar(self, data):
        print "Cerrars"
        self.close()
    def minimizar(self, data):
        print "Minimize"
        self.ui.labelMinimize.repaint()
        
        self.showMinimized()
    def cambiarTab(self, pos):
        estilos = [ "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(2, 136, 209, 230) , stop:.2 rgba(25, 118, 210, 250));",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(67, 160, 71, 230)  , stop:.2 rgba(56, 142, 60, 250));",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(158, 158, 158, 230) , stop:.2 rgba(136, 136, 136, 250));"]
        resto = "#top{%s border-top-left-radius:3px; border-top-right-radius: 3px;}"
        self.ui.top.setStyleSheet(resto%(estilos[pos]))
        print pos
    def resetFiltro(self, data):
        
        print data
    def escanear(self):

        if( self.sender().objectName()  == "escanearCompra"):
            my_dialog = EscanearModal(0, self) 
        elif( self.sender().objectName()  == "escanearVenta"):
            my_dialog = EscanearModal(1, self) 
    
    def exportar(self):

        # Opciones
        correlativo = self.ui.correlativoSpinBox.value()
        contabilizar = self.ui.contabilizarCheckBox.isChecked()
        guardar = self.ui.guardarCheckBox.isChecked()
        print "Corr: %d cont: %s Guardar: %s"%(correlativo, contabilizar, guardar)
        archivo = None
        print "LKSDLKASDN: ", self.sender().objectName()
        if(self.sender().objectName() == "toolButtonPlano"):
            archivo = QtGui.QFileDialog.getSaveFileName(self, directory=(os.path.expanduser("~/Documents/")+"Facturas.txt"), filter="Texto plano (*.txt)")
        else:    
            archivo = QtGui.QFileDialog.getSaveFileName(self, directory=(os.path.expanduser("~/Documents/")+"Facturas.xlsx"), filter="Microsoft Excel (*.xlsx)")
        if(archivo == ""):
            print "Cancelado!!"
        else:
            #TODO: try permiso de escritura 
            DBController.exportarExcel(str(self.ui.filtrarEmpresaComboBox.currentText()), archivo, contabilizar, guardar, correlativo)
            self.updateTablas()
            print "Guardando archivo",archivo

    def clicked(self, position):
        if(self.sender().rowCount()==0): # Ninguna fila en la tabla
            return
        tabla = self.sender()
        menu = QtGui.QMenu()
        editarAction = menu.addAction("Editar")
        eliminarAction = menu.addAction("Eliminar")
        contabilizarAction = menu.addAction("Contabilizar")
        action = menu.exec_(tabla.viewport().mapToGlobal(position))
        print "item clickeado: %s"%tabla.rowAt(position.y())
        row = tabla.rowAt(position.y())
        allRows = tabla.columnCount()
        for i in range(0, allRows):
            print "i: ",i
            print tabla.item(row,i).text()
        
        if action == editarAction:
            print "Editars"
            # Pasar los chorrocientos datos
            datos = {}
            
            for i in range(tabla.horizontalHeader().count()):
                datos[ str(tabla.horizontalHeaderItem(i).text())] =  str(tabla.item(row,i).text())
                print "[%s]: %s"%( str(tabla.horizontalHeaderItem(i).text()).replace("Rut ", "") , tabla.item(row,i).text())
            
            
            if(self.sender().objectName()=="tableWidget_Ventas"):
                my_dialog = EditarDocumentoModal(1, datos ) 
                print "RESULTAOD::", my_dialog.resultado
                if(my_dialog.resultado):
                    self.updateTablas()
            else:
                my_dialog = EditarDocumentoModal(0, datos ) 
                print "RESULTAOD::", my_dialog.resultado
                if(my_dialog.resultado):
                    self.updateTablas()
        if action == eliminarAction:
            # TODO: Si se seleccionan varias columnas, eliminarlas todas
            # TODO: lanzar evento al oprimir suprimir,
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Eliminar documento')
            qm.setText("Esta seguro de que desea eliminar el documento?")
            qm.addButton(QtGui.QMessageBox.Yes).setText("Si")
            qm.addButton(QtGui.QMessageBox.No).setText("No")
            qm.setIcon(QtGui.QMessageBox.Question)
            reply = qm.exec_()
            
            if reply == QtGui.QMessageBox.Yes:
                # Eliminar de la base de datos
                # if(deleteDocumento(id)):
                    #print "Eliminarlo"
                    #tabla.removeRow(row)
                # else:
                    #QtGui.QMessageBox.critical(self, "Error", "Error al eliminar en la base de datos")
                print "Eliminarlo"
                for idx in reversed(tabla.selectionModel().selectedRows()):
                    #print [ "[%s]: %s"%( str(tabla.horizontalHeaderItem(i).text()).replace("Rut ", "") , tabla.item(idx.row(),i).text()) for i in range(tabla.horizontalHeader().count())]
                    print "ID: ",tabla.item(idx.row(),15).text()
                    DBController.eliminarFactura(tabla.item(idx.row(),15).text())
                    tabla.removeRow(idx.row())
                #tabla.removeRow(row)
            else:
                print "Cancelar"
            
            
    def inicializarDatos(self, tabla):
        
        for i in range(tabla.horizontalHeader().count()):
            tabla.horizontalHeader().setResizeMode(i, QtGui.QHeaderView.Stretch)

        documentos = DBController.obtenerLista(tabla.objectName(), None)
        tabla.setRowCount(len(documentos))
        for i in range(len(documentos)):
            for j in range(len(documentos[i])):
                tabla.setItem(i, j, QtGui.QTableWidgetItem(documentos[i][j]))
        for i in range(tabla.verticalHeader().count()):
            tabla.verticalHeader().setResizeMode(i, QtGui.QHeaderView.Fixed)
        tabla.setColumnHidden(tabla.horizontalHeader().count()-1, True)
    def updateTablas(self):
        self.filtrar(self.ui.filtrarEmpresaComboBox.currentText())
        self.updateEmpresas()
        
    def filtrar(self, data):
        tablas = [self.ui.tableWidget_Compras, self.ui.tableWidget_Ventas]
        for tabla in tablas:
            documentos = DBController.obtenerLista(tabla.objectName(), str(data))
            tabla.clearContents()
            tabla.setRowCount(len(documentos))
            for i in range(len(documentos)):
                for j in range(len(documentos[i])):
                    tabla.setItem(i, j, QtGui.QTableWidgetItem(documentos[i][j]))
        
        print "filtrar!!!!!!!"
        print "data: %s"%data
    def updateEmpresas(self):
        self.ui.filtrarEmpresaComboBox.clear()
        self.ui.filtrarEmpresaComboBox.addItem("Todas")
        for e in DBController.getEmpresas():
            self.ui.filtrarEmpresaComboBox.addItem(e)
    
    def _mousePressEvent(self,event):

        if event.button() == QtCore.Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def _mouseMoveEvent(self,event):
        if self.moving: self.move(event.globalPos()-self.offset)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()