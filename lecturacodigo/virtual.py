import os, pty, serial, time

#master, slave = pty.openpty()
#s_name = os.ttyname(slave)
s_name = "/dev/ttys003"
ser = serial.Serial(s_name,9600,timeout=.01)
# To Write to the device
bufer=' ';
while 1:
    #time.sleep(10)
    buf = ser.readline()
    if(buf!=''):
    	bufer=bufer+buf
    elif(bufer!=''):
    	print bufer
    	bufer=''

