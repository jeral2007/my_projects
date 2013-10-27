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
triangle_and_bar,t_uids=  (matrix_from_tuple_list([(1,2),(2,3),(3,1),(4,5),(5,1)]))
print (triangle_and_bar)
#test2 of matrix_from_tuple_list
#matrix form of [(1,1),(2,2),(3,3)] is
# [[1,0,0],
#  [0,1,0],
#  [0,0,1]]
print ("test2 of matrix_from_tuple_list")
dots, d_uids = matrix_from_tuple_list([(1,1),(2,2),(3,3)])
print (dots)
#test1 linked components of [[1,1],
#                            [1,1]] is [[0,1]]
print ("test1 of graph_connected_components")
test1_mat = scipy.array([[1,1],
             [1,1]])
print(graph_connected_components(test1_mat))
print ("test2 of graph_connected_components")
#test2
#connected components of triangle_and_bar is
#[[1,2,3],[4,5]]
print (graph_connected_components(triangle_and_bar),t_uids)
