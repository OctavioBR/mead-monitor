import serial, sys, time, datetime
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure

def serial_port():
	if (len(sys.argv) > 1):
		port = sys.argv[1]
	else:
		port = "/dev/ttyACM0" # /dev/cu.usbmodem14131 for OSX
	return port

def save_on_file(arduino_serial, file_path):
	f = open(file_path, "w")
	f.write("date,time,temp,clicks\n")
	try:
		while True:
			input = arduino_serial.readline()
			input = "{0},{1},{2}".format(\
				time.strftime("%x"), time.strftime("%H:%M:%S"), input)
			f.write(input)
	except KeyboardInterrupt:
		f.close()
		print "\nOutput saved at " + file_path
		pass

def plotly_stream(arduino_serial):
	pass

def main():
	port = serial_port()
	print "Starting serial readings from " + port

	arduino_serial = serial.Serial(port, 9600)
	arduino_serial.flushInput()

	save_on_file(arduino_serial, "data.csv")

if __name__ == "__main__":
    main()