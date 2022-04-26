import configparser
import os


def get_db_into():
    '''
    Get the database configuration
    @return the dictionary with user and db's information
    '''
    # read the configuration file
    curpath = os.path.dirname(os.path.realpath(__file__))
    cfgpath = os.path.join(curpath, "db_info.ini")
    conf = configparser.ConfigParser()
    conf.read(cfgpath, encoding="utf-8")

    # get the items
    db_user_info = conf.items('user_info')
    db_info = conf.items('db_info')

    # convert tuples to dict
    dict = {}
    for curr_tuple in db_user_info:
        dict[curr_tuple[0]] = curr_tuple[1]
    for curr_tuple in db_info:
        dict[curr_tuple[0]] = curr_tuple[1]
    
    return dict


# get the user info and db info
db_info = get_db_into()
username = db_info['username']
password = db_info['password']
host = db_info['host']
port = db_info['port']
db_name = db_info['db_name']