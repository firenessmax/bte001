# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\mainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(760, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/barcode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget#centralWidget{\n"
"    border-radius: 80px;\n"
"}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setMouseTracking(True)
        self.frame_2.setAcceptDrops(False)
        self.frame_2.setStyleSheet(_fromUtf8("#frame_2{\n"
"    \n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    /*background: #eaeaea;*/\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.top = QtGui.QFrame(self.frame_2)
        self.top.setMinimumSize(QtCore.QSize(0, 134))
        self.top.setMaximumSize(QtCore.QSize(16777215, 138))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.top.setFont(font)
        self.top.setStyleSheet(_fromUtf8("#top{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(2, 136, 209, 230) , stop:.2 rgba(25, 118, 210, 250));\n"
"\n"
"    border-top-left-radius:3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller \n"
"}*/"))
        self.top.setFrameShadow(QtGui.QFrame.Plain)
        self.top.setLineWidth(0)
        self.top.setObjectName(_fromUtf8("top"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.top)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(self.top)
        self.frame.setEnabled(True)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(6, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelClose = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelClose.sizePolicy().hasHeightForWidth())
        self.labelClose.setSizePolicy(sizePolicy)
        self.labelClose.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.labelClose.setFont(font)
        self.labelClose.setStyleSheet(_fromUtf8("QLabel{\n"
"    background: none;\n"
"    padding: 0px 15px;\n"
"    margin:0;\n"
"    color: #fafafa;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    font-size:14px;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel:hover{\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    background: #f44336;\n"
"    padding: 0px 15px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        self.labelClose.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelClose.setFrameShadow(QtGui.QFrame.Raised)
        self.labelClose.setLineWidth(0)
        self.labelClose.setObjectName(_fromUtf8("labelClose"))
        self.gridLayout_2.addWidget(self.labelClose, 1, 7, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.labelMinimize = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMinimize.sizePolicy().hasHeightForWidth())
        self.labelMinimize.setSizePolicy(sizePolicy)
        self.labelMinimize.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.labelMinimize.setFont(font)
        self.labelMinimize.setStyleSheet(_fromUtf8("QLabel{\n"
"    background: none;\n"
"    padding: 0px 10px;\n"
"    margin:0;\n"
"    color: #fafafa;\n"
"    font-size:16px;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel:hover{\n"
"    background:  rgba(255, 255, 255, 153);\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        self.labelMinimize.setObjectName(_fromUtf8("labelMinimize"))
        self.gridLayout_2.addWidget(self.labelMinimize, 1, 4, 1, 1)
        self.toolButton = QtGui.QToolButton(self.frame)
        self.toolButton.setIcon(icon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout_2.addWidget(self.toolButton, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:#fafafa;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.maximize_btn = QtGui.QWidget(self.frame)
        self.maximize_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.maximize_btn.setStyleSheet(_fromUtf8("#maximize_btn{\n"
"    background: none;\n"
"    padding: 0px 10px;\n"
"    margin:0;\n"
"    color: #fafafa;\n"
"    font-size:16px;\n"
"}\n"
"\n"
"\n"
"\n"
"#maximize_btn:hover{\n"
"    background:  rgba(255, 255, 255, 153);\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        self.maximize_btn.setObjectName(_fromUtf8("maximize_btn"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.maximize_btn)
        self.verticalLayout_6.setContentsMargins(12, -1, 12, 8)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_2 = QtGui.QLabel(self.maximize_btn)
        self.label_2.setMaximumSize(QtCore.QSize(13, 10))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/maximize.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2)
        self.gridLayout_2.addWidget(self.maximize_btn, 1, 6, 1, 1)
        self.resize_btn = QtGui.QFrame(self.frame)
        self.resize_btn.setStyleSheet(_fromUtf8("#resize_btn{\n"
"    background: none;\n"
"    margin:0;\n"
"    color: #fafafa;\n"
"    font-size:16px;\n"
"}\n"
"\n"
"\n"
"\n"
"#resize_btn:hover{\n"
"    background:  rgba(255, 255, 255, 153);\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        self.resize_btn.setFrameShape(QtGui.QFrame.StyledPanel)
        self.resize_btn.setFrameShadow(QtGui.QFrame.Raised)
        self.resize_btn.setObjectName(_fromUtf8("resize_btn"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.resize_btn)
        self.verticalLayout_7.setContentsMargins(12, -1, 12, 8)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_3 = QtGui.QLabel(self.resize_btn)
        self.label_3.setMinimumSize(QtCore.QSize(0, 12))
        self.label_3.setMaximumSize(QtCore.QSize(12, 12))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/resize.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_7.addWidget(self.label_3)
        self.gridLayout_2.addWidget(self.resize_btn, 1, 5, 1, 1)
        self.verticalLayout_4.addWidget(self.frame)
        self.tabWidget_4 = QtGui.QTabWidget(self.top)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy)
        self.tabWidget_4.setMinimumSize(QtCore.QSize(0, 117))
        self.tabWidget_4.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.tabWidget_4.setFont(font)
        self.tabWidget_4.setStyleSheet(_fromUtf8("\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border:0;\n"
"    background-color: #fafafa;\n"
"    \n"
"    border-left:1px solid #aaaaaa;\n"
"    border-right:1px solid #aaaaaa;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 10px;\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab{\n"
"    color:white;\n"
"    background: rgba(255, 255, 255, 0);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    min-width: 25ex;\n"
"\n"
"    padding: 5 20 5 20;\n"
"    \n"
"    margin-right:2px;\n"
"    margin-left:2px;\n"
"}\n"
"QTabBar::tab {/*grin*/\n"
"    border-bottom:5px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #388e3c, stop: 0.7 #689f38);\n"
"}\n"
"QTabBar::tab:hover:!selected {/*grin*/\n"
"    background:#388e3c;\n"
"    border:1px solid #388e3c;\n"
"    border-bottom:5px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #388e3c, stop: 0.7 #689f38);\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-bottom:5px solid  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1976d2, stop: 0.5 #0288d1);;\n"
"}\n"
"QTabBar::tab:first:hover:!selected {/*grin*/\n"
"    background:#0288d1;\n"
"    border:1px solid #0288d1;\n"
"    border-bottom:5px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1976d2, stop: 0.7 #0288d1);\n"
"}\n"
"QTabBar::tab:last {\n"
"border-bottom :5px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #9e9e9e, stop: 0.5 #AAAAAA);\n"
"}\n"
"QTabBar::tab:last:hover:!selected {/*grin*/\n"
"    background:#ADADAD;\n"
"    border:1px solid #9e9e9e;\n"
"    border-bottom:5px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #9e9e9e, stop: 0.7 #AAAAAA);\n"
"}\n"
"QTabBar::tab:selected {\n"
"    color:black;\n"
"    background: #fafafa;\n"
"    border:0;\n"
"}"))
        self.tabWidget_4.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget_4.setUsesScrollButtons(True)
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.tab_escanear_3 = QtGui.QWidget()
        self.tab_escanear_3.setStyleSheet(_fromUtf8(""))
        self.tab_escanear_3.setObjectName(_fromUtf8("tab_escanear_3"))
        self.formLayout_5 = QtGui.QFormLayout(self.tab_escanear_3)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setContentsMargins(-1, 7, -1, -1)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.escanearVenta = QtGui.QToolButton(self.tab_escanear_3)
        self.escanearVenta.setEnabled(False)
        self.escanearVenta.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.escanearVenta.setFont(font)
        self.escanearVenta.setIcon(icon)
        self.escanearVenta.setIconSize(QtCore.QSize(100, 35))
        self.escanearVenta.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.escanearVenta.setAutoRaise(False)
        self.escanearVenta.setObjectName(_fromUtf8("escanearVenta"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.escanearVenta)
        self.escanearCompra = QtGui.QToolButton(self.tab_escanear_3)
        self.escanearCompra.setEnabled(False)
        self.escanearCompra.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.escanearCompra.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/barcode.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.escanearCompra.setIcon(icon1)
        self.escanearCompra.setIconSize(QtCore.QSize(100, 35))
        self.escanearCompra.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.escanearCompra.setAutoRaise(False)
        self.escanearCompra.setObjectName(_fromUtf8("escanearCompra"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.escanearCompra)
        self.tabWidget_4.addTab(self.tab_escanear_3, _fromUtf8(""))
        self.tab_exportar_3 = QtGui.QWidget()
        self.tab_exportar_3.setObjectName(_fromUtf8("tab_exportar_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_exportar_3)
        self.gridLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.contabilizarCheckBox = QtGui.QCheckBox(self.tab_exportar_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.contabilizarCheckBox.setFont(font)
        self.contabilizarCheckBox.setChecked(True)
        self.contabilizarCheckBox.setObjectName(_fromUtf8("contabilizarCheckBox"))
        self.verticalLayout_3.addWidget(self.contabilizarCheckBox)
        self.guardarCheckBox = QtGui.QCheckBox(self.tab_exportar_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.guardarCheckBox.setFont(font)
        self.guardarCheckBox.setObjectName(_fromUtf8("guardarCheckBox"))
        self.verticalLayout_3.addWidget(self.guardarCheckBox)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.toolButtonExcel = QtGui.QToolButton(self.tab_exportar_3)
        self.toolButtonExcel.setMinimumSize(QtCore.QSize(0, 65))
        self.toolButtonExcel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.toolButtonExcel.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/excel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonExcel.setIcon(icon2)
        self.toolButtonExcel.setIconSize(QtCore.QSize(100, 35))
        self.toolButtonExcel.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonExcel.setObjectName(_fromUtf8("toolButtonExcel"))
        self.gridLayout_6.addWidget(self.toolButtonExcel, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 2, 1, 1)
        self.tabWidget_4.addTab(self.tab_exportar_3, _fromUtf8(""))
        self.tab_configurar_3 = QtGui.QWidget()
        self.tab_configurar_3.setObjectName(_fromUtf8("tab_configurar_3"))
        self.gridLayout = QtGui.QGridLayout(self.tab_configurar_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.tab_configurar_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButtonDevice = QtGui.QPushButton(self.tab_configurar_3)
        self.pushButtonDevice.setEnabled(False)
        self.pushButtonDevice.setObjectName(_fromUtf8("pushButtonDevice"))
        self.gridLayout.addWidget(self.pushButtonDevice, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_configurar_3)
        self.label_5.setMinimumSize(QtCore.QSize(25, 25))
        self.label_5.setMaximumSize(QtCore.QSize(25, 25))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.dispositivosComboBox = QtGui.QComboBox(self.tab_configurar_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispositivosComboBox.sizePolicy().hasHeightForWidth())
        self.dispositivosComboBox.setSizePolicy(sizePolicy)
        self.dispositivosComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.dispositivosComboBox.setObjectName(_fromUtf8("dispositivosComboBox"))
        self.gridLayout.addWidget(self.dispositivosComboBox, 0, 1, 1, 1)
        self.restaurarToolButton = QtGui.QToolButton(self.tab_configurar_3)
        self.restaurarToolButton.setMinimumSize(QtCore.QSize(0, 65))
        self.restaurarToolButton.setStyleSheet(_fromUtf8("margin-bottom: 6px"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/unnamed (2).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restaurarToolButton.setIcon(icon3)
        self.restaurarToolButton.setIconSize(QtCore.QSize(100, 35))
        self.restaurarToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.restaurarToolButton.setObjectName(_fromUtf8("restaurarToolButton"))
        self.gridLayout.addWidget(self.restaurarToolButton, 0, 5, 1, 1)
        self.respaldarToolButton = QtGui.QToolButton(self.tab_configurar_3)
        self.respaldarToolButton.setMinimumSize(QtCore.QSize(0, 65))
        self.respaldarToolButton.setStyleSheet(_fromUtf8("margin-bottom: 6px"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/unnamed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.respaldarToolButton.setIcon(icon4)
        self.respaldarToolButton.setIconSize(QtCore.QSize(100, 35))
        self.respaldarToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.respaldarToolButton.setObjectName(_fromUtf8("respaldarToolButton"))
        self.gridLayout.addWidget(self.respaldarToolButton, 0, 6, 1, 1)
        self.tabWidget_4.addTab(self.tab_configurar_3, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget_4)
        self.verticalLayout_2.addWidget(self.top)
        self.frame_3 = QtGui.QFrame(self.frame_2)
        self.frame_3.setStyleSheet(_fromUtf8("#frame_3{ \n"
"    background-color: #dddddd;\n"
"    border-left:1px solid #aaaaaa;\n"
"    border-right:1px solid #aaaaaa;\n"
"}"))
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(9, 6, 9, 4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.filtrarEmpresaLabel = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.filtrarEmpresaLabel.setFont(font)
        self.filtrarEmpresaLabel.setObjectName(_fromUtf8("filtrarEmpresaLabel"))
        self.horizontalLayout_3.addWidget(self.filtrarEmpresaLabel)
        self.filtrarEmpresaComboBox = QtGui.QComboBox(self.frame_3)
        self.filtrarEmpresaComboBox.setMinimumSize(QtCore.QSize(85, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.filtrarEmpresaComboBox.setFont(font)
        self.filtrarEmpresaComboBox.setModelColumn(0)
        self.filtrarEmpresaComboBox.setObjectName(_fromUtf8("filtrarEmpresaComboBox"))
        self.horizontalLayout_3.addWidget(self.filtrarEmpresaComboBox)
        self.fechaComboBox = QtGui.QComboBox(self.frame_3)
        self.fechaComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.fechaComboBox.setObjectName(_fromUtf8("fechaComboBox"))
        self.fechaComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.fechaComboBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.rehacerToolButton = QtGui.QToolButton(self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Error.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rehacerToolButton.setIcon(icon5)
        self.rehacerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.rehacerToolButton.setObjectName(_fromUtf8("rehacerToolButton"))
        self.horizontalLayout_3.addWidget(self.rehacerToolButton)
        self.deshacerToolButton = QtGui.QToolButton(self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/bigBug.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deshacerToolButton.setIcon(icon6)
        self.deshacerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.deshacerToolButton.setObjectName(_fromUtf8("deshacerToolButton"))
        self.horizontalLayout_3.addWidget(self.deshacerToolButton)
        self.toolButton_3 = QtGui.QToolButton(self.frame_3)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/pregunta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon7)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.tabWidget_2 = QtGui.QTabWidget(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"   background: #fafafa;\n"
"    border:0;\n"
"    border-left:1px solid qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 #666666, stop:1 #dddddd)\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #fafafa;\n"
"    border: 1px solid #777777;\n"
"    border-top: 0;\n"
"    padding: 4px 15px;\n"
"    height:16px;\n"
"    border-top-left-radius: 0;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab{\n"
"    height:10px;\n"
"    padding: 4px 5px;\n"
"    background: #dddddd;\n"
"    border: 1px solid #666666;\n"
"    border-top:3px solid qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 #dddddd, stop:1 #999999);\n"
"    min-width: 40ex;\n"
"    border-top-left-radius: 1px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"QTabBar::tab:first:!selected {\n"
"    border-right:0;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"QTabBar::tab:last:!selected {\n"
"    border-left:0;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background: #dfdfee;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px;\n"
"}\n"
""))
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableWidget_Compras = QtGui.QTableWidget(self.tab)
        self.tableWidget_Compras.setAcceptDrops(False)
        self.tableWidget_Compras.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget_Compras.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget_Compras.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Compras.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_Compras.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget_Compras.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_Compras.setWordWrap(True)
        self.tableWidget_Compras.setCornerButtonEnabled(True)
        self.tableWidget_Compras.setRowCount(1)
        self.tableWidget_Compras.setColumnCount(17)
        self.tableWidget_Compras.setObjectName(_fromUtf8("tableWidget_Compras"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Compras.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_Compras.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_Compras.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_Compras.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_Compras.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_Compras.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_Compras.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_Compras.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_Compras.setItem(0, 0, item)
        self.tableWidget_Compras.horizontalHeader().setVisible(True)
        self.tableWidget_Compras.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Compras.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_Compras.horizontalHeader().setMinimumSectionSize(12)
        self.tableWidget_Compras.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_Compras.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_Compras.verticalHeader().setVisible(True)
        self.tableWidget_Compras.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Compras.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_Compras.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tableWidget_Compras)
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidget_Ventas = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_Ventas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Ventas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_Ventas.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget_Ventas.setRowCount(1)
        self.tableWidget_Ventas.setObjectName(_fromUtf8("tableWidget_Ventas"))
        self.tableWidget_Ventas.setColumnCount(17)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Ventas.setHorizontalHeaderItem(16, item)
        self.tableWidget_Ventas.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Ventas.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_Ventas.horizontalHeader().setMinimumSectionSize(12)
        self.tableWidget_Ventas.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_Ventas.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_Ventas.verticalHeader().setVisible(False)
        self.tableWidget_Ventas.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Ventas.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_Ventas.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_2.addWidget(self.tableWidget_Ventas)
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabWidget_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.statusbar.setStyleSheet(_fromUtf8("QStatusBar{    background:#dddddd;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border:1px solid #aaaaaa;\n"
"    border-top:1px solid #cccccc;\n"
"}"))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabWidget_4, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), MainWindow.cambiarTab_slot)
        QtCore.QObject.connect(self.escanearCompra, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.escanear_slot)
        QtCore.QObject.connect(self.escanearVenta, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.escanear_slot)
        QtCore.QObject.connect(self.toolButtonExcel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.exportar_slot)
        QtCore.QObject.connect(self.filtrarEmpresaComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.filtrar_slot)
        QtCore.QObject.connect(self.tabWidget_2, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), MainWindow.documentoCambiarTab_slot)
        QtCore.QObject.connect(self.pushButtonDevice, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.buscar_slot)
        QtCore.QObject.connect(self.dispositivosComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.dispositivoChange_slot)
        QtCore.QObject.connect(self.deshacerToolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.deshacer_slot)
        QtCore.QObject.connect(self.rehacerToolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.rehacer_slot)
        QtCore.QObject.connect(self.restaurarToolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.restaurar_slot)
        QtCore.QObject.connect(self.respaldarToolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.respaldar_slot)
        QtCore.QObject.connect(self.fechaComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.filtrarFecha_slot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.escanearCompra, self.escanearVenta)
        MainWindow.setTabOrder(self.escanearVenta, self.contabilizarCheckBox)
        MainWindow.setTabOrder(self.contabilizarCheckBox, self.guardarCheckBox)
        MainWindow.setTabOrder(self.guardarCheckBox, self.toolButtonExcel)
        MainWindow.setTabOrder(self.toolButtonExcel, self.filtrarEmpresaComboBox)
        MainWindow.setTabOrder(self.filtrarEmpresaComboBox, self.toolButton_3)
        MainWindow.setTabOrder(self.toolButton_3, self.tabWidget_2)
        MainWindow.setTabOrder(self.tabWidget_2, self.tableWidget_Compras)
        MainWindow.setTabOrder(self.tableWidget_Compras, self.tableWidget_Ventas)
        MainWindow.setTabOrder(self.tableWidget_Ventas, self.tabWidget_4)
        MainWindow.setTabOrder(self.tabWidget_4, self.toolButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Capturador CAMDE 0.9", None))
        self.labelClose.setText(_translate("MainWindow", "x", None))
        self.labelMinimize.setText(_translate("MainWindow", "_", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.label.setText(_translate("MainWindow", "Capturador CAMDE 0.9", None))
        self.escanearVenta.setText(_translate("MainWindow", "Escanear Documentos Venta", None))
        self.escanearCompra.setText(_translate("MainWindow", "Escanear Documentos Compra", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_escanear_3), _translate("MainWindow", "Escanear", None))
        self.contabilizarCheckBox.setToolTip(_translate("MainWindow", "Al realizar la exportación, todas las facturas exportadas se marcarán como \"contabilizadas\"", None))
        self.contabilizarCheckBox.setText(_translate("MainWindow", "Contabilizar al exportar", None))
        self.guardarCheckBox.setToolTip(_translate("MainWindow", "Al realizar la exportación, se incluirán las facturas que han sido \"contabiliadas\"", None))
        self.guardarCheckBox.setText(_translate("MainWindow", "Guardar contabilizados", None))
        self.toolButtonExcel.setText(_translate("MainWindow", "Exportar Excel", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_exportar_3), _translate("MainWindow", "Exportar Excel", None))
        self.label_4.setText(_translate("MainWindow", "Dispositivo:", None))
        self.pushButtonDevice.setText(_translate("MainWindow", "Buscar", None))
        self.restaurarToolButton.setText(_translate("MainWindow", "Restaurar", None))
        self.respaldarToolButton.setText(_translate("MainWindow", "Respaldar", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_configurar_3), _translate("MainWindow", "Configurar", None))
        self.filtrarEmpresaLabel.setToolTip(_translate("MainWindow", "Filtro por rut de las empresas", None))
        self.filtrarEmpresaLabel.setText(_translate("MainWindow", "Filtrar Empresa", None))
        self.filtrarEmpresaComboBox.setToolTip(_translate("MainWindow", "Filtro por rut de las empresas", None))
        self.fechaComboBox.setItemText(0, _translate("MainWindow", "Marzo-2015", None))
        self.rehacerToolButton.setText(_translate("MainWindow", "Rehacer", None))
        self.deshacerToolButton.setText(_translate("MainWindow", "Deshacer", None))
        self.toolButton_3.setText(_translate("MainWindow", "...", None))
        self.tableWidget_Compras.setSortingEnabled(True)
        item = self.tableWidget_Compras.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Contabilizado", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sucursal", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo Documento", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Numero Documento", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fecha", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Rut Emisor", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "RS Emisor", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Rut Receptor", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "RS Receptor", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Monto Exento", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Monto Afecto", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Monto IVA", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Monto Total", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Glosa", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Contracuenta", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Activo Fijo", None))
        item = self.tableWidget_Compras.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "id", None))
        __sortingEnabled = self.tableWidget_Compras.isSortingEnabled()
        self.tableWidget_Compras.setSortingEnabled(False)
        item = self.tableWidget_Compras.item(0, 0)
        item.setText(_translate("MainWindow", "213", None))
        self.tableWidget_Compras.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Documentos Compra", None))
        self.tableWidget_Ventas.setSortingEnabled(True)
        item = self.tableWidget_Ventas.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Contabilizado", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sucursal", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo Documento", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Numero Documento", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fecha", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Rut Emisor", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "RS Emisor", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Rut Receptor", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "RS Receptor", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Monto Exento", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Monto Afecto", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Monto IVA", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Monto Total", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Glosa", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Contracuenta", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Activo Fijo", None))
        item = self.tableWidget_Ventas.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "id", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Documentos Venta", None))

import images_rc
