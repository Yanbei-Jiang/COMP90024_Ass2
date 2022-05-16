"""
Author: Wei Ge - 1074198
        Han Wang - 1041260 
        YanBei Jiang - 1087029
        Yiwen Zhang - 1002781
        Zening Zhang - 1078374
"""
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def sentiment_analysis(text):
    #nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    if scores["neu"] > 0.8:
        #0 indicates = "neu"
        return 0
    elif scores["pos"] > scores["neg"]:
        #1 indicates = "pos"
        return 1
    else:
        #-1 indicates = "neg"
        return -1


def polarity_analysis(text):
    polarity = TextBlob(text).sentiment
    if polarity[1] > 0.5:
        # 0 indicates "subjective"
        return 0
    else:
        # 1 indicates "objective"
        return 1