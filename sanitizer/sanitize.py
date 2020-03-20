#!/usr/bin/python3

from functools import reduce
import spacy
import os
import nltk
import re
import html

NLP = spacy.load('en_core_web_lg')

'''
    Takes a text and a company name and replaces all org's in the text with the
    company name.
    Uses spacy model.
'''
def sub_org(text, company):
    '''
        sub_org: substitute all occurances of an ORG in the text with the given
                    company
    '''
    doc = NLP(text)
    names_in_text = [(entity.text, company)  for entity in doc.ents if entity.label_ in ['ORG']]
    print(names_in_text)

    replaced_text = reduce(lambda x, kv: x.replace(*kv), names_in_text, text)
    print(replaced_text)

def sanitize(text):

	nltk.download('punkt')

	split_data = nltk.tokenize.sent_tokenize(text)

	text = ""

	for i in range(len(split_data)):
		phrase = split_data[i].strip()
		phrase = re.sub(r'[^\x00-\x7F]+',' ', phrase)
		phrase = ' '.join(phrase.split())
		text = text + phrase

	text = unescape_html(text)

	return text

def unescape_html(text):
	return html.unescape(text)
