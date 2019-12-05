#!/usr/bin/python
import re
import glob

if __name__ == "__main__":

    # store all the file names ending in .md, found recursively
    filenames = glob.glob("**/*.md", recursive=True)

    # for each file, store the lines and set the line number to 1
    for filename in filenames:
        file = open(filename)
        lines = file.readlines()
        file.close
        line_num = 1

        # for each line of each file, look for the old docs format. print a message if one is found, and increment the line number variable
        for line in lines:
            if re.search("\]\(/docs/",line):
                print(filename + " --> Line " + str(line_num) + ": DEPRECATED LINK FORMAT" + "\n" + line)
            
            line_num += 1
