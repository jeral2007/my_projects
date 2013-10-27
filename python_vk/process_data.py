#!/usr/bin/env python
import json
import math
import codecs
import scipy
def matrix_from_tuple_list(graph_tuple):
        """ takes graph as tuple as argument,
            returns graph as matrix graph_mat and arrays of uids uids:
            graph_mat,uids = matrix_from_tuple_list(graph_tuple).
            
            arguments:
            graph_tuple - graph description as lists of tuples, if a and b are nodes of graph and tuple (a,b) is in graph_tuple then 
            there is link from node a to node b. 
            
            output:
            graph_mat - matrix NxN, where N is whole number of nodes of graph, if graph_mat[i,j] equals to 1, it means that there is link from i-th node
            to j-th (see below).
            uids - array of node names, uids[i] - the name of i-th node in graph_mat as it represented in graph_tuple."""

            uids = [] #array of node names
            node_numbers = {} #node numbers hash, if uids[i] = a then node_numbers[a] = i
            cur_ind = 0 #temporary variable, which holds current index in uids
            for (a,b) in graph_tuple:
                    if a not in uids:
                            uids[cur_ind] = a
                            node_numbers[a] = cur_ind
                            cur_ind+=1
                    if b not in uids:
                            uids[cur_ind] = b
                            node_numbers[b] = cur_ind
                            cur_ind+=1
            graph_mat = scipy.eye((cur_ind,cur_ind),dtype=scipy.int8) # matrix NxN, where N is whole number of nodes of graph, if graph_mat[i,j] equals to 1, it means that there is link from i-th node to j-th 
            for (a,b) in graph_tuple:
                    graph_mat(node_numbers[a],node_numbers[b]) = 1
            return (graph_mat,scipy.array(uids))

with open('graph.json','r') as jg:
        graph_tup = json.load(jg)
center_id = 15362492 #FIXME
graph_mat,uids = matrix_from_tuple_list(graph_tup)
center_num = scipy.nonzero(uids==center_id)[0][0]
print "uids[{0}]={1}?={2}".format(center_num,uids[center_num],center_id)

