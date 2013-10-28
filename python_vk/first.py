#!/usr/bin/env python
import urllib
import urllib2
import codecs
import json
calls = [0]
stat_friend = {'n':0,'avg':0,'d2':0} # statistics

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

#my_uid = 568716 #my vk uid
my_uid = 15362492 #FIXME
graph = []
me = get_user(my_uid)
processed_friends = {my_uid:{'first_name':me['first_name'],'last_name':me['last_name']}}
process_uid(my_uid,processed_friends,graph,2)
print (calls[0])
with codecs.open('friends.txt','w', encoding='utf-8') as ff:
    for uid in processed_friends.keys():
        tmp  = 0.0
        ff.write(u'{0} - {1} {2}\n'.format(uid,processed_friends[uid]['first_name'], processed_friends[uid]['last_name']))
ind = 0
with open('friends.json','w') as jf:
        json.dump(processed_friends,jf)
with open('graph.json','w') as fg:
        json.dump(graph,fg)
