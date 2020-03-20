#!/usr/bin/python3

'''
    Takes a text and a company name and replaces all org's in the text with the
    company name.
    Uses spacy model.
'''

from functools import reduce
import spacy
import os

NLP = spacy.load('en_core_web_lg')

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


sub_org("Google is not the best Microsoft out there.", "Vans")
