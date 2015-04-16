import Corpus
import ImageGen
import textwrap

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class Alice(object):
	def __init__(self, text_filename):
		self.output = open(text_filename, 'w');
		self.imageGenerator = ImageGen.ImageGen(1024, 768)
		self.textGenerator = Corpus.Generator('alice')

	def createPage(self, image, text):
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype("arial.ttf", 50)

		text_list = textwrap.wrap(text, 40)

		x = 1024*.05
		starting_y = 768*.10

		shadowcolor = "red"
		fillcolor = "black"

		y = starting_y
		while (y < 768-70 and text_list):
			t = text_list.pop(0)
			draw.text((x-1, y-1), t, font=font, fill=shadowcolor)
			draw.text((x+1, y-1), t, font=font, fill=shadowcolor)
			draw.text((x-1, y+1), t, font=font, fill=shadowcolor)
			draw.text((x+1, y+1), t, font=font, fill=shadowcolor)

			draw.text((x, y), t, font=font, fill=fillcolor)
			y = y + 60
		return image

	def createBook(self):
		for i in range(0, 10):
			page = self.createPage(self.imageGenerator.genImage(), self.textGenerator.generateText())
			page.save(str(i) + ".png")

def main():
	alice = Alice('alice_test')
	alice.createBook()

if __name__ == "__main__": main()