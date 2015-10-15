# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\editarDocumentoDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(380, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(380, 400))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/document.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"    background:#fafafa\n"
"}\n"
"QLineEdit,QDateEdit,QDoubleSpinBox{\n"
"    padding:4px\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 8, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(40, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/document.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelTitulo = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.verticalLayout_3.addWidget(self.labelTitulo)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.nDocumentoLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nDocumentoLabel.setFont(font)
        self.nDocumentoLabel.setObjectName(_fromUtf8("nDocumentoLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.nDocumentoLabel)
        self.emisorLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emisorLabel.setFont(font)
        self.emisorLabel.setObjectName(_fromUtf8("emisorLabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.emisorLabel)
        self.receptorLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.receptorLabel.setFont(font)
        self.receptorLabel.setObjectName(_fromUtf8("receptorLabel"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.receptorLabel)
        self.fechaLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fechaLabel.setFont(font)
        self.fechaLabel.setObjectName(_fromUtf8("fechaLabel"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.fechaLabel)
        self.fechaDateEdit = QtGui.QDateEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.fechaDateEdit.setFont(font)
        self.fechaDateEdit.setReadOnly(True)
        self.fechaDateEdit.setObjectName(_fromUtf8("fechaDateEdit"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.fechaDateEdit)
        self.receptorLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.receptorLineEdit.setFont(font)
        self.receptorLineEdit.setReadOnly(True)
        self.receptorLineEdit.setObjectName(_fromUtf8("receptorLineEdit"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.receptorLineEdit)
        self.emisorLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.emisorLineEdit.setFont(font)
        self.emisorLineEdit.setInputMask(_fromUtf8(""))
        self.emisorLineEdit.setText(_fromUtf8(""))
        self.emisorLineEdit.setReadOnly(True)
        self.emisorLineEdit.setObjectName(_fromUtf8("emisorLineEdit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.emisorLineEdit)
        self.nDocumentoLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.nDocumentoLineEdit.setFont(font)
        self.nDocumentoLineEdit.setReadOnly(True)
        self.nDocumentoLineEdit.setObjectName(_fromUtf8("nDocumentoLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.nDocumentoLineEdit)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.line = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.line.setFont(font)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.sucursalLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sucursalLabel.setFont(font)
        self.sucursalLabel.setObjectName(_fromUtf8("sucursalLabel"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.sucursalLabel)
        self.glosaLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.glosaLabel.setFont(font)
        self.glosaLabel.setObjectName(_fromUtf8("glosaLabel"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.glosaLabel)
        self.sucursalLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.sucursalLineEdit.setFont(font)
        self.sucursalLineEdit.setObjectName(_fromUtf8("sucursalLineEdit"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sucursalLineEdit)
        self.glosaLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.glosaLineEdit.setFont(font)
        self.glosaLineEdit.setObjectName(_fromUtf8("glosaLineEdit"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.SpanningRole, self.glosaLineEdit)
        self.horizontalLayout.addLayout(self.formLayout_4)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.cuentaProveedoresClienteLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cuentaProveedoresClienteLabel.setFont(font)
        self.cuentaProveedoresClienteLabel.setObjectName(_fromUtf8("cuentaProveedoresClienteLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.cuentaProveedoresClienteLabel)
        self.cuentaProveedoresClienteLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.cuentaProveedoresClienteLineEdit.setFont(font)
        self.cuentaProveedoresClienteLineEdit.setObjectName(_fromUtf8("cuentaProveedoresClienteLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.cuentaProveedoresClienteLineEdit)
        self.contracuentaLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.contracuentaLabel.setFont(font)
        self.contracuentaLabel.setObjectName(_fromUtf8("contracuentaLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.contracuentaLabel)
        self.contracuentaLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.contracuentaLineEdit.setFont(font)
        self.contracuentaLineEdit.setObjectName(_fromUtf8("contracuentaLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.SpanningRole, self.contracuentaLineEdit)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.montoExcentoLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.montoExcentoLabel.setFont(font)
        self.montoExcentoLabel.setObjectName(_fromUtf8("montoExcentoLabel"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.montoExcentoLabel)
        self.montoExcentoSpinBox = QtGui.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.montoExcentoSpinBox.setFont(font)
        self.montoExcentoSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.montoExcentoSpinBox.setDecimals(0)
        self.montoExcentoSpinBox.setMaximum(1999999999.0)
        self.montoExcentoSpinBox.setObjectName(_fromUtf8("montoExcentoSpinBox"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.SpanningRole, self.montoExcentoSpinBox)
        self.verticalLayout_3.addLayout(self.formLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 8, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.nDocumentoLineEdit, self.emisorLineEdit)
        Dialog.setTabOrder(self.emisorLineEdit, self.receptorLineEdit)
        Dialog.setTabOrder(self.receptorLineEdit, self.fechaDateEdit)
        Dialog.setTabOrder(self.fechaDateEdit, self.sucursalLineEdit)
        Dialog.setTabOrder(self.sucursalLineEdit, self.cuentaProveedoresClienteLineEdit)
        Dialog.setTabOrder(self.cuentaProveedoresClienteLineEdit, self.glosaLineEdit)
        Dialog.setTabOrder(self.glosaLineEdit, self.contracuentaLineEdit)
        Dialog.setTabOrder(self.contracuentaLineEdit, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Nuevo Documento", None))
        self.pushButton.setText(_translate("Dialog", "Guardar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))
        self.labelTitulo.setText(_translate("Dialog", "Editar Documento Electrónico", None))
        self.nDocumentoLabel.setText(_translate("Dialog", "Nº Documento", None))
        self.emisorLabel.setText(_translate("Dialog", "Emisor", None))
        self.receptorLabel.setText(_translate("Dialog", "Receptor", None))
        self.fechaLabel.setText(_translate("Dialog", "Fecha", None))
        self.fechaDateEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd", None))
        self.receptorLineEdit.setPlaceholderText(_translate("Dialog", "Receptor", None))
        self.emisorLineEdit.setPlaceholderText(_translate("Dialog", "Emisor", None))
        self.nDocumentoLineEdit.setPlaceholderText(_translate("Dialog", "Numero de documento", None))
        self.sucursalLabel.setText(_translate("Dialog", "Sucursal", None))
        self.glosaLabel.setText(_translate("Dialog", "Glosa", None))
        self.sucursalLineEdit.setPlaceholderText(_translate("Dialog", "Sucursal", None))
        self.glosaLineEdit.setPlaceholderText(_translate("Dialog", "Glosa", None))
        self.cuentaProveedoresClienteLabel.setText(_translate("Dialog", "Cuenta Proveedores/Cliente", None))
        self.cuentaProveedoresClienteLineEdit.setPlaceholderText(_translate("Dialog", "Numero de cuenta", None))
        self.contracuentaLabel.setText(_translate("Dialog", "Contracuenta", None))
        self.contracuentaLineEdit.setPlaceholderText(_translate("Dialog", "Numero contracuenta", None))
        self.montoExcentoLabel.setText(_translate("Dialog", "Monto Excento", None))
        self.montoExcentoSpinBox.setPrefix(_translate("Dialog", "$ ", None))

import images_rc
