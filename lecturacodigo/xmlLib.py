import re
import xml.etree.ElementTree as ET
class XMLprocessor(object):
	'''
	TD  - tipo documento
	F   - numero de documento
	FE  - fecha de emision || debe ser convertida de aaaa-MM-dd a dd/MM/aaaa
	RE  - rut emisor/proveedor
	RS  - nombre emisor/proveedor
	RR  - rut receptor
	RSR - nombre receptor
	MNT - monto total(iva incluido)   
	//debemos fixear el codigo
	'''
	_string = ''
	_root = None
	def __init__(self,s):
		self._string = s

	def procesar(self):
		if not self.isXMLlike(self._string):
			self.getFix()
		self._root = ET.fromstring(self._string)
	@property
	def TD(self):
		if self._root is None:
			self.procesar()
		return self._root.find('DD').find('TD').text
	@TD.setter
	def TD(self,data):
		self._string=data 
		raise Exception("atributo no seteable")
	@property
	def F(self):
		if self._root is None:
			self.procesar()
		return self._root.find('DD').find('F').text
	@F.setter
	def F(self,data):
		raise Exception("atributo no seteable")
	@property
	def FE(self):
		if self._root is None:
			self.procesar()
		if not re.match("(.*)<FE>[1-2]\d{3}-\d{2}-\d{2}<\/FE>(.*)" ,self._string):
			raise Exception("Fecha no valida")
		return self._root.find('DD').find('FE').text
	@FE.setter
	def FE(self,data):
		raise Exception("atributo no seteable")
	@property
	def RE(self):
		if self._root is None:
			self.procesar()
		return self._root.find('DD').find('RE').text
	@RE.setter
	def RE(self,data):
		raise Exception("atributo no seteable")
	@property
	def RS(self):
		if self._root is None:
			self.procesar()
		return self._root.find('DD').find('CAF').find('DA').find('RS').text
	@RS.setter
	def RS(self,data):
		raise Exception("atributo no seteable")
	@property
	def RR(self):
		if self._root is None:
			self.procesar()
		return self._root.find('DD').find('RR').text
	@RR.setter
	def RR(self,data):
		raise Exception("atributo no seteable")
	@property
	def RSR(self):
		if self._root is None:
			self.procesar()
		return self._root.find('DD').find('RSR').text
	@RSR.setter
	def RSR(self,data):
		raise Exception("atributo no seteable")
	@property
	def MNT(self):
		if self._root is None:
			self.procesar()
		return self._root.find('DD').find('MNT').text
	@MNT.setter
	def MNT(self,data):
		raise Exception("atributo no seteable")
	def getFix(self):
		candidato = self._string
		hadTED= [re.match("<TED (.*)" ,candidato),re.match("(.*)</TED>" ,candidato)]
		hadTD =  re.match("(.*)<DD>(.*)<TD>(.*)</TD>(.*)</DD>(.*)" ,candidato)
		hadF = re.match("(.*)<DD>(.*)<F>(.*)</F>(.*)</DD>(.*)" ,candidato)
		hadFE = re.match("(.*)<DD>(.*)<FE>(.*)</FE>(.*)</DD>(.*)" ,candidato)
		hadRE = re.match("(.*)<DD><RE>(.*)</RE>(.*)</DD>(.*)" ,candidato)
		hadRS = re.match("(.*)<DD>(.*)<RS>(.*)</RS>(.*)</DD>(.*)" ,candidato)
		hadRR = re.match("(.*)<DD>(.*)<RR>(.*)</RR>(.*)</DD>(.*)" ,candidato)
		hadRSR = re.match("(.*)<DD>(.*)<RSR>(.*)</RSR>(.*)</DD>(.*)" ,candidato)
		hadMNT = re.match("(.*)<DD>(.*)<MNT>(.*)</MNT>(.*)</DD>(.*)" ,candidato)
		if hadTD and hadF and hadFE  and hadRE  and hadRS and hadRR and hadRSR and hadMNT:
			print 'el candidato contiene los datos necesarios para la extraccion'
			if hadTED[0] and not hadTED[1]:
				if self.isXMLlike(candidato+"</TED>"):
					self._string = candidato+"</TED>"
				else:
					self._string = candidato+"</FRMT></TED>"
					if not self.isXMLlike(self._string):
						raise Exception("Codigo no es corregible")
				print '==fixed'
		else:
			print "El codigo no tiene los datos necesarios para la extraccion"
			self._string= '<TED><DD></DD></TED>'#not fixeable
			print 'codigo incorrecto'
			raise Exception("Codigo no es corregible")
	def isXMLlike(self,s):
		if not re.match('<TED (.*)',s):
			raise Exception("Codigo no es de tipo TED")
		try:
			ET.fromstring(s)
			return True
		except:
			return False