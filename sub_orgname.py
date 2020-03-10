import spacy
from functools import reduce

nlp = spacy.load('en_core_web_lg')

def sub_org(text, company):
    doc = nlp(text)
    names_in_text = [(entity.text, company)  for entity in doc.ents if entity.label_ in ['ORG']]
    print(names_in_text)

    replaced_text = reduce(lambda x, kv: x.replace(*kv), names_in_text, text)
    print(replaced_text)


sub_org("Google is not the best Microsoft out there.", "Vans")
