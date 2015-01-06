import time, random
class Xmas_4:
        '''
        init
        All pixels to same color
        Run
        Color of all pixels change from one end to another
        Color changes from both ends to middle, then color changes from middle to ends
        '''
        def __init__(self):
                self.initialize = True
                self.targets = []
                self.end_to_end = True

        def end_to_end(direction="left", pixels):
                time.sleep(.2)
                l = len(pixels)
                for i, pixel in enumerate(pixels):
                        pixel.set_colors(255,0,0)
                return True


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
                while end_to_end(left, pixels):
                        pass


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

                if random.randrange(0,1000) == 0:
                        self.initialize = True
                        return False
                return True