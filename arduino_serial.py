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
	username = 'OctavioBR'
	api_key = 't9qlzlod0v'
	stream_token1 = 'yyml0x0ycp'
	stream_token2 = 'xve4lhin3t'
	stream_token3 = 'wh5943tytf'
	py.sign_in(username, api_key)

	trace1 = Scatter(
		x=[], y=[],
		name="temperature1",
		stream=dict(token=stream_token1, maxpoints=80)
	)

	trace2 = Scatter(
		x=[], y=[],
		name="temperature2",
		stream=dict(token=stream_token2, maxpoints=80)
	)

	trace3 = Scatter(
		x=[], y=[],
		name="pulses", yaxis="y2",
		stream=dict(token=stream_token3, maxpoints=80)
	)

	layout = Layout(
		title="Temperature & flow clicks",
		yaxis=dict(title="Temperature"),
		yaxis2=dict(title="# of Pulses", overlaying="y",side="right")
	)

	fig = Figure(data=[trace1, trace2, trace3], layout=layout)
	plot_url = py.plot(fig, filename="Temperature & Flow")

	stream1 = py.Stream(stream_token1)
	stream2 = py.Stream(stream_token2)
	stream3 = py.Stream(stream_token3)
	stream1.open()
	stream2.open()
	stream3.open()

	try:
		while True:
			x = datetime.datetime.now()
			input = arduino_serial.readline()
			stream1.write({"x": x, "y": input.split(",")[0]})
			stream2.write({"x": x, "y": input.split(",")[1]})
			stream3.write({"x": x, "y": input.split(",")[2]})
	except KeyboardInterrupt:
		stream1.close()
		stream2.close()
		stream3.close()
		print "\nStopped plotting at " + plot_url
		pass

def main():
	port = serial_port()
	print "Starting serial readings from " + port

	arduino_serial = serial.Serial(port, 9600)
	arduino_serial.flushInput()

	# save_on_file(arduino_serial, "data.csv")
	plotly_stream(arduino_serial)

if __name__ == "__main__":
    main()