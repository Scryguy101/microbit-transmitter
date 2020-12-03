radio.setGroup(125)
basic.showString("SENDER")
input.setAccelerometerRange(AcceleratorRange.EightG)
// compass
input.calibrateCompass()
basic.forever(function on_forever() {
    radio.sendValue("Z", input.acceleration(Dimension.Z))
    radio.sendValue("Y", input.acceleration(Dimension.Y))
    radio.sendValue("X", input.acceleration(Dimension.X))
    let compass = input.compassHeading()
    radio.sendString("" + compass)
})
