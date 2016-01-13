# -*- coding: utf-8 -*-
#arreglar lo de monto Total --
#checkbox de activo fijo --
    #tirar el dato de activofijo al crear la factura
 #actualizar el lector para leer la pistola, luego de que se ha ingresado una repetida --
import sys
from PyQt4 import QtGui, QtCore
from sys import exit
from GUI.mainWindow import *
from GUI.escanearDialog import *
from GUI.nuevoDocumentoDialog import Ui_Dialog as Ui_Dialog_nuevoDocumento
from GUI.editarDocumentoDialog import Ui_Dialog as Ui_Dialog_editarDocumento
from GUI.login import Ui_Dialog as Ui_Dialog_login
from GUI.editarConfig import Ui_Dialog as Ui_Dialog_config
import math
from lecturacodigo.devices import lectorDevice
from lecturacodigo.reader import *
from lecturacodigo import xmlLib as XML
import LecturaController
import DBController
import ActivacionController
from instance import *#para el manejo de multiples instancias
import os,time
from random import randint
import traceback
# Para que no use el icono de python
import ctypes
myappid = 'BTE.lector.gui.estable' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#----------------------------------- --- Vistas ------------------------------------ 
# TODO: escrbiendo
# aisjdaojsijd

#       asdasd
# Modal para Agregar documento
debug = False
import sys
#sys.stderr = open('%s\\CAMDE\\log.txt' %  os.environ['APPDATA'], 'w')#sys.stdout
if not Instance.verificar('main'):#cambiar 
    Instance.traeralfrente()
    exit(0) # Existe la instancia

class ConfigModal(QtGui.QDialog):
    
    def __init__(self, empresa):
        super(ConfigModal, self).__init__()
        self.ui=Ui_Dialog_config()
        self.reject_slot = self.cancelar
        self.accept_slot = self.aceptar
        self.ui.setupUi(self)
        self.resultado = False
        self.empresa = empresa
        self.ui.labelTitulo.setText("Editar Empresa " + empresa[0] + " " +empresa[1])
        self.exec_()
    def aceptar(self):
        self.close()
    def cancelar(self):
        self.close()
class LoginModal(QtGui.QDialog):
    
    def __init__(self):
        super(LoginModal, self).__init__()
        self.ui=Ui_Dialog_login()
        self.changed_slot = self.verificar
        self.ui.setupUi(self)
        self.resultado = False
        movie = QtGui.QMovie(":/newPrefix/loading.gif")
        self.ui.spinnerLabel.setMovie(movie)
        movie.start()
        self.ui.spinnerLabel.setLayout(QtGui.QHBoxLayout())
        self.ui.spinnerLabel.layout().addWidget(QtGui.QLabel(''))
        self.ui.spinnerLabel.hide()
        self.ui.mensajeLabel.hide()
        self.redimensionar()
        self.ui.enviarPushButton.setEnabled(False)
        self.exec_()
    def activado(self):
        self.resultado = True
        self.close()
    def rechazado(self):
        self.reject()
        # Mostrar mensaje error
    def verificar(self, text):
        passw = self.ui.passwordLineEdit.text()
        user = self.ui.mailLineEdit.text()
        if(ActivacionController.verificarUser(user) and ActivacionController.verificarPassword(passw) ):
            self.ui.enviarPushButton.setEnabled(True)
        else:
            self.ui.enviarPushButton.setEnabled(False)
    def redimensionar(self):
        s = self.sizeHint()
        s.setWidth(self.width())
        self.resize(s);
    def estado(self, mensaje):
        self.ui.mensajeLabel.setText(mensaje)
    def accept(self):
        passw = self.ui.passwordLineEdit.text()
        user = self.ui.mailLineEdit.text()
        self.ui.enviarPushButton.setEnabled(False)
        self.ui.spinnerLabel.show()
        self.ui.mensajeLabel.show()
        self.redimensionar()
        ActivacionController.iniciar(self, user, passw)
        
