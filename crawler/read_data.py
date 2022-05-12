import mmap

def read_data_file(twitter_file):
    # read the file
    with open(twitter_file, "r") as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        
        # position head to the assigned task's first line
        mm.seek(twitter_file_offset[assignment_first_line - 1]) # 'minus 1' because 'the first line's subscript in the list is the 0'
        
        # record the line be searched currently
        curr_line = assignment_first_line
        # filter the twitter data to match grid
        for line in iter(mm.readline, b""):
            
            # get the information from the current line
            line_info = info_capturer.get_grid_language_info(line)

            if (line_info != False):
                comm.send(line_info, dest = 0, tag = 2)

            # count how many assignments have been finished
            curr_line += 1

            # break the loop if all the required assignment has been completed
            if (curr_line == assignment_last_line + 1):
                break

        mm.close()
    f.close()