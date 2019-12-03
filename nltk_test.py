import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('wordnet')
import argparse
import collections
from collections import defaultdict
import pprint as pp



keywords = ["shop", "free", "%", "select", "deal", "sale", "major", "minimum", "terms", "offer", "store", "fast", "pickup", "everything", "shipping", "gift", "last", "end", "up to", "save", "feature", "product", "top", "clearance", "trending"]
industry = ""

parser = argparse.ArgumentParser(description="Retrieve dictionary of marketing terms and scraped phrases")
parser.add_argument('-i', type=str, help="Enter industry as a sinngle string", required=True)
parser.add_argument('-k', action='append', help="Enter keywords in sequence, each separated by -k", required=True)
for _, arg in parser.parse_args()._get_kwargs():
	if arg:
		if type(arg) is list:
			keywords += arg
		else:
			industry = arg


documents = []
cwd = os.getcwd()+"/nltk_documents"

for filename in os.listdir(cwd):
	current = os.path.join(cwd, filename)
	sample_text = ""
	with open(current, 'r') as file:
		sample_text += file.read().replace('\n', ' ')
	documents.append(sample_text)

keyword_to_sent = defaultdict(list)
for document in documents:
	sent_tokenized_text = sent_tokenize(document)
	for sent in sent_tokenized_text:
		for keyword in keywords:
			if keyword in sent:
				keyword_to_sent[keyword].append(sent)

pp.pprint(keyword_to_sent)


# NLTK Tests:
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