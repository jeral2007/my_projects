#!/usr/bin/env python
import urllib
import urllib2
import codecs
import json
import argparse
parser  = argparse.ArgumentParser()
parser.add_argument('uid',type = int, help = "id of user for which graph is to be constructed")
parser.add_argument('friends_json',type = str,help = "friends filename, in this filename info of friends of the user will be saved in json format")
parser.add_argument('graph_json',type = str, help = "the graph filename, here graph will be saved in json format")
args = parser.parse_args()
def get_friends(uid):
        """takes user id and returns list of friends ids, if uid corresponding to the banned user, empty list is returned
        Example:
        get_friends(1) - list of Pavel Durov friends ids"""
        url = "http://api.vk.com/method/friends.get?user_id={:d}&fields=uid,first_name,last_name&".format(uid) #FIXME
        response = urllib2.urlopen(url)
        json_str = response.read(response)
        try:
            return json.loads(json_str)['response']
        except KeyError:
                return []

def get_user(uid):
        """ takes user id and returns his/her name"""
        url = "http://api.vk.com/method/users.get?user_ids={:d}&".format(uid) #FIXME
        response = urllib2.urlopen(url)
        json_str = response.read(response)
        try:
            return json.loads(json_str)['response'][0]
        except KeyError:
                return []
def process_uid(uid,processed_uids,graph,maxdepth):
        """ takes all friends of uid, adds to the graph, and process them recursively with given maximal depth maxdepth. uid modified when function is called, 
        graph of friends stored as list of connected ordered pairs, so if a is friend of b, then (b,a) is in graph"""
        friends_of_uid = get_friends(uid)
        #statistics
        tmp   = len(friends_of_uid)
        processed_uids[uid]['depth'] = maxdepth
        for friend in friends_of_uid:
                graph+=[(uid,friend['uid'])]
                if friend['uid'] not in processed_uids.keys():
                        processed_uids[friend['uid']]={field:friend[field] for field in ['first_name','last_name']}
                        processed_uids[uid]['friend_num'] = len(friends_of_uid)
                        processed_uids[friend['uid']]['depth'] = -2
                if (maxdepth>1 and processed_uids[friend['uid']]['depth']<maxdepth-1):
                        process_uid(friend['uid'],processed_uids,graph,maxdepth-1)

my_uid = args.uid
graph = []
me = get_user(my_uid)
processed_friends = {my_uid:{'first_name':me['first_name'],'last_name':me['last_name']}}
process_uid(my_uid,processed_friends,graph,2)
ind = 0
with open(args.friends_json,'w') as jf:
        json.dump(processed_friends,jf)
with open(args.graph_json,'w') as fg:
        json.dump(graph,fg)
