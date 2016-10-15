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


if __name__ == '__main__':
    stream_api = StreamAPI('../config/twitter_api_config.json')
    tweets = stream_api.stream()
    for item in tweets:
            print item["text"]
