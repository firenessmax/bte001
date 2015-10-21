import math, sys
from PyQt4.QtCore import Qt, QTimer
from PyQt4.QtGui import *

class Overlay(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)
        self.mostrando = False
        self.hide()
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.setPen(QPen(Qt.NoPen))
        
        for i in range(6):
            if (self.counter / 5) % 6 == i:
                painter.setBrush(QBrush(QColor(127 + (self.counter % 5)*32, 127, 127)))
            else:
                painter.setBrush(QBrush(QColor(127, 127, 127)))
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
        
class MainWindow(QMainWindow):

    def __init__(self, parent = None):
    
        QMainWindow.__init__(self, parent)
        
        widget = QWidget(self)
        self.editor = QTextEdit()
        self.editor.setPlainText("0123456789"*100)
        layout = QGridLayout(widget)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        self.button = QPushButton("Wait")
        layout.addWidget(self.button, 1, 1, 1, 1)
        self.button_ = QPushButton("Ocultar")
        layout.addWidget(self.button_, 2, 1, 1, 1)
        
        self.overlay = Overlay(self.editor)
        self.button.clicked.connect(self.overlay.mostrar)
        self.button_.clicked.connect(self.overlay.parar)
        
        self.setCentralWidget(widget)
        
    def resizeEvent(self, event):
    
        self.overlay.resize(event.size())
        event.accept()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())