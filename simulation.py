#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Five"""

import argparse
#Import Module that Opens URL Data
import AnalyzeURL

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL for data retrieval",default=None)
parser.add_argument("--servers", type=int, help="Number of Servers", default=None)

args = parser.parse_args()

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Server:
    def __init__(self):
        self.time_remaining = 0
        self.current_task = None

    def tick(self):
        self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_time()

class Request:
    def __init__(self, time, timeSpent):
        self.timestamp = time
        self.timespent = timeSpent

    def get_stamp(self):
        return self.timestamp

    def get_time(self):
        return self.timespent

    def wait_time(self):
        return self.timespent

def simulateOneServe(requestData):
    """Similuates process with One Server

    Args:
        requestData (list): list of processes

    Returns:
        results: average wait time of server
    """

    server_queue = Queue()

    waiting_times = []

    server = Server()

    for row in requestData:
        #print requestData[row]
        time_value = int(requestData[row]['Time_Value'])
        time_spent = int(requestData[row]['Time_Spent'])

        request = Request(time_value, time_spent)

        #print 'TimeStamp: ' ,request.timestamp, 'Time Spent on Request: ',request.timespent

        server_queue.enqueue(request)

        if (not server.busy()) and (not server_queue.is_empty()):
            next_request = server_queue.dequeue()
            waiting_times.append(next_request.timespent)
            server.start_next(next_request)

        server.tick()

    #print 'wainting times',sum(waiting_times),len(waiting_times)

    results = sum(waiting_times) / len(waiting_times)
    return results

def simulateManyServers(requestData,servers):
    """Similuates process with Multiple Servers

    Args:
        requestData (list): list of processes
        servers (int): Number of servers

    Returns:
        results: average wait time of server
    """
    server_queue = Queue()
    waiting_times = []
    server = Server()

    server_list = []

    for x in range(servers):
        #print 'x: ',x
        server_list.append(Server())

    for k in server_list:
        #print 'Utilizing Server',
        for row in requestData:
            # print requestData[row]
            time_value = int(requestData[row]['Time_Value'])
            time_spent = int(requestData[row]['Time_Spent'])

            request = Request(time_value, time_spent)

            # print 'TimeStamp: ' ,request.timestamp, 'Time Spent on Request: ',request.timespent

            server_queue.enqueue(request)

            if (not server.busy()) and (not server_queue.is_empty()):
                next_request = server_queue.dequeue()
                waiting_times.append(next_request.timespent)
                server.start_next(next_request)

            server.tick()

    results = sum(waiting_times) / len(waiting_times)
    print 'Running on multiple servers: ',servers

    return results

def main():
    # Hardcode URL
    # Work on Dyanamic URL validator
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'
    databaseData = AnalyzeURL.downloadData(url)

    servers = args.servers if args.servers else raw_input("Please provide the Number of Servers to utilize: ")

    if int(servers) > 1:
        #print 'multiple'
        #Run Multiple
        response = simulateManyServers(databaseData,int(servers))

    else:
        #Run Single
        response = simulateOneServe(databaseData)

    print("Average Wait %6.2f secs."%(response))

if __name__ == '__main__':
    main()
