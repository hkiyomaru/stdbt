from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader_analyzer = SentimentIntensityAnalyzer()

print vader_analyzer.polarity_scores('I am happy')
