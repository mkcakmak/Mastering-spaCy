from collections import Counter 
import spacy 
nlp  = spacy.load("en_core_web_md") 

corpus = open("data/atis_utterances.txt", "r").read().split("\n") 


all_ent_labels = [] 
for sentence in corpus: 
    sentence = sentence.strip()     # strip --> Remove spaces at the beginning and at the end of the string
    if sentence:
        doc = nlp(sentence)
        ents = doc.ents 
        all_ent_labels += [ent.label_ for ent in ents] 

c = Counter(all_ent_labels) 
print(c) 
