import tweepy

def api():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_TOKEN = ''
    ACCESS_SECRET = ''
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

def get_tweet_list(api, handle):
    return api.user_timeline(screen_name=handle, exclude_replies=1)

def get_last_tweet(api, handle):
    return api.user_timeline(screen_name=handle, count=1, exclude_replies=1)[0]
