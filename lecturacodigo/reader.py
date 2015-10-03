import serial
s = serial.Serial(port='/dev/tty.Bluetooth-Incoming-Port', baudrate=9600)

s.write('text')
s.read()
s.readline()