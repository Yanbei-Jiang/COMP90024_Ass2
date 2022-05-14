import json
from nlp.sentiment_polarity import *
#from topic_extraction import *

def old_tweet_analysis(tweet_obj):
    text = tweet_obj["doc"]["text"]
    coordinates = tweet_obj["doc"]["place"]["bounding_box"]["coordinates"][0]
    area = filter_area(coordinates)
    tweet_obj["melbourne_area"] = area
    processed_text = preprocess(text)
    sentiment = sentiment_analysis(processed_text)
    tweet_obj["sentiment"] = sentiment
    polarity = polarity_analysis(processed_text)
    tweet_obj["polarity"] = polarity
    return tweet_obj


def new_tweet_analysis(tweet_obj):
    for key in tweet_obj.keys():
        # only look at the third key (i.e. "Hoppers_Crossing_1522304716188700672_stream")
        if key != "_id" and key != "_rev" and key !="id":
            coordinates = tweet_obj[key]["place"]["bounding_box"]["coordinates"][0]
            area = filter_area(coordinates)
            new_tweet_obj = tweet_obj[key]
            new_tweet_obj["melbourne_area"] = area
            if "extended_tweet" in tweet_obj[key].keys():
                text = tweet_obj[key]["extended_tweet"]["full_text"]
                break
            else:
                text = tweet_obj[key]["text"]
                break

    processed_text = preprocess(text)
    sentiment = sentiment_analysis(processed_text)
    new_tweet_obj["sentiment"] = sentiment
    polarity = polarity_analysis(processed_text)
    new_tweet_obj["polarity"] = polarity
    return new_tweet_obj


def filter_area(coordinates):
    melbourne_city = [144.913581,-37.839086,144.994266,-37.781922]
    melbourne_kew = [144.999392,-37.855040,145.141140,-37.786685]
    Hoppers_Crossing = [144.633666,-37.974500,144.913581,-37.694900]

    left_bound = coordinates[0][0]
    right_bound = coordinates[2][0]
    top_bound = coordinates[1][1]
    down_bound = coordinates[0][1]
    center = [(left_bound+right_bound)/2, (top_bound+down_bound)/2]
    coordinates.append(center)
    for coordinate in coordinates:
        if Hoppers_Crossing[0] <= coordinate[0] <= Hoppers_Crossing[2] and Hoppers_Crossing[1] <= coordinate[1] <= Hoppers_Crossing[3]:
            return "Hoppers_Crossing"
        elif melbourne_kew[0] <= coordinate[0] <= melbourne_kew[2] and melbourne_kew[1] <= coordinate[1] <= melbourne_kew[3]:
            return "melbourne_kew" 
        elif melbourne_city[0] <= coordinate[0] <= melbourne_city[2] and melbourne_city[1] <= coordinate[1] <= melbourne_city[3]:
            return "melbourne_city"

    return "other"


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        if not t.startswith('@') and not t.startswith('http'):
            new_text.append(t)
    
    return " ".join(new_text)





