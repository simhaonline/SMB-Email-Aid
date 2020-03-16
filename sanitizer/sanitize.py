#!/usr/bin/python3

import nltk
import re
import html
from sub_orgname import *

nltk.download('punkt')

def sanitize(data_file):
	try:
		file = open(data_file)
		data = file.read()
		split_data = nltk.tokenize.sent_tokenize(data)
		filename = '../training_data/sanitized_data.txt'
		for i in range(len(split_data)):
			n_phrase = split_data[i].strip()
			n_phrase = re.sub(r'[^\x00-\x7F]+',' ', n_phrase)
			n_phrase = ' '.join(n_phrase.split())
			split_data[i] = n_phrase
		try:
			n_file = open(filename, 'w')
			n_file.write(str(split_data))
		finally:
			n_file.close()
	finally:
		file.close()

def unescape_html(text):
	return html.unescape(text)

# file = input('File: ')
sanitize("../training_data/marketing_phrases.txt")
