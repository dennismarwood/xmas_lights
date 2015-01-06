import time, random
class Xmas_1:
        '''
        Xmas_1. Alternating red and green down the wire. They move down the wire.
        '''

        def __init__(self):
                self.initialize = True

        def initialize_(self, pixels):
                self.initialize = False
                flag = False
                for pixel in pixels:
                        if flag:
                                pixel.set_colors(255, 0, 0)
                        else:
                                pixel.set_colors(0,255, 0)
                        flag = not flag

        def display(self, pixels):
                if self.initialize:
                        self.initialize_(pixels)
                
                pixels.pop()
                x = pixels[1]
                pixels.insert(0,x)
                
                time.sleep(1)
                
                if random.randrange(0, 120) == 0:
                        self.initialize = True
                        return False
                return True