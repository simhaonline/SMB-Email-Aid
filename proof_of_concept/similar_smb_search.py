#!/usr/bin/python3

# Importing required modules
import requests, json

# Returns a dictionary containing the websites of SMBs similar to the target SMB
# Parameters: business -> Target SMB
#             zipcode -> Zipcode of target SMB
# Output: A dictionary containing the websites of SMBs where:
#         Key -> Name of similar SMB
#         Value -> Website of similar SMB
def getSimilarSMBsWebsites(business: str, zipcode: str, api_key: str) -> dict:

    # Building query
    query = business + ' in ' + zipcode

    # url used to send request for SMBs that are similar to business in zipcode
    broad_search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # url used to search each SMB individually and get their website
    indi_serach_url = "https://maps.googleapis.com/maps/api/place/details/json?"

    # get method of requests module return response object
    response = requests.get(broad_search_url + 'query=' + query + '&key=' + api_key)

    # conversion from json to a python dict
    x = response.json()

    # getting the results from the search
    SMBs = x['results']

    #list to contain the lists of websites
    SMB_websites = {}

    # loop through the SMBs returned, search them individually and put their
    # websites in a a dictionary with the name of the SMB as key
    for i in range(len(SMBs)):
        place_id = SMBs[i]['place_id']
        name = SMBs[i]['name']
        website = requests.get(indi_serach_url + '&key=' + api_key +
                               '&place_id=' + place_id + '&fields=website')
        website_result = website.json()['result']

        # If statement to prevent duplicates and empty websites in dictionary
        if 'website' in website_result and name not in SMB_websites:
            SMB_websites[name] = website_result['website']

    #print(SMB_websites)
    return SMB_websites

# Used for testing, should be deleted
# business = input('Business: ')
# zipcode = input('Zipcode: ')
# getSimilarSMBsWebsites(business, zipcode)
