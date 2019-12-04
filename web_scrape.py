#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import urllib.parse

def getHTMLContent(link):
    htmlResponse = requests.get(link)
    soup = BeautifulSoup(htmlResponse.content, 'html.parser')
    return soup

def getUsefulContent(link):
    soup = getHTMLContent(link)
    useful_content = ""
    for paragraph in soup.find_all('p'):
        useful_content += paragraph.text
    return useful_content

#for external_link in soup.find_all('a', href = True):
#	raw = external_link['href']
#	h_name = urllib.parse.urlparse(raw).hostname
#	path = urllib.parse.urlparse(raw).path
#	abs_path = str(h_name) + str(path);
#	print(abs_path)
