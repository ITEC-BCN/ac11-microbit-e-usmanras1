let temp = 0
let MAX_TEMP = 50
basic.forever(function on_forever() {
    
    temp = input.temperature()
    led.plotBarGraph(temp, MAX_TEMP)
})
