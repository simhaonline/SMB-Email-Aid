#!/usr/bin/python3

from similar_smb_search import *
from web_scrape import *
from find_competitor_phrases import *
import csv

if __name__ == '__main__':
    # preset keywords
    keywords = ["shop", "free", "%", "select", "deal", "sale", "major", "minimum",
                "terms", "offer", "store", "fast", "pickup", "everything",
                "shipping", "gift", "last", "end", "up to", "save", "feature",
                "product", "top", "clearance", "trending"]
    industry = input('Industry: ')
    zipcode = input('Zipcode: ')
    user_keywords = input('Keywords (separate by space): ')
    keywords += user_keywords.split()
    business_dict = getSimilarSMBsWebsites(industry, zipcode)
    competitor_content = ""
    for business_name in business_dict:
        business_URL = business_dict[business_name]
        print(business_URL)
        web_content = getUsefulContent(business_URL)
        competitor_content += web_content

    keyword_to_phrase = find_competitor_phrases(industry, keywords, competitor_content)

    with open('poc.csv', 'w') as f:
        for key in keyword_to_phrase.keys():
            f.write("%s, %s\n"%(key, keyword_to_phrase[key]))
