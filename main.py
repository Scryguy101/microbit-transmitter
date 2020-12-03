radio.set_group(125)
basic.show_string("SENDER")
input.set_accelerometer_range(AcceleratorRange.EIGHT_G)

def on_forever():
    radio.send_number(input.acceleration(Dimension.Z))
    radio.send_number(input.acceleration(Dimension.Y))
    radio.send_number(input.acceleration(Dimension.X))

basic.forever(on_forever)





 



