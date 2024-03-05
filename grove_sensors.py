import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connected to digital port 2
ultrasonic_ranger = 2
# Potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer, "INPUT")

# Clear LCD screen before starting the main loop
setText("")

while True:
    try:
        # TODO: Read distance value from Ultrasonic Ranger and print distance on LCD
        dist = grovepi.ultrasonicRead(ultrasonic_ranger)

        # TODO: Read threshold from potentiometer
        threshold = grovepi.analogRead(potentiometer)

        if dist < threshold:
            line1 = "{:>4}cm {:^9}".format(threshold, "OBJ PRES")
            line2 = "{:>3}cm {:^10}".format(dist, " ")
            setText_norefresh(line1 + "\n" + line2)
            setRGB(255, 0, 0)  # Set backlight color to red
        else:
            line1 = "{:>4}cm {:^9}".format(threshold, " ")
            line2 = "{:>3}cm {:^10}".format(dist, " ")
            setText_norefresh(line1 + "\n" + line2)
            setRGB(0, 255, 0)  # Set backlight color to green

    except IOError:
        print("Error")
