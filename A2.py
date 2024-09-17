#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 1")
print() #Print space
#import relevant modules
import spacy
import re
from collections import Counter
import time

start=time.time()

with open('textcsv1.txt') as file:
    text = file.read()
sentences = re.split(r'(?<=[.!?]) +', text) #split the text into a list of sentences in order to use nlp.pipeline. 
#Punctuation and numbers were not removed from the text as this interferes with spacy

nlp = spacy.load("en_ner_bc5cdr_md") #this model detects drugs and diseases

drugs = [] #Each drug will be stored here
disease = [] #each disease will be stored here

for doc in  nlp.pipe(sentences,  disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]): #language processing, unnecessary features disabled to speed up process
    for ent in doc.ents:
        if ent.label_=='CHEMICAL':
            drugs.append(ent.text) #entities labeled CHEMICAL are stored here
        if ent.label_=='DISEASE':
            disease.append(ent.text) #entities labeled DISEASE are stored here

#count the number of each type of drug and disease found
drugscount = Counter(drugs)
diseasecount = Counter(disease)

#show the 10 most common drugs and diseases

print(dict(drugscount.most_common(10)))
print(dict(diseasecount.most_common(10)))

print("--- %s seconds ---" % (time.time() - start))
