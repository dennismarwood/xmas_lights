#!/usr/bin/python

import Image, time, random, math
import signal, sys

spidev    = file("/dev/spidev0.0", "wb")

color = bytearray([0]) * 75


def lights_out():
        color = bytearray([0]) * 75
        spidev.flush()
        spidev.write(color)
        print "\nturning off lights."
        sys.exit(0)

red = bytearray([5,0,0])
green = bytearray([0,5,0])
blue = bytearray([0,0,5])
f = True

while True: #RGB
        try:
                if f:
                        color[:0] = red
                else:
                        color[:0] = green
                f = not f
                color = color[:-3]
                #for x in range(0, 73, 3):
                        #print "[" + str(color[x]) + "," + str(color[x+1]) + "," + str(color[x+2]) + "]",
                #print
                time.sleep(.3)
                spidev.flush()
                spidev.write(color)
        except KeyboardInterrupt:
                lights_out()
        except Exception, e:
                print e