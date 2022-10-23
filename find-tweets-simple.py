#this code only brings 100 tweets at one time. If yoy want more than 100 tweets, lookout for another file in same repo named "advanced_tweets_pull.py"

import tweepy
import datetime


API_KEY=''
API_SECRET=''

ACCESS_TOKEN=''
ACCESS_TOKEN_SECRET=''


auth = tweepy.auth.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
q='Content Creation'
q1='infotainment reels'
q2='content ideas -filter:retweets'

search_results = api.search_tweets(q=q2, count=100,result_type='latest')

l=[]
for tweet in search_results:
    if (datetime.datetime.now(datetime.timezone.utc) - tweet.created_at).days < 1:      #get only tweets which are one day old
        l.append(tweet.created_at)
    


