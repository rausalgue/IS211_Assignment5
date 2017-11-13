#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Analyze URL and Return data Object
Update CSV data according to Data coming in
"""

import urllib2
import csv

def downloadData(url):
    """Downloads data from URL

    Args:
        url (string): string value for URL data fetch

    Returns:
        data: something to return
    """

    value = urllib2.Request(url)
    data = urllib2.urlopen(value)

    #print data.read()

    full_database = {}

    reader = csv.reader(data, delimiter=',')

    for row, item in enumerate(reader):
        full_database [row] = {
            'Time_Value': item[0],
            'Time_Spent': item[2],
            'File': item[1]
        }

        #print row

    #print 'Image requests account for 45.3% of all requests', img_hit_counter
    #print data.read()

    return full_database
