import sys
from PyQt4 import QtGui, QtCore
from sys import exit
from GUI.mainWindow import *
from GUI.escanearDialog import *
from GUI.nuevoDocumentoDialog import Ui_Dialog as Ui_Dialog_nuevoDocumento
from GUI.editarDocumentoDialog import Ui_Dialog as Ui_Dialog_editarDocumento
import math
from lecturacodigo.devices import lectorDevice
from lecturacodigo.reader import *
from lecturacodigo import xmlLib as XML
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

lector = None
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
        self.ui.fechaDateEdit.setDisabled(False)
        if(self.datos["Fecha"] == None):
            self.ui.fechaDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.fechaDateEdit.setDisabled(False)
        else:
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
        #if(self.datos["Tipo Documento"] == "34"):
        #    self.ui.montoExcentoSpinBox.setValue(float(self.datos["Monto Total"]))
        self.ui.montoExcentoSpinBox.setMaximum(int(self.datos["Monto Total"]))


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
        print "FECHA!!!!!!", self.datos["Fecha"]
        if(self.datos["Fecha"] == None):
            self.ui.fechaDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.fechaDateEdit.setReadOnly(False)
            
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Advertencia')
            qm.setText('''La fecha no pudo ser encontrada, debe ingresar \nla fecha correcta en el campo correspondiente''')
            qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
            qm.setIcon(QtGui.QMessageBox.Warning)
            reply = qm.exec_()
            
            
        else:
            self.ui.fechaDateEdit.setDate(QtCore.QDate.fromString(self.datos["Fecha"], "yyyy-MM-dd"))
        self.ui.glosaLineEdit.setFocus()
        
        if(self.tipo == 0):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11070100")
        elif(self.tipo == 1):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11040100")
        if(self.datos["Tipo Documento"] == "34"):
            self.ui.montoExcentoSpinBox.setValue(float(self.datos["Monto Total"]))
        print "LLENANDO: ",self.datos
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
        self.ser = LecturaController.iniciarReader(self, window.device)
        self.exec_()
    def terminar(self):
        print "Terminado por usuario"
        self.ser.close()
        self.accept()
    def terminado(self):
        print "Terminando thread"
    def enc(self, data, disp):
        try:
            xmlp = XML.XMLprocessor(data)
            print xmlp.TD, xmlp.F, xmlp.RS, xmlp.RSR
            datos = {}
            datos["Numero Documento"] = str(xmlp.F)
            datos["Rut Emisor"] = str(xmlp.RE)
            datos["Rut Receptor"] = str(xmlp.RR)
            datos["RS Emisor"] = str(xmlp.RS)
            datos["RS Receptor"] = str(xmlp.RSR)
            try:
                datos["Fecha"] = xmlp.FE
            except Exception as e:
                datos["Fecha"] = None
                # Mostrar modal
                print "Fecha mala: ", e
            datos["Monto Total"] = str(xmlp.MNT)
            datos["Tipo Documento"] = str(xmlp.TD)
            self.encontrado(datos)
        except Exception as e:
            # Modal
            print "mensaje codigo no valido: ", e
        #disp.close()
        print "SENAL", data
    def encontrado(self, datos):
        #Codigo encontrado, mostrar nuevo escanearDialog
        #self.thread.parar = True
        print "DATOSSSS!!!!",datos
        if(DBController.existeFactura(self.tipo, datos)):
            print "La factura ya existe!!!"
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Advertencia')
            qm.setText('''Esta factura ya ha sido ingresada.''')
            qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
            qm.setIcon(QtGui.QMessageBox.Warning)
            reply = qm.exec_()
            
            #if reply == QtGui.QMessageBox.Yes:
                # Eliminar de la base de datos
             #   print "Editar Dilog!!!"
        else:
            agregar = AgregarDocumentoModal(self.tipo, datos)
            if(agregar.resultado):
                self.window.updateTablas()
            else:
                print "CANCELANDO!!!!!"
            self.ser.open()
            
