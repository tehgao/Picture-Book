import random

from PIL import Image

class ImageGen(object):
	def __init__(self, w=1024, h=768):
		self.width = w
		self.height = h

	def genImage(self):
		pixels = []

		for i in range(0, self.width * self.height):
			pixels.append((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

		image = Image.new('RGB', (self.width, self.height))
		image.putdata(pixels)
		return image

def main():
	generator = ImageGen(1024, 768)
	generator.genImage.save('test.png')

if __name__ == "__main__": main()
