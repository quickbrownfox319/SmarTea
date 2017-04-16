import os, sys, traceback
import simplejson as json
import serial
import time as t

#rpi serial port with arduino
serialPort = '/dev/cu.usbmodem1411'
filename = "data.txt"


def main():
    #serial connection to arduino
    serialConnection = serial.Serial(serialPort, timeout = 2.0)

    while True:
        #get serial data from arduino
        data = serialConnection.readline().strip()
        if data:
            #print(data)
            with open(filename, 'a') as outputFile:
                outputFile.write('{}\n'.format(data.decode('utf-8')))
                #json.dump(data,outputFile)
            t.sleep(2)

if __name__ == '__main__':
    main()