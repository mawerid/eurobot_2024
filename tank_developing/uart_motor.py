import time
import serial
import sys

ser = serial.Serial(

    port = '/dev/ttyS0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 1000
)
choose_motor = 0b01
choose_dim = 0b01
angle = 0x7
counter=0
while 1:
    ser.write(b'\x02')
    ser.write(b'\x01')
    ser.write(b'\xFE')
    time.sleep(0.01)
    ser.write(b'\x01')
    ser.write(b'\x01')
    ser.write(b'\xFE')
    time.sleep(5)
    ser.write(b'\x02')
    ser.write(b'\x02')
    ser.write(b'\xFE')
    time.sleep(0.01)
    ser.write(b'\x01')
    ser.write(b'\x02')
    ser.write(b'\xFE')
    time.sleep(5)