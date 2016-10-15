import json
from TwitterAPI import TwitterAPI

def get_config(config_path):
    f = open(config_path)
    config = json.load(f)
    f.close()
    return config

config = get_config('config/twitter_api_config.json')
api = TwitterAPI(
    config["consumer_key"],
    config["consumer_secret"],
    config["access_token"],
    config["access_token_secret"]
)

r = api.request(
    'statuses/sample',
    {
        'language': 'en'
    }
)

for item in r:
        print item["text"]
