import sys
from PyQt4 import QtGui, QtCore

from GUI.mainWindow import *
from GUI.escanearDialog import *
from GUI.nuevoDocumentoDialog import Ui_Dialog as Ui_Dialog_nuevoDocumento
import LecturaController
import DBController
import os
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
        if(datos != None):
            titulo = titulo.replace("Nuevo", "Editar")
        self.setWindowTitle(titulo)
        #Fecha actual
        self.ui.fechaDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.datos = datos
        self.llenarDatos()
        self.exec_()
    def accept(self):
        print "Guardando documento"
        # Datos
        # Limitar a numeros o alfanumerico
        
        self.datos["Numero Documento"] = self.ui.nDocumentoLineEdit.text()
        self.datos["Emisor"] = self.ui.emisorLineEdit.text()
        self.datos["Receptor"] = self.ui.receptorLineEdit.text()
        self.datos["Fecha"] = self.ui.fechaDateEdit.text()
        self.datos["Sucursal"] = self.ui.sucursalLineEdit.text()
        self.datos["Glosa"] = self.ui.glosaLineEdit.text()
        self.datos["Monto Exento"] = self.ui.montoExcentoSpinBox.value()
        self.datos["Cuenta"] = self.ui.cuentaProveedoresClienteLineEdit.text()
        self.datos["Contracuenta"] = self.ui.contracuentaLineEdit.text()
        
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
            self.close()
    def llenarDatos(self):
        self.ui.montoExcentoSpinBox.setMaximum(2**53)
        if(self.tipo == 0):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11070100")
        elif(self.tipo == 1):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11040100")
        
        if(self.datos == None):
            self.datos = {}
            self.datos["Numero Documento"] = "912309123"
            self.datos["Emisor"] = "9123123-k"
            self.datos["Receptor"] = "9123123-2"
            self.datos["Fecha"] = "2013-12-12"
            
            self.ui.nDocumentoLineEdit.setText(self.datos["Numero Documento"])
            self.ui.emisorLineEdit.setText(self.datos["Emisor"])
            self.ui.receptorLineEdit.setText(self.datos["Receptor"])
            self.ui.fechaDateEdit.setDate(QtCore.QDate.fromString(self.datos["Fecha"]))
            return
        for key, value in self.datos.items():
            print key," : ", value
        self.ui.nDocumentoLineEdit.setText(self.datos["Numero Documento"])
        self.ui.emisorLineEdit.setText(self.datos["Emisor"])
        self.ui.receptorLineEdit.setText(self.datos["Receptor"])
        self.ui.fechaDateEdit.setDate(QtCore.QDate.fromString(self.datos["Fecha"], "yyyy-MM-dd"))
        self.ui.sucursalLineEdit.setText(self.datos["Sucursal"])
        self.ui.glosaLineEdit.setText(self.datos["Glosa"])
        self.ui.montoExcentoSpinBox.setValue(int(self.datos["Monto Exento"]))
        
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
        self.ui.montoExcentoSpinBox.setMaximum(int(self.datos["Monto Total"]))
# Modal para escanear codigo
class EscanearModal(QtGui.QDialog):
    def __init__(self, tipo):
        super(EscanearModal, self).__init__()
        self.ui=Ui_Dialog()
        self.encontrado_slot = self.encontrado
        self.reject = self.terminar
        self.tipo = tipo
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
        my_dialog = AgregarDocumentoModal(self.tipo, None) 
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
        self.show()
        
    def cerrar(self, data):
        print "Cerrars"
        self.close()
    def minimizar(self, data):
        print "Minimize"
        self.ui.labelMinimize.repaint()
        
        self.showMinimized()
    def cambiarTab(self, pos):
        estilos = [ "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0288d1 , stop:.2 #1976d2);",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #43a047  , stop:.2 #388e3c);",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #9e9e9e , stop:.2 #888888);"]
        resto = "#top{%s}"
        self.ui.top.setStyleSheet(resto%(estilos[pos]))
        print pos
    def resetFiltro(self, data):
        self.ui.filtrarEmpresaComboBox.setCurrentIndex(0)
        print data
    def escanear(self):
        self.statusBar().showMessage(self.sender().text() + ' was pressed')
        if( self.sender().objectName()  == "escanearCompra"):
            my_dialog = EscanearModal(0) 
        elif( self.sender().objectName()  == "escanearVenta"):
            my_dialog = EscanearModal(1) 
    def exportar(self):
        self.statusBar().showMessage(self.sender().text() + ' was pressed')
        # Opciones
        correlativo = self.ui.correlativoSpinBox.value()
        contabilizar = self.ui.contabilizarCheckBox.isChecked()
        guardar = self.ui.guardarCheckBox.isChecked()
        print "Corr: %d cont: %s Guardar: %s"%(correlativo, contabilizar, guardar)
        archivo = QtGui.QFileDialog.getSaveFileName(self, directory=(os.path.expanduser("~/Documents/")+"Facturas.xlsx"), filter="Microsoft Excel (*.xlsx)")
        print "Guardando archivo %s"%archivo
        self.statusBar().showMessage("Archivo exportado en %s"%archivo)
    def clicked(self, position):
        if(self.sender().rowCount()==0): # Ninguna fila en la tabla
            return
        tabla = self.sender()
        menu = QtGui.QMenu()
        editarAction = menu.addAction("Editar")
        eliminarAction = menu.addAction("Eliminar")
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
                datos[ str(tabla.horizontalHeaderItem(i).text()).replace("Rut ", "")] =  tabla.item(row,i).text()
                print "[%s]: %s"%( str(tabla.horizontalHeaderItem(i).text()).replace("Rut ", "") , tabla.item(row,i).text())
            if(self.sender().objectName()=="tableWidget_Ventas"):
                my_dialog = AgregarDocumentoModal(1, datos ) 
            else:
                y_dialog = AgregarDocumentoModal(0, datos ) 
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
                    print [ "[%s]: %s"%( str(tabla.horizontalHeaderItem(i).text()).replace("Rut ", "") , tabla.item(idx.row(),i).text()) for i in range(tabla.horizontalHeader().count())]
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
        
    def filtrar(self, data):
        tabla = self.ui.tableWidget_Compras
        if(self.ui.tabWidget_2.currentIndex()==1):
            tabla = self.ui.tableWidget_Ventas
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