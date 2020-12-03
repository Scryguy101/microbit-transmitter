radio.setGroup(125)
basic.showString("SENDER")
input.setAccelerometerRange(AcceleratorRange.EightG)
// compass
input.calibrateCompass()
let compass = input.compassHeading()
basic.forever(function on_forever() {
    radio.sendNumber(input.acceleration(Dimension.Z))
    radio.sendNumber(input.acceleration(Dimension.Y))
    radio.sendNumber(input.acceleration(Dimension.X))
    radio.sendString("" + compass)
    basic.showString("" + compass)
})
