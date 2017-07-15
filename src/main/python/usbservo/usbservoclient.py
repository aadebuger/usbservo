#encoding=utf-8
'''
Created on 2017年7月15日

@author: aadebuger
'''
import serial
def testservo():
        ser = serial.Serial('/dev/ttyUSB0') 
        print(ser.name)  
        ser.write(b'#1P1500T100\r\n')
        ser.close()
if __name__ == '__main__':
     testservo()