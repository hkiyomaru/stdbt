from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def __call__(self, string):
        return self.analyzer.polarity_scores(string)

if __name__ == '__main__':
    analyzer = SentimentAnalyzer()
    string = "I'm happy!!!"
    print "polarity:", analyzer(string)
