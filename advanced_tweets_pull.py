import tweepy

#Put your Bearer Token in the parenthesis below
client = tweepy.Client(bearer_token='#')

# Get tweets that contain the hashtag #petday
# -is:retweet means I don't wantretweets
# lang:en is asking for the tweets to be in english
query = 'Content Creation -is:retweet lang:en'
q='content ideas -is:retweet lang:en'
tweets = tweepy.Paginator(client.search_recent_tweets, query=q,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=500)

l=[]
for tweet in tweets:
    l.append(tweet.text)
    #if len(tweet.context_annotations) > 0:
    #   print(tweet.context_annotations)
