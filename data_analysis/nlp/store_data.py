"""
Author: Wei Ge - 1074198
        Han Wang - 1041260 
        YanBei Jiang - 1087029
        Yiwen Zhang - 1002781
        Zening Zhang - 1078374
"""
# import sys
# sys.path.append("../crawler")
from db_load_data import *
from nlp.analysis import *
from itertools import zip_longest
import schedule

def nlp_main():

    initialize_couchdb()
    old_tweets = get_spec_db("old_tweets")
    original_tweets = get_spec_db("original_tweets")
    count = 0
    for tweet_old, tweet_new in zip_longest(old_tweets,original_tweets):
        if tweet_old:            
            count += 1            
            if count >= 66170:
                processed_old = old_tweet_analysis(old_tweets[tweet_old])
                store_to_processed_db(processed_old)

        if tweet_new:             
            count += 1
            if count >= 66170:
                processed_new = new_tweet_analysis(original_tweets[tweet_new])
                store_to_processed_db(processed_new)

    
