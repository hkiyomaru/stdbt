#!/usr/bin/env python

import json

from utils import StreamAPI
from utils import Preprocessor
from utils import SentimentAnalyzer
from utils import AttributeSelector
from utils import TweetSorter
from utils import ImageSaver


class DBBuilder:
    def __init__(self, config_path):
        self.stream_api = StreamAPI.StreamAPI(config_path)
        self.sorter = TweetSorter.TweetSorter()
        self.preprocessor = Preprocessor.Preprocessor()
        self.selector = AttributeSelector.AttributeSelector()
        self.saver = ImageSaver.ImageSaver()
        self.vader = SentimentAnalyzer.SentimentAnalyzer()
        self.db = []
        self.tweets_num = 0

    def gather_limit_tweets(self, limit=200000):
        while self.tweets_num < limit:
            tweet_stream = self.stream_api.stream()
            # Get limit tweets
            tweets = self.stream_api.get_tweets(tweet_stream, stream_limit=10000)
            print "Tweets:", len(tweets)
            # select tweets which have several images
            sorted_tweets = self.sorter(tweets)
            print "  Tweets with several images:", len(sorted_tweets)
            # extract necessary attribute
            selected_tweets = [self.selector(item) for item in sorted_tweets]
            self.insert(selected_tweets)
            print "  Total images number:", self.tweets_num
            self.dump('data/image_data.json')
            print "    Go to next step."
        print "saved tweet:", self.tweets_num

    def insert(self, tweets):
        for tweet in tweets:
            for m in tweet["media"]:
                t = {}
                t["id"] = self.tweets_num
                t["url"] = m
                t["text"] = self.preprocessor(tweet["text"])
                polarity = self.vader(t["text"])
                t["positive"] = polarity["pos"]
                t["neutral"] = polarity["neu"]
                t["negative"] = polarity["neg"]
                self.db.append(t)
                self.tweets_num += 1

    def dump(self, data_path):
        try:
            f = open(data_path, 'w')
            json.dump(self.db, f)
            f.close()
            return 1
        except:
            return 0


if __name__ == '__main__':
    dbbuilder = DBBuilder('config/twitter_api_config.json')
    dbbuilder.gather_limit_tweets()
    dbbuilder.dump('data/image_data.json') # save image data
