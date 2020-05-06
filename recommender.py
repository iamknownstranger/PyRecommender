import tweepy
import pandas as pd
import timeago
import datetime

# api keys
api_key = "XXXXXXXXXXXXXXXXXXXXXX"  # consumer key

api_secret_Key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # consumer secret

access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


# Tweepy Handler
auth = tweepy.OAuthHandler(api_key, api_secret_Key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class Recommender:

    def __init__(self):
        #initializing the current time inorder to get the time ago format
        self.time = datetime.datetime.now()

    def get_tweets(self, search_query):
        
        ''' Function returns the tweets that are includ the given search query as a list '''
        self.tweets = []

        # query api for tweets
        for tweet in tweepy.Cursor(api.search, q=search_query, lang='en', count=1000, tweet_mode='extended').items(1000):
            if(not tweet.retweeted) and ('RT @' not in tweet.full_text):
                
                # appending the tweet to the list 
                self.tweets.append(
                    [tweet.user.name, '@'+tweet.user.screen_name, timeago.format(tweet.created_at, self.time), tweet.full_text])

        return self.tweets

# for testing purposes 
# RecommenderObject = Recommender()
# tweets_about_horror_movies = RecommenderObject.get_tweets("best horror netflix")
