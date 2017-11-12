#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Five"""

#import needed libraries
import random
import urllib2
import csv
import argparse
from pprint import pprint
import time
import decimal

def downloadData(url):
    """Downloads data from URL

    Args:
        url (string): string value for URL data fetch

    Returns:
        data: something to return
    """
    value = urllib2.Request(url)
    data = urllib2.urlopen(value)

    # print data.read()
    return data

def processData(fileContents):
    """Processes data passed in

    Args:
        fileContents (object): string value the data file

    Returns:
        full_database: something to return
    """

    #print fileContents.read()
    full_database = {}

    reader = csv.reader(fileContents, delimiter=',')

    for row, item in enumerate(reader):
        full_database [row] = {
            'Time_Value': item[0],
            'File': item[1],
            'Time_Spent': item[2]
        }

        print row

    #print 'Image requests account for 45.3% of all requests', img_hit_counter
    #print fileContents.read()

    return full_database

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulateOneServe():
    print 'simulate'


def main():
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'
    csvData = downloadData(url)

    databaseData = processData(csvData)
    #pprint (databaseData)


if __name__ == '__main__':
    main()