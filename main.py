radio.set_group(125)
basic.show_string("SENDER")
input.set_accelerometer_range(AcceleratorRange.EIGHT_G)

#compass
input.calibrate_compass()
compass = input.compass_heading()

def on_forever():
    radio.send_number(input.acceleration(Dimension.Z))
    radio.send_number(input.acceleration(Dimension.Y))
    radio.send_number(input.acceleration(Dimension.X))
    radio.send_string(str(compass))
    basic.show_string(str(compass))
basic.forever(on_forever)




 



