#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.arthurspastry.com"
csv_filename = 'scraped_data.csv'

def getHTMLContent(link):
	htmlResponse = requests.get(link)
	soup = BeautifulSoup(htmlResponse.content, 'html.parser')
	return soup


soup = getHTMLContent(URL)
for tag in soup.find_all(True):
	if tag.name == 'p':
		print(tag.contents)
