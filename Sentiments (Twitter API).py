import tweepy

import csv

from textblob import TextBlob
from Settings import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

word = raw_input('Enter the word to find sentiments about: ') #Change to input if using Python3

public_tweets = api.search(word)

with open('Tweet_Sentiments', 'w') as pointer:
	newFileWriter = csv.writer(pointer)
	newFileWriter.writerow(['Tweet', 'Label'])


positive_tweets = 0.0
total_tweets = 0.0

for tweet in public_tweets:

	analysis = TextBlob(tweet.text)

	total_tweets += 1.0

	if analysis.sentiment.polarity > 0:
		Label = 'POSITIVE'
		positive_tweets += 1.0
	else :
		Label = 'NEGATIVE'


	with open('Tweet_Sentiments', 'a') as pointer:
		newFileWriter = csv.writer(pointer)
		newFileWriter.writerow([ tweet.text.encode('utf-8') , Label])



if positive_tweets/total_tweets >0.8:
	print('Tweeters love ' + word)

elif positive_tweets/total_tweets > 0.5:
	print('Tweeters have good things to say about ' + word)

elif positive_tweets/total_tweets > 0.3:
	print('Tweeters don\'t really like ' + word)
else:
	print('Tweeters hate ' + word)
