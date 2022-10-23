import tweepy
import datetime
#from datetime import timezone

API_KEY=''
API_SECRET=''

ACCESS_TOKEN=''
ACCESS_TOKEN_SECRET=''

# Authenticate to Twitter
#auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
#auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
#api = tweepy.API(auth)

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
    


