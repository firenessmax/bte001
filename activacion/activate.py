from _winreg import *
import _winreg,uuid, base64,hashlib

SN = '31b19a70-7cdc-49a0-a94e-9b3900003de3'

class Registro(object):
	@staticmethod
	def get_registry_value(key, subkey, value):
		key = getattr(_winreg, key)
		handle = _winreg.OpenKey(key, subkey)
		(value, type) = _winreg.QueryValueEx(handle, value)
		return value
	@staticmethod
	def get_PIDW():
		def get(key):
			return Registro.get_registry_value(
				"HKEY_LOCAL_MACHINE", 
				"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
				key)
		os = get("BuildGUID")
		return "%s" % (os)
	@staticmethod
	def get_activation_code():
		return Registro.get_registry_value('HKEY_CURRENT_USER', 'SOFTWARE\\CAMDE\\Settings', 'register')
	@staticmethod
	def set_activation(code):
		try:
			keyval=r"SOFTWARE\CAMDE\Settings"
			if not Registro.exist_key(HKEY_CURRENT_USER,keyval):
				key = CreateKey(HKEY_CURRENT_USER,keyval)
			Registrykey= OpenKey(HKEY_CURRENT_USER, keyval, 0,KEY_WRITE)
			SetValueEx(Registrykey,"register",0,REG_SZ,code)
			CloseKey(Registrykey)
			return True
		except WindowsError as e:
			print e
			return False
	@staticmethod
	def exist_key(key,keyval):
		try:
			aKey = OpenKey(key, keyval, 0, KEY_WRITE)
			CloseKey(aKey)
			return True
		except WindowsError:
			return False
	@staticmethod
	def verificable():
		try:
			aKey = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\CAMDE\Settings", 0, KEY_WRITE)
			CloseKey(aKey)
			return True
		except WindowsError:
			return False


class activador(object):
	@staticmethod
	def create_signature(data,SN):
		eSN = base64.b64encode(SN)
		ePIDW = base64.b64encode(data)[::-1]
		registry = base64.b64encode(eSN+'&'+ePIDW)
		return hashlib.sha1(registry).hexdigest()
	@staticmethod
	def verificar():
		if Registro.verificable():
			pidw = Registro.get_PIDW()
			'''TODO : debo archivo del SN generado por la pagina'''
			sig = activador.create_signature(pidw,SN)
			actv_code = Registro.get_activation_code()
			return sig==actv_code
		else:
			raise Exception('debe validar')
	@staticmethod
	def validar(user='admin',pw='admin'):
		'''debo contactar con la pagina y obtener el SN'''
		eUser = base64.b64encode(user)[::-1]
		ePass = base64.b64encode(pw+'\x16df'+eUser)[::-1]
		eReg = base64.b64encode(ePass+'\x16df'+Registro.get_PIDW())[::-1]
		'''genero el SN y lo guardo en un archivo especialmente creado para'''
		if Registro.set_activation("%s"%activador.create_signature(Registro.get_PIDW(),SN)):
			print 'OK'
			return True
		else:
			raise Exception('error en la validacion')

##Modo de uso
#try:
#	if activador.verificar():
#		'''continuar correctamente'''
#	else:
#		'''probablemente sea pirata'''
#except Exception as e:
#	'''solicitar usuario y contraseña'''	
#	activador.validar(user,password)



