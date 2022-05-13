import mmap
import json
import db_load_data as db

def read_data_file(twitter_file):
    # read the file
    with open(twitter_file, "r") as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        # filter the twitter data to match grid
        for line in iter(mm.readline, b""):

            # get the information from the current line
            line_json = get_row_language_info(line)

            # store the json format line into old data backup database
            if (line_json != False):
                db.store_to_old_data_backup_db(line_json)

        mm.close()
    f.close()


def get_row_language_info(line):
        '''
        Capture grid id and language from twitter file's line

        :param line: row from twitter file
        :return boolean / the line in json format
        '''

        # convert current line from byte to string format
        line = line.decode('utf8')
        # remove useless element and convert current line to json format
        line = line.replace('"location":"melbourne"}},', '"location":"melbourne"}}')
        line = line.replace('"location":"melbourne"}}]}', '"location":"melbourne"}}')

        # convert current line from string to json format 
        try:
            line = json.loads(line) 
        except:
            #print(line)
            return False
        
        return line