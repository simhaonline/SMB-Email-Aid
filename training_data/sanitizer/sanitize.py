#!/usr/bin/python3

import os
import nltk
import re
import html

def sanitize(text):

    nltk.download('punkt')
    split_data = nltk.tokenize.sent_tokenize(text)

    text = ""

    for i in range(len(split_data)):
        phrase = split_data[i].strip()
        phrase = re.sub(r'[^\x00-\x7F]+',' ', phrase)
        phrase = ' '.join(phrase.split())

        if contain_junk(phrase):
            pass
        else:
            print(f"{phrase}\n")
            text = text + phrase

    text = html.unescape(text)

    return text

def contain_junk(text):
    if "COVID"                  in text or \
       "Jazzberry"              in text or \
       "yazzberryyam@gmail.com" in text or \
       "click"                  in text or \
       "Click"                  in text or \
       "All Rights"             in text:
        return True
    else:
        return False