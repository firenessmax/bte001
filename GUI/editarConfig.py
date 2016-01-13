# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\editarConfig.ui'
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
        Dialog.resize(402, 296)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(402, 100))
        Dialog.setMaximumSize(QtCore.QSize(1000, 1000))
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
        self.facturaElectronicaLineEdit = QtGui.QLineEdit(Dialog)
        self.facturaElectronicaLineEdit.setObjectName(_fromUtf8("facturaElectronicaLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.facturaElectronicaLineEdit)
        self.facturaElectronicaLabel = QtGui.QLabel(Dialog)
        self.facturaElectronicaLabel.setObjectName(_fromUtf8("facturaElectronicaLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.facturaElectronicaLabel)
        self.facturaNoAfectaLineEdit = QtGui.QLineEdit(Dialog)
        self.facturaNoAfectaLineEdit.setObjectName(_fromUtf8("facturaNoAfectaLineEdit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.facturaNoAfectaLineEdit)
        self.facturaNoAfectaLabel = QtGui.QLabel(Dialog)
        self.facturaNoAfectaLabel.setObjectName(_fromUtf8("facturaNoAfectaLabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.facturaNoAfectaLabel)
        self.liquidacionFacturaElectronicaLineEdit = QtGui.QLineEdit(Dialog)
        self.liquidacionFacturaElectronicaLineEdit.setObjectName(_fromUtf8("liquidacionFacturaElectronicaLineEdit"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.liquidacionFacturaElectronicaLineEdit)
        self.liquidacionFacturaElectronicaLabel = QtGui.QLabel(Dialog)
        self.liquidacionFacturaElectronicaLabel.setObjectName(_fromUtf8("liquidacionFacturaElectronicaLabel"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.liquidacionFacturaElectronicaLabel)
        self.facturaDeCompraElectronicaLineEdit = QtGui.QLineEdit(Dialog)
        self.facturaDeCompraElectronicaLineEdit.setObjectName(_fromUtf8("facturaDeCompraElectronicaLineEdit"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.facturaDeCompraElectronicaLineEdit)
        self.facturaDeCompraElectronicaLabel = QtGui.QLabel(Dialog)
        self.facturaDeCompraElectronicaLabel.setObjectName(_fromUtf8("facturaDeCompraElectronicaLabel"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.facturaDeCompraElectronicaLabel)
        self.notaDeDebitoElectronicaLineEdit = QtGui.QLineEdit(Dialog)
        self.notaDeDebitoElectronicaLineEdit.setObjectName(_fromUtf8("notaDeDebitoElectronicaLineEdit"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.notaDeDebitoElectronicaLineEdit)
        self.notaDeDebitoElectronicaLabel = QtGui.QLabel(Dialog)
        self.notaDeDebitoElectronicaLabel.setObjectName(_fromUtf8("notaDeDebitoElectronicaLabel"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.notaDeDebitoElectronicaLabel)
        self.notaDeCreditoElectronicaLabel = QtGui.QLabel(Dialog)
        self.notaDeCreditoElectronicaLabel.setObjectName(_fromUtf8("notaDeCreditoElectronicaLabel"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.notaDeCreditoElectronicaLabel)
        self.notaDeCreditoElectronicaLineEdit = QtGui.QLineEdit(Dialog)
        self.notaDeCreditoElectronicaLineEdit.setObjectName(_fromUtf8("notaDeCreditoElectronicaLineEdit"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.notaDeCreditoElectronicaLineEdit)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.line = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.line.setFont(font)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 8, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject_slot)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept_slot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Editar Documento", None))
        self.pushButton.setText(_translate("Dialog", "Guardar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))
        self.labelTitulo.setText(_translate("Dialog", "Editar Empresa", None))
        self.facturaElectronicaLabel.setText(_translate("Dialog", "Factura Electronica", None))
        self.facturaNoAfectaLabel.setText(_translate("Dialog", "Factura no Afecta", None))
        self.liquidacionFacturaElectronicaLabel.setText(_translate("Dialog", "Liquidacion Factura Electronica", None))
        self.facturaDeCompraElectronicaLabel.setText(_translate("Dialog", "Factura de Compra electronica", None))
        self.notaDeDebitoElectronicaLabel.setText(_translate("Dialog", "Nota de debito electronica", None))
        self.notaDeCreditoElectronicaLabel.setText(_translate("Dialog", "Nota de credito Electronica", None))

import images_rc
