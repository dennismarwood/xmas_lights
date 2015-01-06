import time
class Strand_test_1:
        '''
        Pulse red then green and then blue.
        '''
        def __init__(self):
                self.x = [255, 0, 0]

        def display(self, pixels): 
                for pixel in pixels:
                        pixel.set_colors(self.x[0], self.x[1], self.x[2])
                time.sleep(1)
                print self.x
                self.x.insert(0, self.x.pop(-1))
                return True
