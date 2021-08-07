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

#By the way we are keeping that sentiment in such a way
#That 0 means negative and 1 means positive

#-----------------------------importing data1
data1 = load_files('data1/',encoding='utf-8')
data1X,data1Y = data1.data,data1.target
# storing it in pickle file
with open('data1X.pickle','wb') as f:
    pickle.dump(data1X,f)
with open('data1Y.pickle','wb') as f:
    pickle.dump(data1Y,f)
# unpickling file
with open('data1X.pickle','rb') as f:
    data1X = pickle.load(f)
with open('data1Y.pickle','rb') as f:
    data1Y = pickle.load(f)

#-----------------------------importing data2
# i had made a combined data txt file manually
data2 = pd.read_csv("data2\COMBINED_DATA.txt",delimiter='\t')
data2X=list(data2.iloc[:,0].values)
data2Y=data2.iloc[:,1].values
with open('data2X.pickle','wb') as f:
    pickle.dump(data2X,f)
with open('data2Y.pickle','wb') as f:
    pickle.dump(data2Y,f)
# unpickling file
with open('data2X.pickle','rb') as f:
    data2X = pickle.load(f)
with open('data2Y.pickle','rb') as f:
    data2Y = pickle.load(f)

#-----------------------------importing data3
# data 3 is going to be a quite different as its in .review file
# even BeautifulSoup and Elementtree library will have hard time
# so we will use the old method... divide and conquer


#getting subdirectory names in data3
subfolders = [ f.path for f in os.scandir("data3") if f.is_dir() ]
data3X=[]
data3Y=[]

#for negative words
for i in subfolders:
    foldername=i+"\\negative.review"
    with open(foldername, 'r') as f:
        data3 = f.read()
    data3= nltk.sent_tokenize(data3)
    for i in range(len(data3)):
        data3[i]=data3[i].lower()
        data3[i]=re.sub(r'\/review\_text'," SENTENCEEND ",data3[i])
        data3[i]=re.sub(r'review\_text+'," SENTENCESTART ",data3[i])
    data3=" ".join(data3)
started="no"
sentence=[]
temp=[]
words=nltk.word_tokenize(data3)
for i in range(len(words)):
    if words[i] == "SENTENCESTART":
        started="yes"
    if started=="yes":
        temp.append(words[i])
    if words[i]== "SENTENCEEND":
        started="no"
        sentence.append(temp)
        temp=[]
for i in range(len(sentence)):
    sentence[i]=" ".join(sentence[i])
    data3X.append(sentence[i])
    data3Y.append[0]

#for positive
for i in subfolders:
    foldername=i+"\\positive.review"
    with open(foldername, 'r') as f:
        data3 = f.read()
    data3= nltk.sent_tokenize(data3)
    for i in range(len(data3)):
        data3[i]=data3[i].lower()
        data3[i]=re.sub(r'\/review\_text'," SENTENCEEND ",data3[i])
        data3[i]=re.sub(r'review\_text+'," SENTENCESTART ",data3[i])
    data3=" ".join(data3)
started="no"
sentence=[]
temp=[]
words=nltk.word_tokenize(data3)
for i in range(len(words)):
    if words[i] == "SENTENCESTART":
        started="yes"
    if started=="yes":
        temp.append(words[i])
    if words[i]== "SENTENCEEND":
        started="no"
        sentence.append(temp)
        temp=[]
for i in range(len(sentence)):
    sentence[i]=" ".join(sentence[i])
    data3X.append(sentence[i])
    data3Y.append(1)


#changing data3Y into array
data3Y=np.asarray(data3Y)
#saving data3X and data3Y
with open('data3X.pickle','wb') as f:
    pickle.dump(data3X,f)
with open('data3Y.pickle','wb') as f:
    pickle.dump(data3Y,f)
# unpickling file
with open('data3X.pickle','rb') as f:
    data3X = pickle.load(f)
with open('data3Y.pickle','rb') as f:
    data3Y = pickle.load(f)


#--------------------------SAVING THE DATASET

#MERGING DATA1x,2x,3x and 1y,2y,3y
combined_dataX=[]
combined_dataY=[]
data1Y=list(data1Y)
data2Y=list(data2Y)
data3Y=list(data3Y)
for i in range(len(data1X)):
    combined_dataX.append(data1X[i])
    combined_dataY.append(data1Y[i])
for i in range(len(data2X)):
    combined_dataX.append(data2X[i])
    combined_dataY.append(data2Y[i])
for i in range(len(data3X)):
    combined_dataX.append(data3X[i])
    combined_dataY.append(data3Y[i])

#saving the combined data but first changing Y in array
combined_dataY=np.asarray(combined_dataY)
#saving
with open('combined_dataX.pickle','wb') as f:
    pickle.dump(combined_dataX,f)
with open('combined_dataY.pickle','wb') as f:
    pickle.dump(combined_dataY,f)
# unpickling file
with open('combined_dataX.pickle','rb') as f:
    combined_dataX = pickle.load(f)
with open('combined_dataY.pickle','rb') as f:
    combined_dataY = pickle.load(f)

# AND HERE WE ARE DONE WITH COLLECTING DATASET... now we have to preprocess it