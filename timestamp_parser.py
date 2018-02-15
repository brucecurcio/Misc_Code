#!/usr/bin/env python
'''
This Python script is used to calculate the difference between timestamps

feed into this script a file that only has a list of timestamp.

'''
   
import sys
import os
import time
import datetime

def extract_values(line):
     date = line[0][:19]
     t = time.strptime(date, "%Y-%m-%dT%H:%M:%S")
     d = datetime.datetime(*t[:6])
     return (date, d)
    
def main():
    log_file = sys.argv[1]

    in_file = open(log_file, 'r')
    parser = in_file.readlines()
    in_file.close()

    print ' TimeStamp            Delta'
    for i in range(0, len(parser)):
        if i < (len(parser) - 1):
            (date1, d1) = extract_values(parser[i].rstrip().split(' '))
            (date2, d2) = extract_values(parser[i+1].rstrip().split(' '))

            time_delta = d2 - d1
           if time_delta.seconds > 0:
                qps = (hits + miss) / time_delta.seconds
                hits_per = float((float(hits) / float(total_queries)) * 100.00)
                miss_per = float((float(miss) / float(total_queries)) * 100.00)
                print '%s %5min' \
                  %(date2, time_delta)

if __name__ == "__main__":
    main()

