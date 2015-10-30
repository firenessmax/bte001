# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\login.ui'
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
        Dialog.resize(338, 205)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Error.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"    background:#fafafa\n"
"}\n"
"QLineEdit,QDateEdit,QDoubleSpinBox{\n"
"    padding:4px\n"
"}"))
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.enviarPushButton = QtGui.QPushButton(Dialog)
        self.enviarPushButton.setObjectName(_fromUtf8("enviarPushButton"))
        self.horizontalLayout_2.addWidget(self.enviarPushButton)
        self.cancelPushButton = QtGui.QPushButton(Dialog)
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.horizontalLayout_2.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 6, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelTitulo = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
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
        self.mailLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.mailLineEdit.setFont(font)
        self.mailLineEdit.setReadOnly(False)
        self.mailLineEdit.setObjectName(_fromUtf8("mailLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.mailLineEdit)
        self.emisorLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emisorLabel.setFont(font)
        self.emisorLabel.setObjectName(_fromUtf8("emisorLabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.emisorLabel)
        self.passwordLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setInputMask(_fromUtf8(""))
        self.passwordLineEdit.setText(_fromUtf8(""))
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setReadOnly(False)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.passwordLineEdit)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.mensajeLabel = QtGui.QLabel(Dialog)
        self.mensajeLabel.setObjectName(_fromUtf8("mensajeLabel"))
        self.gridLayout_2.addWidget(self.mensajeLabel, 2, 2, 1, 1)
        self.spinnerLabel = QtGui.QLabel(Dialog)
        self.spinnerLabel.setEnabled(True)
        self.spinnerLabel.setMinimumSize(QtCore.QSize(25, 25))
        self.spinnerLabel.setMaximumSize(QtCore.QSize(25, 25))
        self.spinnerLabel.setText(_fromUtf8(""))
        self.spinnerLabel.setScaledContents(True)
        self.spinnerLabel.setObjectName(_fromUtf8("spinnerLabel"))
        self.gridLayout_2.addWidget(self.spinnerLabel, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 6, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancelPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.enviarPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.mailLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), Dialog.reject)
        QtCore.QObject.connect(self.mailLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.changed_slot)
        QtCore.QObject.connect(self.passwordLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.changed_slot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.mailLineEdit, self.passwordLineEdit)
        Dialog.setTabOrder(self.passwordLineEdit, self.enviarPushButton)
        Dialog.setTabOrder(self.enviarPushButton, self.cancelPushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Activacion", None))
        self.enviarPushButton.setText(_translate("Dialog", "Enviar", None))
        self.cancelPushButton.setText(_translate("Dialog", "Cancelar", None))
        self.labelTitulo.setText(_translate("Dialog", "Autentificacion", None))
        self.nDocumentoLabel.setText(_translate("Dialog", "E-mail", None))
        self.mailLineEdit.setPlaceholderText(_translate("Dialog", "E-mail", None))
        self.emisorLabel.setText(_translate("Dialog", "Constraseña", None))
        self.passwordLineEdit.setPlaceholderText(_translate("Dialog", "Contraseña", None))
        self.mensajeLabel.setText(_translate("Dialog", "Conectando", None))

import images_rc
