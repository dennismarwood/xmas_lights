#!/usr/bin/python

import random, time, sys
import Pixel, Xmas_1, Xmas_2, Xmas_3, Strand_test_1

if 'no_spidev' not in sys.argv: 
        spidev = file("/dev/spidev0.0", "wb")
num_pixels = 1

pixels = [Pixel.Pixel() for i in range(num_pixels)]
#d_c = Display_Colors.Display_Colors()
xmas_1 = Xmas_1.Xmas_1()
xmas_2 = Xmas_2.Xmas_2()
xmas_3 = Xmas_3.Xmas_3()
t_1 = Strand_test_1.Strand_test_1()

def write_spidev(x):
        '''
        load bytearry into pixels
        '''
        if 'no_spidev' in sys.argv:
                return
        spidev.write(x)
        spidev.flush()

def lights_out():
        write_spidev(bytearray([0]) * (num_pixels * 3))
        print "\nturning off lights."
        sys.exit(0)

def print_pixels():
        print "red:" + str(pixels[0].get_color("red"))
        print "green:" + str(pixels[0].get_color("green"))
        print "blue:" + str(pixels[0].get_color("blue"))
        x = bytearray()
        for pixel in pixels:
                x += pixel.get_colors()
        for y in x:
                print y,
        print
        write_spidev(x)
        #d_c.print_(pixels)
while True:
        try:
                while t_1.display(pixels):
                        print_pixels()  
        except KeyboardInterrupt:
                lights_out()
        except Exception, e:
                print e

lights_out()