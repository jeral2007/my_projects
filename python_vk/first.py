#!/usr/bin/env python
import urllib
import urllib2
import codecs
calls = [0]
def get_friends(uid):
        """takes user id and returns list of friends ids
        Example:
        get_friends(1) - list of Pavel Durov friends ids"""
        import json
        url = "http://api.vk.com/method/friends.get?user_id={:d}&fields=uid,first_name,last_name&".format(uid) #FIXME
        response = urllib2.urlopen(url)
        json_str = response.read(response)
        print "get_friends called"
        return json.loads(json_str)['response']
def process_uid(uid,processed_uids,graph):
        """ takes all friends of uid, adds to the graph, and process them recursively. uid modified when function is called, 
        graph of friends stored as list of connected ordered pairs, so if a is friend of b, then (b,a) is in graph"""
        friends_of_uid = get_friends(uid)
        for friend in friends_of_uid:
                graph+=[(uid,friend['uid'])]
                if friend['uid'] not in processed_uids.keys():
                        processed_uids[friend['uid']]={field:friend[field] for field in ['first_name','last_name']}
                        process_uid(friend['uid'],processed_uids,graph)

my_uid = 568716 #my vk uid
graph = []
processed_friends = {my_uid:{'first_name':'Me','last_name':''}}
process_uid(my_uid,processed_friends,graph)
print (calls[0])
print (graph)
with codecs.open('friends.txt','w', encoding='utf-8') as ff:
    for uid in processed_friends.keys():
        ff.write(u'{0} - {1} {2}\n'.format(uid,processed_friends[uid]['first_name'], processed_friends[uid]['last_name']))

