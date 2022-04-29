import configparser
from multiprocessing.spawn import old_main_modules
import os
import couchdb
import json

# global variables
db_info_ini_file = "db_info.ini"

username = ""
password = ""
host = ""
port = ""
odl_db_name = ""
new_db_name = ""
couch = ""


def connect_couchdb(username, password, host, port):
    '''
    Connect to couchdb
    '''
    couch = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return couch


def get_spec_db(db_name, couch):
    '''
    Get the specific database
    '''
    # get existed db
    try:
        return couch[db_name]
    # otherwise, create the db
    except:
        return couch.create(db_name)


def get_db_into():
    '''
    Get the database configuration
    @return the dictionary with user and db's information
    '''
    global db_info_ini_file
    # read the configuration file
    curpath = os.path.dirname(os.path.realpath(__file__))
    cfgpath = os.path.join(curpath, db_info_ini_file)
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


def initialize_couchdb():
    '''
    Initialize the couchdb
    '''
    print("--------------Initialize the database--------------")
    global username
    global password
    global host
    global port
    global odl_db_name
    global new_db_name
    global couch

    # set up info
    db_info = get_db_into()
    username = db_info['username']
    password = db_info['password']
    host = db_info['host']
    port = db_info['port']
    odl_db_name = db_info['odl_db_name']
    new_db_name = db_info['new_db_name']

    # connect the database
    couch = connect_couchdb(username, password, host, port)
    print("Initialize the database Successfully")


def store_to_backup_db(data):
    '''
    Accept data and store into backup database
    @param data be stored
    '''
    global odl_db_name
    global couch
    get_spec_db(odl_db_name, couch).save(data)


def store_to_processed_db(data):
    '''
    Accept data and store into processed databse
    @param data be stored
    '''
    global new_db_name
    global couch
    get_spec_db(new_db_name, couch).save(data)
    

def get_data_from_db(db_name):
    '''
    Get data from couchdb
    @param db_name
    '''
    # get all rows from 
    for id in db_name:
        print(db_name[id])


def empty_spec_db(couch, db_name):
    '''
    Delete all data in the specific database
    @param db: the couchdb
    @param db_name: the specific database be deleted
    '''
    couch.delete(db_name)