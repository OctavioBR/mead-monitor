from __future__ import print_function
import serial, sys, time

if (len(sys.argv) > 1):
	port = sys.argv[1]
else:
	port = "/dev/ttyACM0" # /dev/cu.usbmodem14131 for OSX

print("Starting serial readings from " + port)

fp = "data.txt"
f = open(fp, "w")
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

try:
	while True:
		input = serialFromArduino.readline()
		input = "[{0} - {1}] {2}".format(\
			time.strftime("%x"), time.strftime("%H:%M:%S"), input)
		print(input, end="")
		f.write(input)
except KeyboardInterrupt:
	f.close()
	print("\nOutput saved at " + fp)
	pass
