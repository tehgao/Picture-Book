"""
Alvin Gao
corpus.py

This script takes in a corpus and generates pseudorandom sentences which (hopefully) bear some
resemblence to the corpus using Markov chains.

"""

import random
import nltk
import codecs
import pprint

class Generator(object):
	def __init__(self, filename):
		self.dictionary = {}
		self.file = codecs.open(filename, 'r')
		self.corpus = self.getCorpus()
		self.length = len(self.corpus)
		self.buildDictionary()

	def getCorpus(self):
		self.file.seek(0)
		raw_text = self.file.read()
		tokens = nltk.word_tokenize(raw_text)
		return tokens

	def triples(self):
		if len(self.corpus) < 3:
			return # need more than three to generate a tuple!

		for i in range(len(self.corpus) - 2):
			yield (self.corpus[i], self.corpus[i+1], self.corpus[i+2])

	def buildDictionary(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.dictionary:
				self.dictionary[key].append(w3)
			else:
				self.dictionary[key] = [w3]

	def generateText(self):
		sampleLength = random.randint(75,85)
		seed = random.randint(0, self.length - 3)
		seed_word, next_word = self.corpus[seed], self.corpus[seed + 1]

		w1, w2 = seed_word, next_word
		words = []
		for i in xrange(sampleLength):
			words.append(w1)
			w1, w2 = w2, random.choice(self.dictionary[(w1, w2)])
		words.append(w2)

		pprint.pprint(self.dictionary)
		return ' '.join(words)