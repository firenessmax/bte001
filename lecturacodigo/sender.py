import os, serial
from random import randint 
#master, slave = pty.openpty()
#s_name = os.ttyname(slave)
master = "COM3"
ser = serial.Serial(master,9600,timeout=1)
# To Write to the device

while True:
	m='pp<TED version="1.0"><DD><RE>61808000-5</RE><TD>33</TD><F>'+str(randint(18678,675567))+'</F><FE>'+str(randint(2000,2015))+'-'+str(randint(1,12))+'-24</FE><RR>76041727-0</RR><RSR>SONIA GONZALEZ ,</RSR><MNT>20470</MNT><IT1>CARGO FIJO CLIENTE</IT1><CAF version="1.0"><DA><RE>61808000-5</RE><RS>AGUAS ANDINAS S A</RS><TD>39</TD><RNG><D>57030001</D><H>66030000</H></RNG><FA>2015-05-13</FA><RSAPK><M>y7ztbkQl6i5sTiPzy4a/kj2aTHZGCxTWFPODqQEy6dajXT8y3NrNKx2B8CkEZwA6QhFYAbkI7NU/AYH+GnVd0Q==</M><E>Aw==</E></RSAPK><IDK>300</IDK></DA><FRMA algoritmo="SHA1withRSA">gebZWxFc9JagXmhKaIALZ7g7Ai9rb501jsmyO6L4jThGeblJYuTAi9SDQLXoH2FtcgKOeJ+HbjdIqc520YIFZw==</FRMA></CAF><TSTED>2015-11-24T06:16:49</TSTED></DD><FRMT algoritmo="SHA1withRSA">kUjsT2edBYjhP6SS20jREfxNORT+IBG9TstFBSKayK+usFnyZNg33UDNUxcCbcXk12nQkVfsgKMedrZ4ND2AMQ==</FRMT></TED>'
	#m="0101906606000781852410300000"

	msg=raw_input("mensaje : ")
	ser.write(m)

#ser.write('Your text')
#print "puerto:\n%s"%s_name 
# To read from the device
#print os.read(master,1000)

#ser.readline()