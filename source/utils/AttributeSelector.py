class AttributeSelector:
    def __init__(self):
        pass

    def __call__(self, tweet):
        t = {}
        t["text"] = tweet["text"]
        t["media"] = []
        for m in tweet["extended_entities"]["media"]:
            if "jpg" in m["media_url"]:
                t["media"].append(m["media_url"])
        return t
