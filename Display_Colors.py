from colored import fg, bg, attr
from x256 import x256
import sys

class Display_Colors:
	def restart_line(self):
		sys.stdout.write('\r')
		sys.stdout.flush()

	def print_(self, pixels):
		y = ""
		for pixel in pixels:
			x = pixel.get_colors()
			y += ('%s %s' % (bg(x256.from_rgb(x[0], x[1], x[2])), attr(0)))
		sys.stdout.write(y)
		sys.stdout.flush()
		self.restart_line()