class EditarDocumentoModal(QtGui.QDialog):
    
    def __init__(self, tipo, datos):
        super(EditarDocumentoModal, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
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
        self.f = fac = DBController.getFactura(datos, tipo)
        rx = QtCore.QRegExp("[0-9]*")
        qr = QtGui.QRegExpValidator(rx)
        
        self.ui.nDocumentoLineEdit.setValidator( qr )
        self.ui.sucursalLineEdit.setValidator( qr)
        self.ui.correlativoLineEdit.setValidator( qr )
        self.ui.cuentaProveedoresClienteLineEdit.setValidator( qr )
        self.ui.contracuentaLineEdit.setValidator( qr )
        
        self.datos = datos
        self.llenarDatos()
        self.resultado = False
        self.exec_()
    def accept(self):
        self.datos["Numero Documento"] = unicode(self.ui.nDocumentoLineEdit.text())
        self.datos["RS Emisor"] = unicode(self.ui.emisorLineEdit.text())
        self.datos["RS Receptor"] = unicode(self.ui.receptorLineEdit.text())
        self.datos["Fecha"] = unicode(self.ui.fechaDateEdit.text())
        self.datos["Sucursal"] =unicode( self.ui.sucursalLineEdit.text())
        self.datos["Glosa"] = unicode(self.ui.glosaLineEdit.text())
        self.datos["Monto Exento"] = unicode(self.ui.montoExcentoSpinBox.value())
        self.datos["Cuenta"] = unicode(self.ui.cuentaProveedoresClienteLineEdit.text())
        self.datos["Contracuenta"] = unicode(self.ui.contracuentaLineEdit.text())
        self.datos["Correlativo"] = unicode(self.ui.correlativoLineEdit.text())
        if(self.ui.activoFijoCheckBox.checkState () == QtCore.Qt.Checked):
            self.datos["Activo Fijo"] = 1
        else:
            self.datos["Activo Fijo"] = 0
        # Si uno de los datos esta vacio
        # TODO: Cambiar color al encontrar error
        fallas = []
        for key, value in self.datos.items():
            if(not ("%s"%value)):
                fallas.append(key)
        error = ""
        for i in fallas:
            error = error+"%s\n"%i
        if(len(fallas)!=0):
            QtGui.QMessageBox.about(self, "Datos incompletos", "Faltan datos a ingresar en los siguientes campos:\n%s"%error)
        else:
            # Guardando
            DBController.modificarFactura(self.f, self.datos, self.tipo)
            self.resultado = True
            self.close()
    def llenarDatos(self):
        self.ui.montoExcentoSpinBox.setMaximum(2**53)
        self.ui.correlativoLineEdit.setText(self.datos["Correlativo"])
        self.ui.cuentaProveedoresClienteLineEdit.setText(self.datos["Cuenta"])
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
        self.ui.contracuentaLineEdit.setText(self.datos["Contracuenta"])
        
        self.ui.activoFijoCheckBox.setCheckState(QtCore.Qt.Unchecked)
        if(self.datos["Activo Fijo"] == "Si"):
            self.ui.activoFijoCheckBox.setCheckState(QtCore.Qt.Checked)
        
        self.ui.montoTotalLabel.setText("$ %s"%self.datos["Monto Total"])
        self.ui.montoExcentoSpinBox.setMaximum(int(self.datos["Monto Total"]))


class AgregarDocumentoModal(QtGui.QDialog):
    
    def __init__(self, tipo, datos):
        super(AgregarDocumentoModal, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
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

        rx = QtCore.QRegExp("[0-9]*")
        qr = QtGui.QRegExpValidator(rx)
        self.ui.sucursalLineEdit.setValidator( qr )

        self.ui.cuentaProveedoresClienteLineEdit.setValidator( qr )
        self.ui.contracuentaLineEdit.setValidator( qr )
        self.ui.correlativoLineEdit.setValidator( qr)
        
        self.datos = datos
        self.llenarDatos()
        self.resultado = False
        self.exec_()
        
    def accept(self):
        # Datos
        # Limitar a numeros o alfanumerico
        
        self.datos["Numero Documento"] = unicode(self.ui.labelNDocumento.text())
        self.datos["RS Emisor"] = unicode(self.ui.labelEmisor.text())
        self.datos["RS Receptor"] = unicode(self.ui.labelReceptor.text())
        self.datos["Fecha"] = unicode(self.ui.fechaDateEdit.text())
        self.datos["Sucursal"] =unicode( self.ui.sucursalLineEdit.text())
        self.datos["Glosa"] = unicode(self.ui.glosaLineEdit.text())
        self.datos["Monto Exento"] = unicode(self.ui.montoExcentoSpinBox.value())
        self.datos["Cuenta"] = unicode(self.ui.cuentaProveedoresClienteLineEdit.text())
        self.datos["Contracuenta"] = unicode(self.ui.contracuentaLineEdit.text())
        self.datos["Correlativo"] = unicode(self.ui.correlativoLineEdit.text())
        if(self.ui.activoFijoCheckBox.checkState () == QtCore.Qt.Checked):
            self.datos["Activo Fijo"] = 1
        else:
            self.datos["Activo Fijo"] = 0
        # Si uno de los datos esta vacio
        # TODO: Cambiar color al encontrar error
        fallas = []
        for key, value in self.datos.items():
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
            self.ui.cuentaProveedoresClienteLineEdit.setText("21070100")
        elif(self.tipo == 1):
            self.ui.cuentaProveedoresClienteLineEdit.setText("11040100")
        self.llenarUltima()
        self.ui.montoTotalLabel.setText("$ %s"%self.datos["Monto Total"])
        self.ui.labelNDocumento.setText(self.datos["Numero Documento"])
        self.ui.labelEmisor.setText(self.datos["RS Emisor"])
        self.ui.labelReceptor.setText(self.datos["RS Receptor"])

        if(self.datos["Fecha"] == None):
            self.ui.fechaDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.fechaDateEdit.setReadOnly(False)
            self.ui.fechaDateEdit.setFocus()
            
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Advertencia')
            qm.setText('''La fecha no pudo ser encontrada, debe ingresar \nla fecha correcta en el campo correspondiente''')
            qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
            qm.setIcon(QtGui.QMessageBox.Warning)
            reply = qm.exec_()
        else:
            self.ui.fechaDateEdit.setDate(QtCore.QDate.fromString(self.datos["Fecha"], "yyyy-MM-dd"))
            self.ui.contracuentaLineEdit.setFocus()
        
        if(self.datos["Tipo Documento"] == "34"):
            self.ui.montoExcentoSpinBox.setValue(float(self.datos["Monto Total"]))
            self.ui.montoExcentoSpinBox.setReadOnly(True)

        self.ui.activoFijoCheckBox.setCheckState(QtCore.Qt.Unchecked)
        if(self.datos["Activo Fijo"]):
            self.ui.activoFijoCheckBox.setCheckState(QtCore.Qt.Checked)
        
        self.ui.montoExcentoSpinBox.setMaximum(int(self.datos["Monto Total"]))
        
    def llenarUltima(self):
        
        fact = DBController.ultimaFactura(self.datos["Rut Emisor"])
        if(fact):
            self.datos["Sucursal"] = unicode(fact.sucursal)
            self.datos["Cuenta"] = unicode(fact.cuentaProveedores)
            self.datos["Glosa"] = unicode(fact.Glosa)
            self.datos["Contracuenta"] = unicode(fact.contracuenta)
            self.datos["Activo Fijo"] = fact.activoFijo
            self.datos["RS Emisor"] = fact.empresaEmisor.rS
            self.datos["RS Receptor"] = fact.empresaReceptor.rS
            self.ui.sucursalLineEdit.setText(self.datos["Sucursal"])
            self.ui.glosaLineEdit.setText(self.datos["Glosa"])
            self.ui.contracuentaLineEdit.setText(self.datos["Contracuenta"])
            self.ui.cuentaProveedoresClienteLineEdit.setText(self.datos["Cuenta"])
        
# Modal para escanear codigo
class EscanearModal(QtGui.QDialog):
    def __init__(self, tipo, window):
        super(EscanearModal, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui=Ui_Dialog()
        self.encontrado_slot = self.encontrado
        self.reject = self.terminar
        self.tipo = tipo
        self.window = window
        self.ui.setupUi(self)
        self.ui.estadoLabel.setText("Estado: Listo")
        self.ser = LecturaController.iniciarReader(self, window.device)
        
        self.exec_()
    def terminar(self):
        self.ser.close()
        self.accept()
    def terminado(self):
        pass
    def error(self):
        self.window.ui.escanearCompra.setEnabled(False)
        self.window.ui.escanearVenta.setEnabled(False)
        self.window.ui.dispositivosComboBox.clear()
        self.window.ui.dispositivosComboBox.setEnabled(False)
        qm = QtGui.QMessageBox(self)
        qm.setWindowTitle('Advertencia')
        qm.setText('''No se ha encontrado ningun lector soportado''')
        qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
        qm.setIcon(QtGui.QMessageBox.Warning)
        reply = qm.exec_()
        self.close()
    def codError(self, d):
        self.ui.estadoLabel.setText("Estado: El codigo no es legible")
        self.window.zumbido(self)
        self.ser.open()
    def enc(self, data, disp):
        self.ui.estadoLabel.setText("Estado: Factura encontrada")
        try:
            xmlp = XML.XMLprocessor(data)
            datos = {}
            datos["Numero Documento"] = unicode(xmlp.F)
            datos["Rut Emisor"] = unicode(xmlp.RE)
            datos["Rut Receptor"] = unicode(xmlp.RR)
            datos["RS Emisor"] = unicode(xmlp.RS)
            datos["RS Receptor"] = unicode(xmlp.RSR)
            datos["Activo Fijo"] = 0
            try:
                datos["Fecha"] = xmlp.FE
            except Exception as e:
                datos["Fecha"] = None
                # Mostrar modal
            datos["Monto Total"] = unicode(xmlp.MNT)
            datos["Tipo Documento"] = unicode(xmlp.TD)
            self.encontrado(datos)
        except Exception as e:
            traceback.print_exc()
            
            # Modal
            self.ui.estadoLabel.setText("Estado: El codigo no es legible")
            self.ser.open()            
            self.window.zumbido(self)
        #disp.close()
    def encontrado(self, datos):
        #Codigo encontrado, mostrar nuevo escanearDialog
        #self.thread.parar = True
        if(DBController.existeFactura(self.tipo, datos)):
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Advertencia')
            qm.setText('''Esta factura ya ha sido ingresada.''')
            qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
            qm.setIcon(QtGui.QMessageBox.Warning)
            reply = qm.exec_()
            self.ser.open()
            self.ui.estadoLabel.setText("Estado: Listo")
            #if reply == QtGui.QMessageBox.Yes:
                # Eliminar de la base de datos
             #   print "Editar Dilog!!!"
        else:
            agregar = AgregarDocumentoModal(self.tipo, datos)
            if(agregar.resultado):
                self.window.updateTablas()
            else:
                pass
            self.ui.estadoLabel.setText("Estado: Listo")
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
        self.correlativo_changed_slot = self.correlativoChanged
        self.buscar_slot = self.buscarDevices
        self.config_slot = self.configDialog
        self.filtrar_slot = self.filtrar
        self.deshacer_slot = self.deshacer
        self.rehacer_slot = self.rehacer
        self.respaldar_slot = self.backup
        self.restaurar_slot = self.restaurarDB
        self.filtrarFecha_slot = self.filtrarFecha
        self.dispositivoChange_slot = self.cambiarDispositivo
        self.documentoCambiarTab_slot = self.resetFiltro
        self.empresas = [["Todas", ""]]
        self.fechas = [["Todo", None, None]]
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.tableWidget_Compras.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableWidget_Compras.customContextMenuRequested.connect(self.clicked)
        self.ui.tableWidget_Ventas.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableWidget_Ventas.customContextMenuRequested.connect(self.clicked)
        
        self.inicializarDatos(self.ui.tableWidget_Compras)
        self.inicializarDatos(self.ui.tableWidget_Ventas)
        self.updateEmpresas()
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
        self.ui.rehacerToolButton.setEnabled(False)
        self.ui.deshacerToolButton.setEnabled(False)
        
        rx = QtCore.QRegExp("^[1-9][0-9]*|^$")
        qr = QtGui.QRegExpValidator(rx)
        
        self.ui.codigoLineEdit.setValidator( qr )
        self.ui.centroLineEdit.setValidator( qr )
        # Loading Spinner
        movie = QtGui.QMovie(":/newPrefix/loading.gif")
        self.ui.label_5.setMovie(movie)
        movie.start()
        self.ui.label_5.setLayout(QtGui.QHBoxLayout())
        self.ui.label_5.layout().addWidget(QtGui.QLabel(''))

        LecturaController.iniciarDevice(self)
        
        self.show()
    def configDialog(self):
        my_dialog = ConfigModal(self.empresas[self.ui.filtrarEmpresaComboBox.currentIndex()])
    def restaurarDB(self):
        path = QtGui.QFileDialog.getOpenFileName(self, directory=(os.path.expanduser("~/Documents/")+"dump.sql"), filter="Sql Script (*.sql)")
        if(path!=""):
            if(DBController.verificar(path)):
                # Mensaje
                qm = QtGui.QMessageBox(self)
                qm.setWindowTitle('Advertencia')
                qm.setText(QtCore.QString(u"Al restaurar la base de datos se perderán todos los datos ingresados posterior al respaldo.\nEstá seguro de que desea realizar esta operación?"))
                qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
                qm.addButton(QtGui.QMessageBox.No).setText("Cancelar")
                qm.setIcon(QtGui.QMessageBox.Warning)
                reply = qm.exec_()
                if reply == QtGui.QMessageBox.Yes:
                    DBController.restaurar(path)
                    self.updateTablas()
                    self.mensaje("Base de datos restaurada desde %s"%path)
                    
    def mensaje(self,mensaje):
        self.ui.statusbar.showMessage(mensaje)
        QtCore.QTimer.singleShot(4000, self.ui.statusbar.clearMessage)

    def backup(self):
        path = QtGui.QFileDialog.getSaveFileName(self, directory=(os.path.expanduser("~/Documents/")+"dump.sql"), filter="Sql Script (*.sql)")
        if(path!=""):
            try:
                DBController.backup(path)
                #raise Exception("OIADIOASIOHDS")
            except Exception as e:
                traceback.print_exc()
            self.mensaje("Base de datos respaldada en %s"%path)
    def rehacer(self):
        DBController.contabilizarFacturas(self.contabilizados, not self.cambiarContabilizados)
        self.ui.rehacerToolButton.setEnabled(False)
        self.ui.deshacerToolButton.setEnabled(True)
        self.updateTablas()
    def deshacer(self):
        DBController.contabilizarFacturas(self.contabilizados, self.cambiarContabilizados)
        self.ui.deshacerToolButton.setEnabled(False)
        self.ui.rehacerToolButton.setEnabled(True)
        self.updateTablas()
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
        self.ui.dispositivosComboBox.clear()
        self.ui.dispositivosComboBox.setEnabled(True)
        for d in device.device_list:
            self.ui.dispositivosComboBox.addItem(d["frendly_name"])
    def cambiarDispositivo(self, pos):
        self.device.device = pos
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
        self.close()
    def restaurar(self, data):
        self.ui.maximize_btn.show();self.ui.resize_btn.hide()#toggle
        self.showNormal()
    def maximizar(self, data):
        height = QtGui.QDesktopWidget().availableGeometry().bottom()
        width = QtGui.QDesktopWidget().availableGeometry().right()
        self._prev_width=self.width()
        self.ui.maximize_btn.hide();self.ui.resize_btn.show()#toggle
        self.showMaximized()
        self.resize(width, height)
        self.showMaximized()
        self.resize(self.width(), height)
    def minimizar(self, data):
        self.ui.labelMinimize.repaint()
        
        self.showMinimized()
    def cambiarTab(self, pos):
        estilos = [ "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(2, 136, 209, 230) , stop:.2 rgba(25, 118, 210, 250));",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(67, 160, 71, 230)  , stop:.2 rgba(56, 142, 60, 250));",
                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(158, 158, 158, 230) , stop:.2 rgba(136, 136, 136, 250));"]
        resto = "#top{%s border-top-left-radius:3px; border-top-right-radius: 3px;}"
        self.ui.top.setStyleSheet(resto%(estilos[pos]))
    def resetFiltro(self, data):
        pass
    def escanear(self):
        if( self.sender().objectName()  == "escanearCompra"):
            my_dialog = EscanearModal(0, self) 
            
        elif( self.sender().objectName()  == "escanearVenta"):
            my_dialog = EscanearModal(1, self) 
    def correlativoChanged(self):
        self.ui.correlativoDoubleSpinBox.value()
        if(self.ui.correlativoDoubleSpinBox.value() <= 0):
            self.ui.correlativoDoubleSpinBox.setValue(1)
    def exportar(self):
        # Opciones
        if(self.ui.filtrarEmpresaComboBox.currentIndex() == 0):
            qm = QtGui.QMessageBox(self)
            qm.setWindowTitle('Advertencia')
            qm.setText(u'¿Esta seguro de que desea exportar todas las facturas?')
            qm.addButton(QtGui.QMessageBox.Yes).setText("Si")
            qm.addButton(QtGui.QMessageBox.No).setText("No")
            qm.setIcon(QtGui.QMessageBox.Warning)
            reply = qm.exec_()
            if reply == QtGui.QMessageBox.No:
                return
        
        
        contabilizar = self.ui.contabilizarCheckBox.isChecked()
        guardar = self.ui.guardarCheckBox.isChecked()
        centro = self.ui.centroLineEdit.text() 
        especial = self.ui.codigoLineEdit.text()
        archivo = None
        correlativo = self.ui.correlativoDoubleSpinBox.value()
        if(self.sender().objectName() == "toolButtonPlano"):
            archivo = QtGui.QFileDialog.getSaveFileName(self, directory=(os.path.expanduser("~/Documents/")+"Facturas.tcv"), filter="Texto tcv (*.tcv)")
        else:    
            archivo = QtGui.QFileDialog.getSaveFileName(self, directory=(os.path.expanduser("~/Documents/")+"Facturas.xls"), filter="Microsoft Excel (*.xls)")
        if(archivo != ""):
            self.ui.deshacerToolButton.setEnabled(False)
            self.ui.rehacerToolButton.setEnabled(False)
            #TODO: try permiso de escritura 
            if(self.sender().objectName() != "toolButtonPlano"):
                month = self.fechas[self.ui.fechaComboBox.currentIndex()][1]
                year = self.fechas[self.ui.fechaComboBox.currentIndex()][2]
                print "YEYYEYE",year
                print "MJSAASD",month
                try:
                    if(contabilizar):
                        tablas = [self.ui.tableWidget_Compras, self.ui.tableWidget_Ventas]
                        self.contabilizados = []
                        self.cambiarContabilizados = False
                        for tabla in tablas:
                            allRows = tabla.rowCount()
                            for row in xrange(0,allRows):
                                c = unicode(tabla.item(row,0).text())
                                Id = unicode(tabla.item(row,tabla.horizontalHeader().count()-1).text())
                                if(c == "No"):
                                    self.contabilizados.append(int(Id))
                    DBController.exportarExcel(unicode(self.empresas[self.ui.filtrarEmpresaComboBox.currentIndex()][0]), archivo, contabilizar, guardar, month, year, correlativo, centro, especial)
                    print "WEWEWE"
                    
                    if(len(self.contabilizados)!=0):
                        #DBController.contabilizarFacturas(self.contabilizados, 1)
                        self.ui.deshacerToolButton.setEnabled(True)
                    self.updateTablas()
                    self.mensaje("Archivo exportado en: " + unicode(archivo))
                    
                    qm = QtGui.QMessageBox(self)
                    qm.setWindowTitle('Abrir archivo')
                    qm.setText("Exportado existosamente. Desea abrir el archivo?")
                    qm.addButton(QtGui.QMessageBox.Yes).setText("Si")
                    qm.addButton(QtGui.QMessageBox.No).setText("No")
                    qm.setIcon(QtGui.QMessageBox.Information)
                    reply = qm.exec_()
                    if reply == QtGui.QMessageBox.Yes:
                        os.startfile(unicode(archivo))
                    
                except:
                    traceback.print_exc()
                    qm = QtGui.QMessageBox(self)
                    qm.setWindowTitle('Error de escritura')
                    qm.setText("Se produjo un error al exportar el archivo, verifique que no tiene el archivo de salida abierto")
                    qm.addButton(QtGui.QMessageBox.Yes).setText("Aceptar")
                    qm.setIcon(QtGui.QMessageBox.Warning)
                    reply = qm.exec_()
                    DBController.contabilizarFacturas(self.contabilizados, False)



            
                

    def clicked(self, position):
        if(self.sender().rowCount()==0): # Ninguna fila en la tabla
            return
        tabla = self.sender()
        menu = QtGui.QMenu()
        editarAction = menu.addAction("Editar")
        eliminarAction = menu.addAction("Eliminar")
        contabilizar = 0
        for idx in reversed(tabla.selectionModel().selectedRows()):
            if(tabla.item(idx.row(),0).text()=="No"):
                contabilizar = 1
                break
        contabilizarAction = None
        if(contabilizar):
            contabilizarAction = menu.addAction("Contabilizar")
        else:
            contabilizarAction = menu.addAction("Descontabilizar")
        action = menu.exec_(tabla.viewport().mapToGlobal(position))
        row = tabla.rowAt(position.y())
        allRows = tabla.columnCount()
        
        if action == contabilizarAction:
            lista = []
            for idx in reversed(tabla.selectionModel().selectedRows()):
                datos = {}
                for i in range(tabla.horizontalHeader().count()):
                    datos[ unicode(tabla.horizontalHeaderItem(i).text())] =  unicode(tabla.item(idx.row(),i).text())
                lista.append(datos)
            if(self.sender().objectName()=="tableWidget_Ventas"):
                DBController.contabilizar(self, 1,contabilizar, lista)
            else:
                DBController.contabilizar(self, 0,contabilizar, lista)
        elif action == editarAction:
            datos = {}
            
            for i in range(tabla.horizontalHeader().count()):
                datos[ unicode(tabla.horizontalHeaderItem(i).text())] =  unicode(tabla.item(row,i).text())
            tipo = 0
            if(self.sender().objectName()=="tableWidget_Ventas"):
                tipo = 1
            fac = DBController.getFactura(datos, tipo)
            datos["Cuenta"] = fac.cuentaProveedores
            datos["Correlativo"] = unicode(fac.correlativo)
            my_dialog = EditarDocumentoModal(tipo, datos ) 
            if(my_dialog.resultado):
                self.updateTablas()
        elif action == eliminarAction:
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
                for idx in reversed(tabla.selectionModel().selectedRows()):
                    DBController.eliminarFactura(tabla.item(idx.row(),16).text())
                    tabla.removeRow(idx.row())

    def inicializarDatos(self, tabla):
        self.updateFechas()
        documentos = DBController.obtenerLista(tabla.objectName(), None, None, None)
        tabla.setRowCount(len(documentos))
        for i in range(len(documentos)):
            for j in range(len(documentos[i])):
                item = QtGui.QTableWidgetItem()
                item.setText(documentos[i][j])
                item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
                tabla.setItem(i, j, item) # QtGui.QTableWidgetItem(documentos[i][j])
        for i in range(tabla.verticalHeader().count()):
            tabla.verticalHeader().setResizeMode(i, QtGui.QHeaderView.Fixed)
        tabla.setColumnHidden(tabla.horizontalHeader().count()-1, True)
    def updateTablas(self):
        self.updateFechas()
        self.filtrar(self.ui.filtrarEmpresaComboBox.currentIndex())
        self.updateEmpresas()
        
    def updateFechas(self):
        self.ui.fechaComboBox.clear()
        self.fechas = DBController.obtenerFechas()
        for f in self.fechas:
            self.ui.fechaComboBox.addItem(f[0])
    def filtrarFecha(self, fechaData):
        self.filtrar(self.ui.filtrarEmpresaComboBox.currentIndex())
    def filtrar(self, data):
        if(self.ui.filtrarEmpresaComboBox.currentIndex() == 0):
            self.ui.editarEmpresaToolButton.setEnabled(False)
        else:
            self.ui.editarEmpresaToolButton.setEnabled(True)
        tablas = [self.ui.tableWidget_Compras, self.ui.tableWidget_Ventas]
        f = self.fechas[self.ui.fechaComboBox.currentIndex()]
        if data != "":
            for tabla in tablas:
                documentos = DBController.obtenerLista(tabla.objectName(), unicode(self.empresas[data][0]), f[1], f[2])

                tabla.clearContents()
                tabla.setRowCount(len(documentos))
                for i in range(len(documentos)):
                    for j in range(len(documentos[i])):
                        item = QtGui.QTableWidgetItem()
                        item.setText(documentos[i][j])
                        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
                        tabla.setItem(i, j, item) # QtGui.QTableWidgetItem(documentos[i][j])
                tabla.verticalHeader().setVisible(True)
                tabla.resizeColumnsToContents()

    def updateEmpresas(self):
        self.ui.filtrarEmpresaComboBox.clear()
        self.ui.filtrarEmpresaComboBox.addItem("Todas")
        self.empresas = []
        self.empresas.append(["Todas", ""])
        for e in DBController.getEmpresas():
            self.empresas.append(e)
            self.ui.filtrarEmpresaComboBox.addItem(e[0]+" | "+e[1])
    
    def _mousePressEvent(self,event):

        if event.button() == QtCore.Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def _mouseMoveEvent(self,event):
        if self.moving: 
            if self.isMaximized():
                if (self._prev_width/2)<self.offset.x():
                    diferencia = 0 
                    if (event.globalPos().x()+self._prev_width/2)>QtGui.QDesktopWidget().availableGeometry().right():
                        diferencia = (event.globalPos().x()+self._prev_width/2-QtGui.QDesktopWidget().availableGeometry().right())
                    self.offset = QtCore.QPoint(self._prev_width/2+diferencia,self.offset.y())
                self.showNormal()
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
    def _mouseReleaseEvent(self,event):
        if not hasattr(self, '_drop_top'):
            return
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
    def zumbido(self,dialog):
        point =dialog.pos()
        dialog.move(point-QtCore.QPoint(15,0))
        time.sleep(.03)
        dialog.move(point+QtCore.QPoint(15,0))
        time.sleep(.03)
        dialog.move(point-QtCore.QPoint(15,0))
        time.sleep(.03)
        dialog.move(point+QtCore.QPoint(15,0))
        time.sleep(.03)
        dialog.move(point)
        
def main():
    app = QtGui.QApplication(sys.argv)
    if(not debug):
        ex = MainWindow()
        sys.exit(app.exec_())
    if(ActivacionController.valido()):
        ex = MainWindow()
        sys.exit(app.exec_())
    else:
        login = LoginModal()
        if(login.resultado):
            ex = MainWindow()
            sys.exit(app.exec_())
        else:
            sys.exit()

if __name__ == '__main__':
    main()