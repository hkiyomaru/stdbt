class TweetSorter:
    """
      Sort out tweets which include image.
    """
    def __init__(self):
        pass

    def __call__(self, tweets):
        tweets = [item for item in tweets if self.sort(item)]
        return tweets

    def sort(self, tweet):
        if "extended_entities" in tweet:
            for media in tweet["extended_entities"]["media"]:
                if "jpg" in media["media_url"]:
                    return tweet
            else:
                return 0
        else:
            return 0
