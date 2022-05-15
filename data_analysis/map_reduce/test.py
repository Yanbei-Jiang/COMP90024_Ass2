import sys
sys.path.append("..\..\crawler")
from db_load_data import *
import json 
initialize_couchdb()
wow = get_spec_db('original_tweets')
for i in wow:
    print(wow[i].keys())
    break
# store_to_old_data_backup_db(json.dumps(tweet_obj))


