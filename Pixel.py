class Pixel:
	'''
	Pixel
	'''

	def __init__(self):
		self.red = 0
		self.green = 0
		self.blue = 0

	def get_colors(self):
		'''
		Return a bytearray of red, green, blue. The color of the pixel.
		'''
		return bytearray([self.red, self.green, self.blue])

	def get_color(self, color):
		if self.color == "red":
			return self.red
		if self.color == "green":
			return self.green
		return self.blue

	def set_colors(self, red, green, blue):
		'''
		You pass 3 digits
		'''
		self.red = red
		self.green = green
		self.blue = blue

	def set_color(self, color, value):
		if self.color == "red":
			self.red = value
		if self.color == "green":
			self.green = value
		if self.color == "blue":
			self.blue =  value