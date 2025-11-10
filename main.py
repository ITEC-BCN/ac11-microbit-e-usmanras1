temp = 0
MAX_TEMP = 50

def on_forever():
    global temp
    temp = input.temperature()
    led.plot_bar_graph(temp, MAX_TEMP)
basic.forever(on_forever)
