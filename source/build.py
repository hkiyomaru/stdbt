#!/usr/bin/env python

from utils import stream
from utils import preprocessor
from utils import vader
from utils import select
from utils import sort


class DBBuilder:
    def __init__(self, config_path):
        self.stream_api = stream.StreamAPI(config_path)
        self.tweet_stream = self.stream_api.stream()
        self.sorter = sort.TweetSorter()
        self.preprocessor = preprocessor.Preprocessor()
        self.selector = select.AttributeSelector()
        self.vader = vader.SentimentAnalyzer()
        self.db = []

    def set_limit(self, limit):
        self.limit = limit

    def stream(self):
        tweets = self.stream_api.get_tweets(self.tweet_stream)
        sorted_tweets = self.sorter(tweets)
        selected_tweets = [self.selector(item) for item in sorted_tweets]
        return selected_tweets

if __name__ == '__main__':
    dbbuilder = DBBuilder('config/twitter_api_config.json')
    for item in dbbuilder.stream():
        print item
        print "---"
