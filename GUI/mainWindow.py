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
        MainWindow.resize(760, 508)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/barcode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
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
"    background: #eaeaea;\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.top = QtGui.QFrame(self.frame_2)
        self.top.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.top.setFont(font)
        self.top.setStyleSheet(_fromUtf8("#top{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0288d1 , stop:.2 #1976d2);\n"
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
        self.gridLayout_3 = QtGui.QGridLayout(self.top)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame = QtGui.QFrame(self.top)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.toolButton = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet(_fromUtf8("QToolButton{\n"
"    background: none;\n"
"    padding: 0px 10px;\n"
"    margin:0;\n"
"    color: #dddddd;\n"
"    font-size:14px;\n"
"}\n"
"\n"
"\n"
"\n"
"QToolButton:hover{\n"
"    background: #cccccc;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout_2.addWidget(self.toolButton, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.toolButton_2 = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet(_fromUtf8("QToolButton{\n"
"    background: none;\n"
"    padding: 0px 10px;\n"
"    margin:0;\n"
"    color: #dddddd;\n"
"    font-size:14px;\n"
"}\n"
"\n"
"\n"
"\n"
"QToolButton:hover{\n"
"    background: #cccccc;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/maximize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(14, 14))
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.gridLayout_2.addWidget(self.toolButton_2, 1, 3, 1, 1)
        self.toolButton_3 = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setAutoFillBackground(False)
        self.toolButton_3.setStyleSheet(_fromUtf8("QToolButton{\n"
"    background: none;\n"
"    padding: 0px 15px;\n"
"    margin:0;\n"
"    color: #dddddd;\n"
"    font-size:14px;\n"
"}\n"
"\n"
"\n"
"\n"
"QToolButton:hover{\n"
"    background: #f44336;\n"
"    padding: 0px 15px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        self.toolButton_3.setAutoExclusive(False)
        self.toolButton_3.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.gridLayout_2.addWidget(self.toolButton_3, 1, 4, 1, 1)
        self.toolButton_4 = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet(_fromUtf8("QToolButton{\n"
"    background: none;\n"
"    padding: 0px 10px;\n"
"    margin:0;\n"
"    color: #dddddd;\n"
"    font-size:14px;\n"
"}\n"
"\n"
"\n"
"\n"
"QToolButton:hover{\n"
"    background: rgba(255, 255, 255, 153);\n"
"    color: white;\n"
"    font-size: 14px;\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/resize.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon2)
        self.toolButton_4.setIconSize(QtCore.QSize(14, 14))
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.gridLayout_2.addWidget(self.toolButton_4, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget_4 = QtGui.QTabWidget(self.top)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy)
        self.tabWidget_4.setMinimumSize(QtCore.QSize(0, 100))
        self.tabWidget_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tabWidget_4.setStyleSheet(_fromUtf8("\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border:0;\n"
"    background-color: #fafafa;\n"
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
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.escanearCompra = QtGui.QToolButton(self.tab_escanear_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/barcode.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.escanearCompra.setIcon(icon3)
        self.escanearCompra.setIconSize(QtCore.QSize(40, 35))
        self.escanearCompra.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.escanearCompra.setAutoRaise(False)
        self.escanearCompra.setObjectName(_fromUtf8("escanearCompra"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.escanearCompra)
        self.escanearVenta = QtGui.QToolButton(self.tab_escanear_3)
        self.escanearVenta.setIcon(icon)
        self.escanearVenta.setIconSize(QtCore.QSize(100, 35))
        self.escanearVenta.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.escanearVenta.setAutoRaise(False)
        self.escanearVenta.setObjectName(_fromUtf8("escanearVenta"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.escanearVenta)
        self.tabWidget_4.addTab(self.tab_escanear_3, _fromUtf8(""))
        self.tab_exportar_3 = QtGui.QWidget()
        self.tab_exportar_3.setObjectName(_fromUtf8("tab_exportar_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_exportar_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.correlativoLabel_3 = QtGui.QLabel(self.tab_exportar_3)
        self.correlativoLabel_3.setObjectName(_fromUtf8("correlativoLabel_3"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.correlativoLabel_3)
        self.correlativoSpinBox = QtGui.QSpinBox(self.tab_exportar_3)
        self.correlativoSpinBox.setWrapping(False)
        self.correlativoSpinBox.setFrame(True)
        self.correlativoSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.correlativoSpinBox.setSpecialValueText(_fromUtf8(""))
        self.correlativoSpinBox.setSuffix(_fromUtf8(""))
        self.correlativoSpinBox.setMaximum(999999999)
        self.correlativoSpinBox.setObjectName(_fromUtf8("correlativoSpinBox"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.correlativoSpinBox)
        self.verticalLayout_3.addLayout(self.formLayout_6)
        self.contabilizarCheckBox = QtGui.QCheckBox(self.tab_exportar_3)
        self.contabilizarCheckBox.setChecked(True)
        self.contabilizarCheckBox.setObjectName(_fromUtf8("contabilizarCheckBox"))
        self.verticalLayout_3.addWidget(self.contabilizarCheckBox)
        self.guardarCheckBox = QtGui.QCheckBox(self.tab_exportar_3)
        self.guardarCheckBox.setObjectName(_fromUtf8("guardarCheckBox"))
        self.verticalLayout_3.addWidget(self.guardarCheckBox)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.toolButton_5 = QtGui.QToolButton(self.tab_exportar_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/excel.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(100, 35))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.gridLayout_6.addWidget(self.toolButton_5, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 2, 1, 1)
        self.tabWidget_4.addTab(self.tab_exportar_3, _fromUtf8(""))
        self.tab_configurar_3 = QtGui.QWidget()
        self.tab_configurar_3.setObjectName(_fromUtf8("tab_configurar_3"))
        self.toolButton.raise_()
        self.tabWidget_4.addTab(self.tab_configurar_3, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget_4, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.top)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, -1, 0, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.filtrarEmpresaLabel = QtGui.QLabel(self.frame_2)
        self.filtrarEmpresaLabel.setObjectName(_fromUtf8("filtrarEmpresaLabel"))
        self.horizontalLayout_3.addWidget(self.filtrarEmpresaLabel)
        self.filtrarEmpresaComboBox = QtGui.QComboBox(self.frame_2)
        self.filtrarEmpresaComboBox.setObjectName(_fromUtf8("filtrarEmpresaComboBox"))
        self.filtrarEmpresaComboBox.addItem(_fromUtf8(""))
        self.filtrarEmpresaComboBox.addItem(_fromUtf8(""))
        self.filtrarEmpresaComboBox.addItem(_fromUtf8(""))
        self.filtrarEmpresaComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.filtrarEmpresaComboBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget_2 = QtGui.QTabWidget(self.frame_2)
        self.tabWidget_2.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"    border:0;\n"
"    background-color: #fafafa;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #fafafa;\n"
"    border: 1px solid #777777;\n"
"    border-top: 0;\n"
"    padding: 4px 10px;\n"
"    \n"
"}\n"
"\n"
"QTabBar::tab{\n"
"    min-width: 35ex;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 9px;\n"
"}"))
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_2.setUsesScrollButtons(True)
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
        self.tableWidget_Compras.setCornerButtonEnabled(False)
        self.tableWidget_Compras.setRowCount(1)
        self.tableWidget_Compras.setColumnCount(16)
        self.tableWidget_Compras.setObjectName(_fromUtf8("tableWidget_Compras"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_Compras.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
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
        self.tableWidget_Compras.horizontalHeader().setVisible(False)
        self.tableWidget_Compras.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Compras.horizontalHeader().setDefaultSectionSize(118)
        self.tableWidget_Compras.horizontalHeader().setMinimumSectionSize(118)
        self.tableWidget_Compras.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_Compras.horizontalHeader().setStretchLastSection(False)
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
        self.tableWidget_Ventas.setRowCount(0)
        self.tableWidget_Ventas.setObjectName(_fromUtf8("tableWidget_Ventas"))
        self.tableWidget_Ventas.setColumnCount(16)
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
        self.tableWidget_Ventas.horizontalHeader().setDefaultSectionSize(118)
        self.tableWidget_Ventas.horizontalHeader().setMinimumSectionSize(118)
        self.horizontalLayout_2.addWidget(self.tableWidget_Ventas)
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.tableWidget_Compras.raise_()
        self.tabWidget_2.raise_()
        self.top.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 6))
        self.statusbar.setStyleSheet(_fromUtf8("    background:#eaeaea;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;"))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QObject.connect(self.tabWidget_4, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), MainWindow.cambiarTab_slot)
        QtCore.QObject.connect(self.escanearCompra, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.escanear_slot)
        QtCore.QObject.connect(self.escanearVenta, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.escanear_slot)
        QtCore.QObject.connect(self.toolButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.exportar_slot)
        QtCore.QObject.connect(self.filtrarEmpresaComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), MainWindow.filtrar_slot)
        QtCore.QObject.connect(self.tabWidget_2, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), MainWindow.documentoCambiarTab_slot)
        QtCore.QObject.connect(self.toolButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.showFullScreen)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.showMinimized)
        QtCore.QObject.connect(self.toolButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.showNormal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SuperPrograma", None))
        self.toolButton.setText(_translate("MainWindow", "_", None))
        self.toolButton_2.setText(_translate("MainWindow", "...", None))
        self.toolButton_3.setText(_translate("MainWindow", "x", None))
        self.toolButton_4.setText(_translate("MainWindow", "...", None))
        self.escanearCompra.setText(_translate("MainWindow", "Escanear Documentos Compra", None))
        self.escanearVenta.setText(_translate("MainWindow", "Escanear Documentos Venta", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_escanear_3), _translate("MainWindow", "Escanear", None))
        self.correlativoLabel_3.setText(_translate("MainWindow", "Correlativo", None))
        self.contabilizarCheckBox.setText(_translate("MainWindow", "Contabilizar al exportar", None))
        self.guardarCheckBox.setText(_translate("MainWindow", "Guardar contabilizados", None))
        self.toolButton_5.setText(_translate("MainWindow", "Exportar Excel", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_exportar_3), _translate("MainWindow", "Exportar Excel", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_configurar_3), _translate("MainWindow", "Configurar", None))
        self.filtrarEmpresaLabel.setText(_translate("MainWindow", "Filtrar Empresa", None))
        self.filtrarEmpresaComboBox.setItemText(0, _translate("MainWindow", "Todas", None))
        self.filtrarEmpresaComboBox.setItemText(1, _translate("MainWindow", "Empresa1", None))
        self.filtrarEmpresaComboBox.setItemText(2, _translate("MainWindow", "Empresa2", None))
        self.filtrarEmpresaComboBox.setItemText(3, _translate("MainWindow", "Empresa3", None))
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
        item.setText(_translate("MainWindow", "id", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Documentos Compra", None))
        self.tableWidget_Ventas.setSortingEnabled(True)
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
        item.setText(_translate("MainWindow", "id", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Documentos Venta", None))

import images_rc
