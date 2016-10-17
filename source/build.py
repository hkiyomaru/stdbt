#!/usr/bin/env python

import json

from utils import stream
from utils import preprocessor
from utils import vader
from utils import select
from utils import sort
from utils import image


class DBBuilder:
    def __init__(self, config_path):
        self.stream_api = stream.StreamAPI(config_path)
        self.sorter = sort.TweetSorter()
        self.preprocessor = preprocessor.Preprocessor()
        self.selector = select.AttributeSelector()
        self.saver = image.ImageSaver()
        self.vader = vader.SentimentAnalyzer()
        self.db = []

    def gather_limit_tweets(self, limit=50000):
        self.tweets_num = 0
        loop = 0
        while self.tweets_num < limit:
            tweet_stream = self.stream_api.stream()
            tweets = self.stream_api.get_tweets(tweet_stream, limit=1000) # Get limit tweets
            print "Tweets:", len(tweets)
            sorted_tweets = self.sorter(tweets) # select tweets which have several images
            print "  Tweets with several images:", len(sorted_tweets)
            selected_tweets = [self.selector(item) for item in sorted_tweets] # extract necessary attribute
            self.insert(selected_tweets)
            print "  Inserted data number:", len(selected_tweets)
            print "Go to next step."
        print "saved tweet:", self.tweets_num

    def insert(self, tweets):
        for tweet in tweets:
            for m in tweet["media"]:
                if self.saver(self.tweets_num, m): # image was saved
                    t = {}
                    t["id"] = self.tweets_num
                    t["text"] = self.preprocessor(tweet["text"])
                    polarity = self.vader(t["text"])
                    t["positive"] = polarity["pos"]
                    t["neutral"] = polarity["neu"]
                    t["negative"] = polarity["neg"]
                    self.db.append(t)
                    self.tweets_num += 1
                else: # image was not saved
                    continue

    def dump(self):
        try:
            f = open('data/image_data.json', 'w')
            json.dump(self.db, f)
            f.close()
            return 1
        except:
            return 0



if __name__ == '__main__':
    dbbuilder = DBBuilder('config/twitter_api_config.json')
    dbbuilder.gather_limit_tweets()
    dbbuilder.dump() # save image data
