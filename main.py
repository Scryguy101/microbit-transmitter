radio.set_group(125)
basic.show_string("SENDER")
input.set_accelerometer_range(AcceleratorRange.EIGHT_G)

#compass
input.calibrate_compass()

def on_forever():
    radio.send_value("Z", input.acceleration(Dimension.Z))
    radio.send_value("Y", input.acceleration(Dimension.Y))
    radio.send_value("X", input.acceleration(Dimension.X))
    compass = input.compass_heading()
    radio.send_string(str(compass))
    basic.show_string(str(compass))
basic.forever(on_forever)




 