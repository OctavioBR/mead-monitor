import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time, datetime, random

username = 'OctavioBR'
api_key = 't9qlzlod0v'
stream_token = 'yyml0x0ycp'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(title='Raspberry Pi Streaming Sensor Data')
fig = Figure(data=[trace1], layout=layout)
print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

stream = py.Stream(stream_token)
stream.open()

while True:
    piru = random.randint(1,10)
    stream.write({'x': datetime.datetime.now(), 'y': piru})
    time.sleep(1) # delay between stream posts