from os import access
import tweepy
import re
import pickle
from tweepy import OAuthHandler

class bot():
    consumer_key=""
    consumer_secret=""
    access_token=""
    access_secret=""
    def __init__(self,c_key,c_secret,a_token,a_secret):
        self.consumer_key=c_key
        self.consumer_secret=c_secret
        self.access_token=a_token
        self.access_secret=a_secret
        self.authh=OAuthHandler(self.consumer_key,self.consumer_secret)
        self.authh.set_access_token(self.access_token,self.access_secret)
        api=tweepy.API(self.authh,timeout=10)
        with open('TFIDF.pickle','rb') as f:
            self.vectorizer=pickle.load(f)
        with open('CLASSIFIER.pickle','rb') as f:
            self.classifier=pickle.load(f)

    def analyse(self,argument,items):
        list_tweets=[]
        query=argument[0]
        if len(argument)==1:
            for status in tweepy.Cursor(self.api.search,q=query+"-filter:retweets",lang='en',result_type='recent').items(items):
                list_tweets.append(status.text)
        #processing the tweets
        total_pos=0
        total_neg=0
        neg=[]
        pos=[]
        for tweet in list_tweets:
            tweet=re.sub(r"^https://t.co/[a-zA-Z0-9]*\s"," ",tweet)
            tweet=re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s"," ",tweet)
            tweet=re.sub(r"\s+http://t.co/[a-zA-Z0-9]*$"," ",tweet)
            tweet=tweet.lower()
            tweet=re.sub(r"that's","that is",tweet)
            tweet=re.sub(r"there's","there is",tweet)
            tweet=re.sub(r"what's","what is",tweet)
            tweet=re.sub(r"where's","where is",tweet)
            tweet=re.sub(r"it's","it is",tweet)
            tweet=re.sub(r"who's","who is",tweet)
            tweet=re.sub(r"i'm","i am",tweet)
            tweet=re.sub(r"she's","she is",tweet)
            tweet=re.sub(r"he's","ho is",tweet)
            tweet=re.sub(r"they're","they are",tweet)
            tweet=re.sub(r"ain't","am not",tweet)
            tweet=re.sub(r"wouldn't","would not",tweet)
            tweet=re.sub(r"shouldn't","should not",tweet)
            tweet=re.sub(r"can't","can not",tweet)
            tweet=re.sub(r"couldn't","could not",tweet)
            tweet=re.sub(r"won't","will not",tweet)
            tweet=re.sub(r"\W"," ",tweet)
            tweet=re.sub(r"\d"," ",tweet)
            tweet=re.sub(r"\s+[a-z]\s+"," ",tweet)
            tweet=re.sub(r"\s+[a-z]$"," ",tweet)
            tweet=re.sub(r"^[a-z]\s+"," ",tweet)
            tweet=re.sub(r"\s+"," ",tweet)
            sentiment=self.classifier.predict(self.vectorizer.transform([tweet]).toarray())
            if sentiment==0:
                total_neg+=1
                neg.append(tweet)
            else:
                total_pos+=1
                pos.append(tweet)
        return(total_neg,total_pos,neg,pos)