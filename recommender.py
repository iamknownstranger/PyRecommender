import tweepy
import pandas as pd
import timeago
import datetime

api_key = "KlZ7E7VDg0rEsZiNMCU22u07V"  # consumer key

api_secret_Key = "VVf5XJKCW9gWQRsu87Lkl6VjC39Rep8G4QSI0I5KcYI19Y9wn5"  # consumer secret

access_token = "1143902557439320064-sfnE7zUdIXnTV6QUL2MH4UH6jVMoNy"

access_token_secret = "rp60MfnpM8yKSUhcnsfI8KQ1biAqIKUOt82mzOWhoXLPj"

auth = tweepy.OAuthHandler(api_key, api_secret_Key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class Recommender:

    def __init__(self):
        #initializing the current time inorder to get the time ago format
        self.time = datetime.datetime.now()

    def get_tweets(self, search_query):
        
        '''Function returns the tweets that are includ the given search query as a list'''
        self.tweets = []
        for tweet in tweepy.Cursor(api.search, q=search_query, lang='en', count=1000, tweet_mode='extended').items(1000):
            if(not tweet.retweeted) and ('RT @' not in tweet.full_text):
                
                # appending the tweet to the list 
                self.tweets.append(
                    [tweet.user.name, '@'+tweet.user.screen_name, timeago.format(tweet.created_at, self.time), tweet.full_text])

        return self.tweets
    
# RecommenderObject = Recommender()
# tweets_about_horror_movies = RecommenderObject.get_tweets("best horror netflix")
