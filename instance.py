import subprocess, win32gui,win32con
import re  

class Instance(object):
	@staticmethod
	def verificar(name):
		tasks = subprocess.check_output(['tasklist']).split("\r\n")
		cont=0
		for task in tasks:
			m = re.match("(.*)"+name+".exe(.*)",task)
			if m:
				if cont == 0:
					cont=1
				else:
					return False
		return True
	@staticmethod
	def windowEnumerationHandler(hwnd, top_windows):
		top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
	@staticmethod
	def traeralfrente():
		results = []
		top_windows = []
		win32gui.EnumWindows(Instance.windowEnumerationHandler, top_windows)
		for i in top_windows:
			print "Ventana:",i[1]
			if "Capturador CAMDE" in i[1]:
				print i
				win32gui.ShowWindow(i[0],win32con.SW_RESTORE)#9
				win32gui.SetForegroundWindow(i[0])
				break
