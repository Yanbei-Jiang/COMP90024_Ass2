import io
import time
import json
from time import gmtime, strftime
import tweepy
import threading
import configparser
import os.path

class StreamListener(threading.Thread, tweepy.Stream):

    count = 1
    # count_for_sleep = 0
    data_since = strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    result_dict ={data_since:[]}
    file_name = data_since[:10]+'.json'
    start_time = time.perf_counter()


    # initialize
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret, keywords, thread_name):
        # extend from father
        threading.Thread.__init__(self)
        tweepy.Stream.__init__(self, api_key, api_key_secret, access_token, access_token_secret)
        # self attributes
        self.keywords = keywords
        self.thread_name = thread_name
    

    # Override Tweepy.Stream
    def on_data(self, data):
        # # count the sleep time
        # dur_for_sleep = time.perf_counter()-self.start_time
        # self.count_for_sleep += 1

        # 
        try:
            data_dict = json.loads(data)
            place = data_dict['place']
            json_data = {data_dict['id']:data_dict}
            if  place != None:

                # generate or open the file to store data
                if os.path.isfile(self.file_name):
                    with io.open(self.file_name, 'r') as f:
                        content = json.load(f) 
                    content.update(json_data)
                    with io.open(self.file_name,'w') as f:
                        json.dump(content,f,indent = 2)
                else:
                    with io.open(self.file_name,'w') as f:
                        json.dump(json_data,f,indent = 2)
                
                # show the processing
                i = self.count%10
                a = '*'* i
                b = '.'*(10-i)
                c = (i/10)*100
                dur = time.perf_counter()-self.start_time
                print(self.thread_name + '： {:^3.0f}%[{}->{}]{:.2f}s\n'.format(c,a,b,dur),end='')
                if self.count %10 == 0:
                    print('\nHave crawled %d twitter' %self.count)
                    
                # print(self.count)
                self.count+=1

                # if self.count == 10:
                # self.disconnect()

        # ignore the tweets without 'place' attribute
        except KeyError as e:
            # print("\n")
            # print("This tweet does not have the 'place' attibutes thus be ignored")
            # print(data)
            # print("\n")
            return True

        except BaseException as e:
            print("Exception made. Data printed below")
            print(data)
            print(e)

        return True


    # Override Stream
    def on_error(self, status_code):
        print(status_code)

        if status_code == 420:
            print('Too many requests! Please wait')
            self.disconnect()
            time.sleep(20)
        if status_code == 429:
            print("Too many requests! Please wait")
            self.disconnect()
            time.sleep(15*60 + 1)
        else:
            print("unexpected error. See error code above. Retry in 10s")
            time.sleep(10)


    # Override Thread
    def run(self):
        # get the searching key words
        language_val = self.keywords['languages']
        track_val = self.keywords['track']
        locations_val = self.keywords['locations']

        # start filter
        self.filter(languages=language_val, track=track_val, locations=locations_val)


    """
    def on_status(self, status):
        if status.retweeted:
            return
    """




