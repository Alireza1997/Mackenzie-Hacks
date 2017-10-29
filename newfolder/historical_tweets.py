import got

def main():

    def printTweet(descr, t):
        print(descr)
        print("Username: %s" % t.username)
        print("Retweets: %d" % t.retweets)
        print("Text: %s" % t.text)
        print("Date: %s" % t.date)  
        print("Mentions: %s" % t.mentions)
        print("Hashtags: %s" % t.hashtags)
        print("Geo: %s\n" % t.geo)


    # Example 2 - Get tweets by query search
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('herman').setSince("2017-01-01").setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    tweet = tweets[1]

    for i in range(100):
        printTweet("\n", tweet)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]

if __name__ == '__main__':
    main()