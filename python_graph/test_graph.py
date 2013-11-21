
from graph_func import *
import scipy
#test of matrix_from_tuple_list
#matrix form of [(1,2),(2,3),(3,1),(4,5),(5,1)] is
# [[1,1,0,0,0],
#  [0,1,1,0,0],
#  [1,0,1,0,0],
#  [0,0,0,1,1],
#  [0,0,0,1,1]]
print ("test1 of matrix_from_tuple_list")
triangle_and_bar,t_uids=  (matrix_from_tuple_list([(1,2),(2,3),(3,1),(4,5),(5,4)]))
print (triangle_and_bar)
#test2 of matrix_from_tuple_list
#matrix form of [(1,1),(2,2),(3,3)] is
# [[1,0,0],
#  [0,1,0],
#  [0,0,1]]
print ("test2 of matrix_from_tuple_list")
dots, d_uids = matrix_from_tuple_list([(1,1),(2,2),(3,3)])
print (dots)
#test 1 of tuple_list_from_matrix
#tuple list form of 
# triangle_and_bar is [(1,2),(2,3),(3,1),(4,5),(5,1)]
t_and_b_tuples = tuple_list_from_matrix(triangle_and_bar,t_uids)
print (t_and_b_tuples)
#test1 of graph_connected_components connected components of [[1,1],
#                                                             [1,1]] is [[0,1]]
print ("test1 of graph_connected_components")
test1_mat = scipy.array([[1,1],
             [1,1]])
print(graph_connected_components(test1_mat))
#test2 of graph_connected_components
#connected components nodes of triangle_and_bar is
#[[1,2,3],[4,5]]
print ("test2 of graph_connected_components")
con_comps= graph_connected_components(triangle_and_bar)
print(con_comps)
#corresponding subgraphs:
#[[1,1,0],
# [0,1,1],
# [1,0,0]],
#[[1,1],
#[1,1]]
for nodes in con_comps:
    cc = (triangle_and_bar[nodes,:][:,nodes],t_uids[nodes]) # FIXME connected component subgraph in matrix form
    print (cc)
    print (tuple_list_from_matrix(cc[0],cc[1]))
#test of subgraph_with_center
#subgraph of [(1,2),(2,1),(2,3),(3,2),(3,1),(1,3),(4,5),(5,4)] with center in node 1 is
#[(1,2),(2,1),(1,3),(3,1),(2,3),(3,2)]
# with center in node 4 [(4,5),(5,4)]
print ("subgraph_with_center test")
tb = [(1,2),(2,1),(2,3),(3,2),(3,1),(1,3),(4,5),(5,4)] # bidirected triangle and bar
tbm,tb_nod= matrix_from_tuple_list(tb)
print (tbm)
print tuple_list_from_matrix(*subgraph_with_center(tbm,tb_nod,1))
print tuple_list_from_matrix(*subgraph_with_center(tbm,tb_nod,4))

