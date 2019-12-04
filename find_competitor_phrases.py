import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import argparse
import collections
from collections import defaultdict
import pprint as pp


# downloading NLTK parsing / tokenising libraries -- uncomment if not
# already downloaded
nltk.download('punkt')
nltk.download('wordnet')


# Returns a dictionary containing of preset keywords : list of phrases from
# competitor sites (web scraped) containing keyword
# Parameters: keywords -> preset keywords, user can add to these via
#             command line
# Output: A dictionary containing keywords : phrases
#  		  Key -> specific keyword
#         Value -> list of strings (phrases) from competitor websites
def find_competitor_phrases(industry, keywords, competitor_documents):
	keyword_to_sent = defaultdict(list)
 	# separate text from all documents into list of sentences
	sent_tokenized_text = sent_tokenize(competitor_documents)
	for sent in sent_tokenized_text:
		for keyword in keywords:
			if keyword in sent:
				keyword_to_sent[keyword].append(sent)
	return keyword_to_sent


# accumulate all webscraped text from competitor homepages
# competitor_documents = []
# cwd = os.getcwd()+"/nltk_documents"
#
# for filename in os.listdir(cwd):
# 	current = os.path.join(cwd, filename)
# 	sample_text = ""
# 	with open(current, 'r') as file:
# 		sample_text += file.read().replace('\n', ' ')
# 	competitor_documents.append(sample_text)


# retrieve user input from command line for indsutry and additional keywords
# industry = ""
# parser = argparse.ArgumentParser(description="Retrieve dictionary of marketing terms and scraped phrases")
# parser.add_argument('-i', type=str, help="Enter industry as a sinngle string", required=True)
# parser.add_argument('-k', action='append', help="Enter keywords in sequence, each separated by -k", required=True)
# for _, arg in parser.parse_args()._get_kwargs():
# 	if arg:
# 		if type(arg) is list:
# 			keywords += arg
# 		else:
# 			industry = arg

# pp.pprint(find_competitor_phrases(industry, keywords, competitor_documents))




# IGNORE -- NLTK TESTS:
# sent_tokenized_text = sent_tokenize(sample_text)
# # for sent in sent_tokenized_text:
# # 	print("SENTENCE:")
# # 	print(sent)
# # 	print("\n")

# # word_tokenized_text = word_tokenize(sample_text)
# # for word in word_tokenized_text:
# # 	print("WORD:")
# # 	print(word)
# # 	print("\n")

# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# tokens = word_tokenize(sample_text)


# lemmatizer = WordNetLemmatizer()
# tokens = [lemmatizer.lemmatize(token) for token in tokens]
# # print(tokens)

# # nltk.download('stopwords')
# stopwords = set(stopwords.words('english'))
# new_stopwords = ["hello", "test"]
# stopwords = stopwords.union(new_stopwords)
# tokens = [token for token in tokens if token not in stopwords]

# term_freq_scores = defaultdict(int)
# term_freq_scores = collections.Counter(tokens)
