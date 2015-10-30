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
        Dialog.resize(412, 214)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
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
        self.nDocumentoLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.nDocumentoLineEdit.setFont(font)
        self.nDocumentoLineEdit.setReadOnly(False)
        self.nDocumentoLineEdit.setObjectName(_fromUtf8("nDocumentoLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.nDocumentoLineEdit)
        self.emisorLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emisorLabel.setFont(font)
        self.emisorLabel.setObjectName(_fromUtf8("emisorLabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.emisorLabel)
        self.emisorLineEdit = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.emisorLineEdit.setFont(font)
        self.emisorLineEdit.setInputMask(_fromUtf8(""))
        self.emisorLineEdit.setText(_fromUtf8(""))
        self.emisorLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.emisorLineEdit.setReadOnly(False)
        self.emisorLineEdit.setObjectName(_fromUtf8("emisorLineEdit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.emisorLineEdit)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.spinnerLabel = QtGui.QLabel(Dialog)
        self.spinnerLabel.setMinimumSize(QtCore.QSize(25, 25))
        self.spinnerLabel.setMaximumSize(QtCore.QSize(25, 25))
        self.spinnerLabel.setText(_fromUtf8(""))
        self.spinnerLabel.setScaledContents(True)
        self.spinnerLabel.setObjectName(_fromUtf8("spinnerLabel"))
        self.horizontalLayout.addWidget(self.spinnerLabel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 6, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.nDocumentoLineEdit, self.emisorLineEdit)
        Dialog.setTabOrder(self.emisorLineEdit, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Activacion", None))
        self.pushButton.setText(_translate("Dialog", "Enviar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))
        self.labelTitulo.setText(_translate("Dialog", "Autentificacion", None))
        self.nDocumentoLabel.setText(_translate("Dialog", "E-mail", None))
        self.nDocumentoLineEdit.setPlaceholderText(_translate("Dialog", "E-mail", None))
        self.emisorLabel.setText(_translate("Dialog", "Constraseña", None))
        self.emisorLineEdit.setPlaceholderText(_translate("Dialog", "Contraseña", None))
        self.label_2.setText(_translate("Dialog", "TextLabel", None))

import images_rc
