from PyQt4 import QtCore
import time


class EscanerThread(QtCore.QThread):
	def run(self):
		self.parar = False
		count = 0
		while count < 15:
			if(self.parar):
				return
			time.sleep(1)
			print "Escaneando %d veces"%count
			count += 1

