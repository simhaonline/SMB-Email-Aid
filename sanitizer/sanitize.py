#!/usr/bin/python3

import nltk
import re
import html
from sub_orgname import *

def sanitize(text):

	nltk.download('punkt')

	split_data = nltk.tokenize.sent_tokenize(text)

	for i in range(len(split_data)):
		n_phrase = split_data[i].strip()
		n_phrase = re.sub(r'[^\x00-\x7F]+',' ', n_phrase)
		n_phrase = ' '.join(n_phrase.split())
		split_data[i] = n_phrase
	return str(split_data)

def unescape_html(text):
	return html.unescape(text)

# file = input('File: ')
def main():
	file = open("../training_data/marketing_phrases.txt")
	text = file.read()
	text = sanitize(text)
	text = unescape_html(text)

	sanitized_filename = "../training_data/sanitized_data.txt"
	try:
		sanitized_file = open(sanitized_filename, "w")
		sanitized_file.write(text)
	finally:
		sanitized_file.close()

main()
