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

def main():

    # Filepaths
    original_filename = "unsanitzed_data.txt"
    sanitized_filename = "sanitized_data.txt"

    # Read unsanitized, original data
    try:
        original_file = open(original_filename)
        text = original_file.read()
    finally:
        original_file.close()

    # Sanitize
    text = sanitize(text)

    # Write the result
    try:
        sanitized_file = open(sanitized_filename, "w")
        sanitized_file.write(text)
    finally:
        sanitized_file.close()

if __name__ == '__main__':
    main()
