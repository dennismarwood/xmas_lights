#!/usr/bin/python

import random, time, sys
import Pixel, Xmas_1, Xmas_2

spidev    = file("/dev/spidev0.0", "wb")

pixels = [Pixel.Pixel() for i in range(25)]
xmas_1 = Xmas_1.Xmas_1()
xmas_2 = Xmas_2.Xmas_2()

def lights_out():
        spidev.write(bytearray([0]) * 75)
        spidev.flush()
        print "\nturning off lights."
        sys.exit(0)

def print_pixels():
        x = bytearray()
        for pixel in pixels:
                x += pixel.get_colors()
        spidev.write(x)
        spidev.flush()

try:
        #while xmas_1.display(pixels):
                #print_pixels()  
        while xmas_2.display(pixels):
                print_pixels()  
except KeyboardInterrupt:
        lights_out()
except Exception, e:
        print e

lights_out()