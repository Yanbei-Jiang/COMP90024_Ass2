import sys
sys.path.append("..\..\crawler")
from db_load_data import *
from main import *

initialize_couchdb()
old_tweets = get_spec_db("old_tweets")
original_tweets = get_spec_db("original_tweets")

for tweet in old_tweets:
    processed = old_tweet_analysis(tweet)
    
    store_to_processed_db(processed)

for tweet in original_tweets:
    processed = new_tweet_analysis(tweet)

    store_to_processed_db(processed)

