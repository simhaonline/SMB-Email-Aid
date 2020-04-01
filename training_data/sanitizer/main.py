#!/usr/bin/python3

from sanitize import *

if __name__ == '__main__':

    # Filepaths
    original_filename = "../training_data/marketing_phrases.txt"
    sanitized_filename = "../training_data/sanitized_data.txt"

    # Read unsanitized, original data
    try:
        original_file = open(original_filename)
        text = original_file.read()
    finally:
        original_file.close()

    # Sanitize
    text = sanitize(text)
    #text = sub_org(text, "SMBORG")

    # Write the result
    try:
        sanitized_file = open(sanitized_filename, "w")
        sanitized_file.write(text)
    finally:
        sanitized_file.close()
