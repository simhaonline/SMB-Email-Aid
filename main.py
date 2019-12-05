#!/usr/bin/python3

from similar_smb_search import *
from web_scrape import *
from find_competitor_phrases import *
import csv

if __name__ == '__main__':
    # Preset keywords
    keywords = ["shop", "free", "%", "select", "deal", "sale", "major", "minimum",
                "terms", "offer", "store", "fast", "pickup", "everything",
                "shipping", "gift", "last", "end", "up to", "save", "feature",
                "product", "top", "clearance", "trending"]

    # User input for industry, zipcode, and desired keywords
    industry = input('\nIndustry: ')
    zipcode = input('\nZipcode: ')
    user_keywords = input('\nKeywords (separate by space): ')
    keywords += user_keywords.split()

    # Fetch a dictionary of business and their website links through Google
    # Maps API
    print('\nSearching for competitor websites...\n\n')
    business_dict = getSimilarSMBsWebsites(industry, zipcode)
    print('Found ' + str(len(business_dict)) + ' websites\n\n')

    # Web scrape the links from above and get useful contents
    print('Web scraping...\n\n')
    competitor_content = ""
    for business_name in business_dict:
        business_URL = business_dict[business_name]
        print(business_URL)
        web_content = getUsefulContent(business_URL)
        competitor_content += web_content

    # NLP: Dictonary for key-value pairs of keyword and phrases that contain
    # the keyword
    print('Fetching phrases...\n\n')
    keyword_to_phrase = find_competitor_phrases(industry, keywords, competitor_content)
    print('Done!\n')

    # Write the key-value pairs to a .txt file
    with open('poc.txt', 'wt') as out:
        pp.pprint(keyword_to_phrase, stream=out)

    # Write the key-value pairs to a .csv file
    with open('poc.csv', 'w') as f:
        for key in keyword_to_phrase.keys():
            f.write("%s, %s\n"%(key, keyword_to_phrase[key]))
