radio.setGroup(125)
basic.showString("SENDER")
input.setAccelerometerRange(AcceleratorRange.EightG)
basic.forever(function on_forever() {
    radio.sendNumber(input.acceleration(Dimension.Z))
    radio.sendNumber(input.acceleration(Dimension.Y))
    radio.sendNumber(input.acceleration(Dimension.X))
})
