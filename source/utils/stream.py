import json
from TwitterAPI import TwitterAPI


class StreamAPI:
    def __init__(self, config_path):
        self.set_api(config_path)

    def set_api(self, config_path):
        config = self.get_config(config_path)
        self.api = TwitterAPI(
            config["consumer_key"],
            config["consumer_secret"],
            config["access_token"],
            config["access_token_secret"])

    def get_config(self, config_path):
        f = open(config_path)
        config = json.load(f)
        f.close()
        return config

    def stream(self):
        r = self.api.request(
            'statuses/sample',
            {
                'language': 'en'
            })
        return r

    def get_tweets(self, tweet_stream, limit=100):
        tweets = []
        count = 0
        for item in tweet_stream:
            if count >= limit:
                break
            else:
                tweets.append(item)
                count += 1
        return tweets


if __name__ == '__main__':
    stream_api = StreamAPI('../config/twitter_api_config.json')
    tweets = stream_api.stream()
    for item in stream_api.get_tweets(tweets):
        for key, value in item.items():
            print "*", key
            print " --- ", value
