import datetime, time, random

def logstamp():
    return str(datetime.datetime.now()) + ': '

def logtoot(toot):
    #print(logstamp())
    f = open('mastodon.log', 'a')
    f.write(logstamp() + toot + '\n')
    f.close()

def logtweet(tweet):
    f = open('twitter.log', 'a')
    f.write(logstamp() + tweet + '\n')
    f.close()

def random_wait():
    seconds = random.randint(120, 300)
    time.sleep(seconds)
