import time, random
class Xmas_3:
        '''
        Init
        All pixels are lit red or green at some random strenght.
        Run
        Random 1/3 of the pixels are selected to gently twinkle
        '''
        def __init__(self):
                self.initialize = True
                self.targets = []

        def initialize_(self, pixels):
                self.initialize = False
                flag = False
                for pixel in pixels:
                        if flag:
                                pixel.set_colors(random.randrange(1,255), 0, 0)
                        else:
                                pixel.set_colors(0,random.randrange(1,255), 0)
                        flag = not flag
                self.targets = random.sample(range(len(pixels)), len(pixels) / 3)

        def display(self, pixels):
                if self.initialize:
                        self.initialize_(pixels)
                for i in self.targets:
                        c = "green"
                        if pixels[i].get_color("red"):
                                c = "red"
                        x = pixels[i].get_color(c)
                        x += random.randrange(0,5)
                        if x > 255:
                                x = 1
                        pixels[i].set_color(c, x)

                time.sleep(.2)

                if random.randrange(0, 600) == 0:
                        self.initialize = True
                        return False
                return True