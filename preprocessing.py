import numpy as np
import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
from bs4 import BeautifulSoup
import lxml
import os

# unpickling the saved file 
with open('combined_dataX.pickle','rb') as f:
    combined_dataX = pickle.load(f)
with open('combined_dataY.pickle','rb') as f:
    combined_dataY = pickle.load(f)

#preprocessing data
corpus=[]
for i in range(len(combined_dataX)):
    review=nltk.word_tokenize(combined_dataX[i])
    review=[word for word in review if word!="SENTENCESTART" and word!="SENTENCEEND"]
    review=" ".join(review)
    review.lower()
    review=re.sub(r'n\'t','not',review)
    review=re.sub(r'\'s','is',review)
    review=re.sub(r'\'ll','will',review)
    review=re.sub(r'\'d','would',review)
    review=re.sub(r'\'re','are',review)
    review=re.sub(r'\'ve','have',review)
    review=re.sub(r'\'m','am',review)
    review=re.sub(r'[\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\:\;\"\'\<\>\/\~\`]',' ',review)
    review=re.sub(r'\s+\,',',',review)
    review=re.sub(r'\s+\.','.',review)
    review=re.sub(r'\s+\?','?',review)
    review=re.sub(r'\s+\!','!',review)
    review=re.sub(r'[0-9]',' ',review)
    review=re.sub(r'\s+',' ',review)
    corpus.append(review)

#saving the processed data
with open('PROCESSED_DATA.pickle','wb') as f:
    pickle.dump(corpus,f)
with open('PROCESSED_DATA.pickle','rb') as f:
    corpus=pickle.load(f)
#also combined_dataY is same for process_data
with open('PROCESSED_LABEL.pickle','wb') as f:
    pickle.dump(combined_dataY,f)
with open('PROCESSED_LABEL.pickle','rb') as f:
    label=pickle.load(f)

