import re
import xml.etree.ElementTree as ET
class XMLprocessor:
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
		if not self._root:
			self.procesar()
		return self._root.find('DD').find('TD').text
	@TD.setter
	def TD(self,data):
		self._string=data 
		raise Exception("atributo no seteable")
	@property
	def F(self):
		if not self._root:
			self.procesar()
		return self._root.find('DD').find('F').text
	@F.setter
	def F(self,data):
		raise Exception("atributo no seteable")
	@property
	def FE(self):
		if not self._root:
			self.procesar()
		if not re.match("(.*)<FE>[1-2]\d{3}-\d{2}-\d{2}<\/FE>(.*)" ,self._string):
			raise Exception("Fecha no valida")
		return self._root.find('DD').find('FE').text
	@FE.setter
	def FE(self,data):
		raise Exception("atributo no seteable")
	@property
	def RE(self):
		if not self._root:
			self.procesar()
		return self._root.find('DD').find('RE').text
	@RE.setter
	def RE(self,data):
		raise Exception("atributo no seteable")
	@property
	def RS(self):
		if not self._root:
			self.procesar()
		return self._root.find('DD').find('RS').text
	@RS.setter
	def RS(self,data):
		raise Exception("atributo no seteable")
	@property
	def RR(self):
		if not self._root:
			self.procesar()
		return self._root.find('DD').find('RR').text
	@RR.setter
	def RR(self,data):
		raise Exception("atributo no seteable")
	@property
	def RSR(self):
		if not self._root:
			self.procesar()
		return self._root.find('DD').find('RSR').text
	@RSR.setter
	def RSR(self,data):
		raise Exception("atributo no seteable")
	@property
	def MNT(self):
		if not self._root:
			self.procesar()
		return self._root.find('DD').find('MNT').text
	@MNT.setter
	def MNT(self,data):
		raise Exception("atributo no seteable")
	def getFix(self):
		candidato = self._string
		hadTED= [False,False]
		hadTD= [False,False]
		hadF= [False,False]#numero documento
		hadFE= [False,False]#Fecha emision
		hadRE= [False,False]#Rut Emisor
		hadRS= [False,False]#Razon Social Emisor
		hadRR= [False,False]#Rut Receptor
		hadRSR= [False,False]#Razon Social Receptor
		hadMNT= [False,False]#Razon Social Receptor

		hadTED[0] = re.match("<TED (.*)" ,candidato)
		hadTED[1] = re.match("(.*)</TED>" ,candidato)
		
		hadTD[0] =  re.match("(.*)<DD>(.*)<TD>(.*)" ,candidato)
		hadTD[1] = re.match("(.*)</TD>(.*)</DD>(.*)" ,candidato)
		
		hadF[0] = re.match("(.*)<DD>(.*)<F>(.*)" ,candidato)
		hadF[1] = re.match("(.*)</F>(.*)</DD>(.*)" ,candidato)
		
		hadFE[0] = re.match("(.*)<DD>(.*)<FE>(.*)" ,candidato)
		hadFE[1] = re.match("(.*)</FE>(.*)</DD>(.*)" ,candidato)
		
		hadRE[0] = re.match("(.*)<DD><RE>(.*)" ,candidato)
		hadRE[1] = re.match("(.*)</RE>(.*)</DD>(.*)" ,candidato)

		hadRS[0] = re.match("(.*)<DD>(.*)<RS>(.*)" ,candidato)
		hadRS[1] = re.match("(.*)</RS>(.*)</DD>(.*)" ,candidato)
		
		hadRR[0] = re.match("(.*)<DD>(.*)<RR>(.*)" ,candidato)
		hadRR[1] = re.match("(.*)</RR>(.*)</DD>(.*)" ,candidato)
		
		hadRSR[0] = re.match("(.*)<DD>(.*)<RSR>(.*)" ,candidato)
		hadRSR[1] = re.match("(.*)</RSR>(.*)</DD>(.*)" ,candidato)
		
		hadMNT[0] = re.match("(.*)<DD>(.*)<MNT>(.*)" ,candidato)
		hadMNT[1] = re.match("(.*)</MNT>(.*)</DD>(.*)" ,candidato)

		if hadTD[0] and  hadTD[1] and hadF[0] and hadF[1] and hadFE[0] and hadFE[1]  and hadRE[0] and hadRE[1]  and hadRS[0] and hadRS[1] and hadRR[0] and hadRR[1] and hadRSR[0] and hadRSR[1] and hadMNT[0] and hadMNT[1]:
			print 'el candidato contiene los datos necesarios para la extraccion'
			if hadTED[0] and not hadTED[1]:
				if self.isXMLlike(candidato+"</TED>"):
					self._string = candidato+("</FRMT>","")["<FRMT " in candidato and "</FRMT>" not in candidato]+"</TED>"
				else:
					self._string = candidato+"</FRMT></TED>"
				print '--fixed'
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