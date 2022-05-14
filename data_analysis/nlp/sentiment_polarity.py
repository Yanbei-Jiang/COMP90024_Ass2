import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def sentiment_analysis(text):
    #nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    if scores["neu"] > 0.8:
        return "neu"
    elif scores["pos"] > scores["neg"]:
        return "pos"
    else:
        return "neg"


def polarity_analysis(text):
    polarity = TextBlob(text).sentiment
    if polarity[1] > 0.5:
        return "subjective"
    else:
        return "objective"