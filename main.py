#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S2)

#initialize brick variables
AV1 = DriveBase(left_motor, right_motor, 30, 100)
ev3 = EV3Brick()



# Write your program here.
while line_sensor.color() != Color.BLACK:
    #ev3.speaker.play_notes(['C4/4', 'C4/4', 'G4/4', 'G4/4'])
    AV1.straight(10)
    #ev3.speaker.beep(frequency=1000, duration=500)
    
# Write your program here.
ev3.speaker.say("All Done!")