# Ventana Principal 
class MainWindow(QtGui.QMainWindow):
    _resized=False
    _prev_width=670
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        # Inicializar Ventana
        self.escanear_slot = self.escanear
        self.exportar_slot = self.exportar
        self.cambiarTab_slot = self.cambiarTab
        self.buscar_slot = self.buscarDevices
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
        self.ui.maximize_btn.mouseReleaseEvent = self.maximizar
        self.ui.resize_btn.mouseReleaseEvent = self.restaurar
        self.ui.labelClose.mousePressEvent = self.cerrar
        self.ui.labelMinimize.mouseReleaseEvent = self.minimizar
        self.moving = False
        self.ui.frame.mousePressEvent = self._mousePressEvent
        self.ui.frame.mouseMoveEvent = self._mouseMoveEvent
        self.ui.frame.mouseReleaseEvent = self._mouseReleaseEvent
        self.ui.tabWidget_4.tabBar().mousePressEvent = self._mousePressEvent
        self.ui.tabWidget_4.tabBar().mouseMoveEvent = self._mouseMoveEvent
        self.ui.resize_btn.hide()
        
        # Loading Spinner
        movie = QtGui.QMovie(":/newPrefix/loading.gif")
        self.ui.label_5.setMovie(movie)
        movie.start()
        self.ui.label_5.setLayout(QtGui.QHBoxLayout())
        self.ui.label_5.layout().addWidget(QtGui.QLabel(''))

        LecturaController.iniciarDevice(self)
        
        self.show()
    def buscarDevices(self):
        LecturaController.iniciarDevice(self)
    def deviceEncontrado(self, device):
        self.device = device
        self.ui.escanearCompra.setEnabled(True)
        self.ui.escanearVenta.setEnabled(True)
        self.ui.pushButtonDevice.setEnabled(True)
        # device.device_list -> spinBox
        self.ui.statusbar.clearMessage()
        self.ui.label_5.hide()
        self.ui.dispositivosComboBox.setEnabled(True)
        print "Dispositivos: ", device.device_list
        self.ui.dispositivosComboBox.addItem(device.device_list[0]["frendly_name"])
        for d in device.device_list:
            self.ui.dispositivosComboBox.addItem(d["frendly_name"])
        print "ENCONTRADOOOO !!!!!"
    def deviceCambiado(self):
        pass
    def deviceNoEncontrado(self):
        qm = QtGui.QMessageBox(self)
        qm.setWindowTitle('Advertencia')
        qm.setText('''No se ha encontrado ningun lector soportado''')
        qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
        qm.setIcon(QtGui.QMessageBox.Warning)
        self.ui.statusbar.clearMessage()
        self.ui.escanearCompra.setEnabled(False)
        self.ui.escanearVenta.setEnabled(False)
        self.ui.pushButtonDevice.setEnabled(True)
        self.ui.label_5.hide()
        reply = qm.exec_()
    def cerrar(self, data):
        print "Cerrars"
        self.close()
    def restaurar(self, data):
        print "Maximize"
        self.ui.maximize_btn.show();self.ui.resize_btn.hide()#toggle
        self.showNormal()
    def maximizar(self, data):
        print "Maximize"
        height = QtGui.QDesktopWidget().availableGeometry().bottom()
        width = QtGui.QDesktopWidget().availableGeometry().right()
        self._prev_width=self.width()
        self.ui.maximize_btn.hide();self.ui.resize_btn.show()#toggle
        self.showMaximized()
        self.resize(width, height)
        self.showMaximized()
        self.resize(self.width(), height)
    def minimizar(self, data):
        print "Minimize"
        self.ui.labelMinimize.repaint()
        
        self.showMinimized()
    def cambiarTab(self, pos):
        #self.overlay.parar()
        estilos = [ "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(2, 136, 209, 230) , stop:.2 rgba(25, 118, 210, 250));",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(67, 160, 71, 230)  , stop:.2 rgba(56, 142, 60, 250));",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(158, 158, 158, 230) , stop:.2 rgba(136, 136, 136, 250));"]
        resto = "#top{%s border-top-left-radius:3px; border-top-right-radius: 3px;}"
        self.ui.top.setStyleSheet(resto%(estilos[pos]))
        print pos
    def resetFiltro(self, data):
        
        print data
    def escanear(self):
        print "ESCANEAR", self.sender().objectName() 
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
        contabilizar = 0
        for idx in reversed(tabla.selectionModel().selectedRows()):
            print "CONTABILIZADO: ",tabla.item(idx.row(),0).text()
            if(tabla.item(idx.row(),0).text()=="No"):
                contabilizar = 1
                break
        contabilizarAction = None
        if(contabilizar):
            contabilizarAction = menu.addAction("Contabilizar")
        else:
            contabilizarAction = menu.addAction("Descontabilizar")
        action = menu.exec_(tabla.viewport().mapToGlobal(position))
        print "item clickeado: %s"%tabla.rowAt(position.y())
        row = tabla.rowAt(position.y())
        allRows = tabla.columnCount()
        
        if action == contabilizarAction:
            print "Contabilizars: ",contabilizar
            lista = []
            for idx in reversed(tabla.selectionModel().selectedRows()):
                datos = {}
                for i in range(tabla.horizontalHeader().count()):
                    datos[ str(tabla.horizontalHeaderItem(i).text())] =  str(tabla.item(idx.row(),i).text())
                lista.append(datos)
            if(self.sender().objectName()=="tableWidget_Ventas"):
                DBController.contabilizar(self, 1,contabilizar, lista)
            else:
                DBController.contabilizar(self, 0,contabilizar, lista)
        elif action == editarAction:
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
        elif action == eliminarAction:
            # TODO: Si se seleccionan varias columnas, eliminarlas todas
            # TODO: lanzar evento al oprimir suprimir,
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Eliminar documento')
            if( len(tabla.selectionModel().selectedRows()) == 1):
                qm.setText("Esta seguro de que desea eliminar el documento ?")
            else:
                qm.setText("Esta seguro de que desea eliminar los %d documentos ?"%len(tabla.selectionModel().selectedRows()))
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
        if self.moving: 
            if self.isMaximized():
                print 'event.globalPos().x : %d'%event.globalPos().x()
                print '>offset.x : %d'%(self._prev_width/2)
                if (self._prev_width/2)<self.offset.x():
                    diferencia = 0 
                    if (event.globalPos().x()+self._prev_width/2)>QtGui.QDesktopWidget().availableGeometry().right():
                        diferencia = (event.globalPos().x()+self._prev_width/2-QtGui.QDesktopWidget().availableGeometry().right())
                    self.offset = QtCore.QPoint(self._prev_width/2+diferencia,self.offset.y())
                #self.x = event.globalPos().x() - self._prev_width/2
                self.showNormal()
                print 'W : %d '%(event.globalPos().x() - self.width()/2)
                self._drop_top=False
                self._drop_left=False
                self._drop_right=False
                self._resized=False
                self.ui.maximize_btn.show();self.ui.resize_btn.hide()#toggle
            elif self._resized:
                self.resize(self._prev_width, self._prev_height)
                self._resized=False
            elif event.globalPos().y()==0:#caso ventana a top
                self._drop_top=True
                self._drop_left=False
                self._drop_right=False
            elif event.globalPos().x()==0:#caso ventana a la izquierda
                self._drop_top=False
                self._drop_left=True
                self._drop_right=False
            elif event.globalPos().x()==QtGui.QDesktopWidget().availableGeometry().right():#caso ventana a la derecha
                self._drop_top=False
                self._drop_left=False
                self._drop_right=True
            else:
                self._drop_top=False
                self._drop_left=False
                self._drop_right=False
            #no deberia dejar mover debajo del menu de inicio
            if event.globalPos().y()<QtGui.QDesktopWidget().availableGeometry().bottom():
                self.move(event.globalPos()-self.offset)
            #print event.globalPos().x()
    def _mouseReleaseEvent(self,event):
        if self._drop_top:
            height = QtGui.QDesktopWidget().availableGeometry().bottom()
            width = QtGui.QDesktopWidget().availableGeometry().right()
            self._prev_width=self.width()
            self.showMaximized()
            self.resize(width, height)
            self.showMaximized()
            self.resize(width, height)
            self.move(QtCore.QPoint(0,0))
            self.ui.maximize_btn.hide();self.ui.resize_btn.show()#toggle
            self._drop_top=False
        elif self._drop_left:
            height = QtGui.QDesktopWidget().availableGeometry().bottom()
            width = QtGui.QDesktopWidget().availableGeometry().right()
            self.move(QtCore.QPoint(0,0))
            self._prev_width=self.width(); self._prev_height=self.height()
            self.resize(width/2, height)
            self._resized=True
        elif self._drop_right:
            height = QtGui.QDesktopWidget().availableGeometry().bottom()
            width = QtGui.QDesktopWidget().availableGeometry().right()
            self.move(QtCore.QPoint(width/2,0))
            self._prev_width=self.width(); self._prev_height=self.height()
            self.resize(width/2, height)
            self._resized=True
    def isMaximized(self):
        height = QtGui.QDesktopWidget().availableGeometry().bottom()
        width = QtGui.QDesktopWidget().availableGeometry().right()
        return self.height()==height and self.width()==width
    def resizeEvent(self, event):
        #self.overlay.resize(event.size())
        event.accept()
        
class Overlay(QtGui.QWidget):

    def __init__(self, parent = None):
    
        QtGui.QWidget.__init__(self, parent)
        palette = QtGui.QPalette(self.palette())
        palette.setColor(palette.Background, QtCore.Qt.transparent)
        self.setPalette(palette)
        self.mostrando = False
        self.hide()
    def paintEvent(self, event):
    
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(255, 255, 255, 127)))
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        
        for i in range(6):
            if (self.counter / 5) % 6 == i:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(127 + (self.counter % 5)*32, 127, 127)))
            else:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(127, 127, 127)))
            painter.drawEllipse(
                event.rect().width()/2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
                event.rect().height()/2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
                20, 20)
        
        painter.end()
    
    def showEvent(self, event):
        self.timer = self.startTimer(50)
        self.counter = 0
    def parar(self):
        self.mostrando = False
        self.counter = 590
        self.killTimer(self.timer)
        self.hide()
    def timerEvent(self, event):
    
        self.counter += 1
        self.update()
        if self.counter == 600:
            self.killTimer(self.timer)
            self.hide()
            self.mostrando = False

    def mostrar(self):
        if(not self.mostrando):
            self.show()
            self.mostrando = True
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()