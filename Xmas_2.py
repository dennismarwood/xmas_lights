import time, random
class Xmas_2:
        '''
        Twinkle random red and green at random strength.
        '''

        def __init__(self):
                pass

        def display(self, pixels):
                for pixel in pixels:
                        if random.randrange(0,2):
                                pixel.set_colors(random.randrange(0,256), 0, 0)
                        else:
                                pixel.set_colors(0, random.randrange(0,256), 0)
                time.sleep(.3)
                return random.randrange(0,100)