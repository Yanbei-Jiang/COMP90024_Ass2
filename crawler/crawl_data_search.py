import threading
import configparser
import io
import json
import datetime
import datetime as dt
import schedule
import tweepy_search_crawler
import db_load_data
import time
from pytz import utc


def set_configuration():
    '''
    Set the configuration for crawlers
    '''
    # get the key words for each crawler to search
    keywords_file = 'search_keywords.json'
    # read the json with key words
    keywords = []
    with io.open(keywords_file,'r') as f:
        keywords = json.load(f)

    # get the configuration of crawler
    config_file = 'crawler_config.ini'
    # read the configuration
    try:
        # read the configuration file
        config = configparser.ConfigParser()
        config.read(config_file)
        # curr_key_words records each crawler's key words from keywords list
        curr_key_words = 0
    
        # initilize each crawler followed by assigning key searching word to it
        for i in config.sections():
            # set the configuration
            api_key = config[i]['api_key']
            api_key_secret = config[i]['api_key_secret']

            access_token = config[i]['access_token']
            access_token_secret = config[i]['access_token_secret']
            datetime_until  = (datetime.datetime.now().astimezone(utc) - datetime.timedelta(days = 6)).strftime("%Y-%m-%d")
            globals()['listener_'+i] = tweepy_search_crawler.StreamListener(
                                                                            api_key, api_key_secret, access_token, access_token_secret, 
                                                                            (keywords[list(keywords.keys())[curr_key_words]]),
                                                                            (list(keywords.keys())[curr_key_words]),
                                                                            datetime_until,
                                                                            "Thread_"+str(curr_key_words))
            # move to the next key words should be searched
            curr_key_words+=1
        print("Initialize the Crawlers Successfully.\n")

    except KeyError:
        print('\nMissing the key of Api or Access, please check the file')
        exit(1)





def start_crawlers():
    '''
    Start the crawlers to manipulate the data
    '''
    # initialize the crawlers
    print("Initialize the Crawlers")
    set_configuration()

    # start the crawlers
    print("Start Crawlers")
    listener_account_1.start()
    listener_account_2.start()
    listener_account_3.start()
    print("Start Three Crawlers Successfully\n")
    
    # assign the work to re-start all thread each 15 minutes
    #schedule.every(15).minutes.do(restart_crawlers)

    # while (True):
    #     schedule.run_pending()
        

def initialize_db():
    '''
    Provide the API to initialize the couch db
    '''
    db_load_data.initialize_couchdb()


# initialize the db
initialize_db()

# start the crawlers
start_crawlers()
schedule.every().day.at("00:01").do(start_crawlers)
# empty the db
#db_load_data.empty_spec_db('original_tweets')
#db_load_data.empty_spec_db('processed_tweets')
