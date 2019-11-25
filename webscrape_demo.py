import requests 
from bs4 import BeautifulSoup
import csv

URL = "https://www.danishpastryhouse.com"
csv_filename = 'scraped_data.csv'

result = requests.get(URL)
parsed_result = BeautifulSoup(result.content, 'html5lib')

competitor_data = []

data_table = parsed_result.find('div', attrs = {'id': 'et-main-area'})

for row in data_table.findAll('div', attrs={'class': 'et_pb_promo_description'}):
	curr_text = {}
	curr_text['content'] = row.get_text()
	competitor_data.append(curr_text)


with open(csv_filename, 'w') as f:
	f.write("Content")
	for content_dict in competitor_data:
		for key in content_dict.keys():
			f.write("%s"%(content_dict[key].encode("utf-8")))

