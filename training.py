import numpy as np
import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
#importing data and label
with open('PROCESSED_DATA.pickle','rb') as f:
    corpus=pickle.load(f)
with open('PROCESSED_LABEL.pickle','rb') as f:
    label=pickle.load(f)
#initialising TFIDF vectorizer
vectorizer=TfidfVectorizer(max_features=20000,min_df=2,max_df=0.95,stop_words=stopwords.words('english'))
#transform the data for vectorizer
X=vectorizer.fit_transform(corpus).toarray()
#creating train and test data sets
text_train,text_test,label_train,label_test= train_test_split(X,label,test_size=0.1,random_state=0)
#training the model
classifier=LogisticRegression()
classifier.fit(text_train,label_train)
label_pred=classifier.predict(text_test)
cm=confusion_matrix(label_test,label_pred)
#save the vectorizer
with open('TFIDF.pickle','wb') as f:
    pickle.dump(vectorizer,f)
#save the classifier
with open('CLASSIFIER.pickle','wb') as f:
    pickle.dump(classifier,f)

#testing one sample
sample=["Elon musk just launched something amazing!!!!!"]
sample=vectorizer.transform(sample).toarray()
print(classifier.predict(sample))
