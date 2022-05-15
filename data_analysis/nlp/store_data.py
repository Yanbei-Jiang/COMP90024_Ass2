import sys
sys.path.append("..\crawler")
from db_load_data import *
from nlp.analysis import *
from itertools import zip_longest

def main():
    initialize_couchdb()
    old_tweets = get_spec_db("old_tweets")
    original_tweets = get_spec_db("original_tweets")
    # if len(old_tweets) > 0 and len(original_tweets) > 0:
    #     for tweet_old, tweet_new in zip(old_tweets,original_tweets):
    #         processed_old = old_tweet_analysis(old_tweets[tweet_old])
    #         processed_new = new_tweet_analysis(original_tweets[tweet_new])
            
    #         store_to_processed_db(processed_old)
    #         store_to_processed_db(processed_new)

    # elif len(old_tweets) > 0 and len(original_tweets) == 0:
    #     for tweet_old in old_tweets:
    #         processed_old = old_tweet_analysis(old_tweets[tweet_old])
    #         store_to_processed_db(processed_old)
    
    # elif len(old_tweets) == 0 and len(original_tweets) > 0:
    #     for tweet_new in original_tweets:
    #         processed_new = new_tweet_analysis(original_tweets[tweet_new])
    #         store_to_processed_db(processed_new)
    for tweet_old, tweet_new in zip_longest(old_tweets,original_tweets):
        if tweet_old:
            processed_old = old_tweet_analysis(old_tweets[tweet_old])
            store_to_processed_db(processed_old)
        if tweet_new:
            processed_new = new_tweet_analysis(original_tweets[tweet_new])
            store_to_processed_db(processed_new)