import tweepy
from tweepy import streaming
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json

consumer_key = "3K5VmYbYQd3Ckx9Ag6QNOTpzd"
consumer_secret = "EjYkY9kNXYZ4JmpJ8WHPZdpZL8BhUcxfuon8VmGNYRXmuS6eYy"
access_token = "921571447000231937-ojxGCndOQfnarGPghjqDeL6RkBGPYgH"
access_secret = "St582XvLyKL7mzVb1FZGA59VnefQjhJATdNvJpRV05bPh"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('FILENAME.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

#Set the hashtag to be searched
twitter_stream = tweepy.Stream(auth, MyListener())
twitter_stream.filter(track=['#bellletstalk'])
