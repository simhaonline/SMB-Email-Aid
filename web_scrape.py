#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse

URL = "https://www.arthurspastry.com"
csv_filename = 'scraped_data.csv'

def getHTMLContent(link):
	htmlResponse = requests.get(link)
	soup = BeautifulSoup(htmlResponse.content, 'html.parser')
	return soup

soup = getHTMLContent(URL)
for paragraph in soup.find_all('p'):
	print(paragraph.text)

#for external_link in soup.find_all('a', href = True):
#	raw = external_link['href']
#	h_name = urllib.parse.urlparse(raw).hostname
#	path = urllib.parse.urlparse(raw).path
#	abs_path = str(h_name) + str(path);
#	print(abs_path)
