import json


def old_tweet_analysis(tweet_json):
    tweet_obj = json.load(tweet_json)
    text = tweet_obj["doc"]["text"]
    return process_tweet(text)


def new_tweet_analysis(tweet_json):
    tweet_obj = json.load(tweet_json)
    text = tweet_json["doc"]["text"]
    return process_tweet(text)


def process_tweet(text):
    processed_text = preprocess(text)
    sentiment = sentiment_analysis(processed_text)
    tweet_obj["sentiment"] = sentiment
    polarity = polarity_analysis(processed_text)
    tweet_obj["polarity"] = polarity
    topic = topic_extraction(processed_text)
    tweet_obj["topic"] = topic
    return json.dump(tweet_obj)


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)



old_tweet_analysis()