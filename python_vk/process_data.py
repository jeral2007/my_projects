#!/usr/bin/env python
import json
import math
import codecs
import scipy
from graph_func import *
import argparse
def graphviz_string(graph_tup,graph_name,process_uid):
    result  = u"subgraph cluster_{0} {{\n".format(graph_name)
    if (len(graph_tup) ==1):
            result+="style = filled\n fillcolor = gray \n"
            
    for (a,b) in graph_tup:
        if (a!=b):
           result+=u"{0} -- {1};\n".format(process_uid(a),process_uid(b))
        else:
           result+=process_uid(a)+";\n"
    return result+"}\n"

parser  = argparse.ArgumentParser()
parser.add_argument('uid',type = int, help = "id of user for which graph is to be constructed")
parser.add_argument('friends_json',type = str,help = "friends filename, in this filename info of friends of the user is saved in json format")
parser.add_argument('graph_json',type = str, help = "the graph filename, here graph is  saved in json format")
parser.add_argument('graph_dot',type = str, help = "the graph will be saved in the dot format in this file")
args = parser.parse_args()
with open(args.graph_json,'r') as jg:
        graph_tup = json.load(jg)
with open(args.friends_json,'r') as jf:
        pfr = json.load(jf)
center_id = args.uid #central node FIXME
graph_mat,uids = matrix_from_tuple_list(graph_tup)
center_num = scipy.nonzero(uids==center_id)[0][0]
subgraph,sub_uids = subgraph_with_center(graph_mat,uids,center_id)
print (subgraph.shape,graph_mat.shape)
#remove center from subgraph
cnum = scipy.nonzero(uids==center_id)[0][0]
print (cnum)
subgraph = scipy.delete(scipy.delete(subgraph,cnum,0),cnum,1)
sub_uids = scipy.delete(sub_uids,cnum,0)
#make graph biderected (if there is link from a to b, then link from b to a also present)
subgraph = subgraph + scipy.transpose(subgraph)
con_comps = graph_connected_components(subgraph)

i=0
header = "graph sd {\n fontsize=8 \n" #dotfile header FIXME
with codecs.open(args.graph_dot,'w',encoding='utf-8') as fd:
    fd.write(header)
    for nodes in con_comps:
        i+=1
        cc = (subgraph[nodes,:][:,nodes],sub_uids[nodes]) # FIXME connected component subgraph in matrix form
        tmp_g = [ edge for edge in tuple_list_from_matrix(cc[0],cc[1]) if (edge[0]<=edge[1])]
        fd.write(graphviz_string(tmp_g,'g'+str(i),lambda uid:'"'+pfr[str(uid)]['first_name']+u' '+pfr[str(uid)]['last_name']+' '+ str(uid)+'"' ))
    fd.write("}\n")

