
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
                    uids+=[a]
                    node_numbers[a] = cur_ind
                    cur_ind+=1
            if b not in uids:
                    uids+=[b]
                    node_numbers[b] = cur_ind
                    cur_ind+=1
    graph_mat = scipy.eye(cur_ind,dtype=scipy.int8) # matrix NxN, where N is whole number of nodes of graph, if graph_mat[i,j] equals to 1, it means that there is link from i-th node to j-th 
    for (a,b) in graph_tuple:
            graph_mat[node_numbers[a],node_numbers[b]] = 1
    return (graph_mat,scipy.array(uids))

def tuple_list_from_matrix(graph_mat,uids):
    """ takes graph as graph_mat matrix and uids list as arguments
    returns graph_tuple, which is representation of the graph as list of tuple. This is inverse function for matrix_from_tuple_list, in sense that
    matrix_from_tuple_list(tuple_list_from_matrix(graph)) ~ graph, and
    tuple_list_from_matrix(matrix_from_tuple_list(graph)) ~ graph (not strictly equal because elements maybe rearranged"""
    tuple_list = []
    for i in xrange(graph_mat.shape[0]):
            indexes = scipy.nonzero(graph_mat[i,:])[0] #list of nodes connected with i-th
            tuple_list+=[(uids[i],j) for j in uids[indexes]]
    return tuple_list

def subgraph_with_center(graph_mat, uids, center_num):
    """takes number of center node, and returns new subgraph, that consists of all nodes connected with center.
        
        arguments:
        graph_mat,uids - graph description as matrix (see matrix_from_tuple_list doc for details)
        center_num - number of center node

        output:
        subgraph,sub_uids - subgraph description as matrix (see matrix_from_tuple_list doc for details)"""
    center_friends_num = scipy.nonzero(graph_mat[center_num,:] == 1)[0] #indexes of friends of central node including itself
    subgraph = graph_mat[center_friends_num,:][:,center_friends_num] # FIXME we consider part of graph which consists of friends of center only 
    sub_uids = uids[center_friends_num]
    return (subgraph,sub_uids)

def graph_connected_components(graph_mat):
    """takes graph as matrix and return list of connected components
          
       arguments:
       graph_mat - matrix of graph
              
       output:
       list_of_comp - list of components, list_of_comp[i] - list of node numbers in (i-1)-th component"""
    component_of_graph = scipy.zeros(graph_mat.shape[0],dtype = scipy.int8) # component_of_graph[i] is the number of component of i-th node.
    cur_comp = 1 #the number of current component (see below)
    try:
        tmp_nodes_to_process = [scipy.nonzero(component_of_graph==0)[0][0]] #node indexes to process
    except IndexError:
            #exceptional situation, when graph_mat is empty
            return []

    #kind of breadth first search
    while(len(tmp_nodes_to_process)>0): #while there is nodes to process
        cur_node = tmp_nodes_to_process.pop() #take one from array
        lnodes_numbers = scipy.nonzero(graph_mat[cur_node,:])[0] #take indexes of all of it linked nodes
        #and choose that corresponds to the non processed nodes of them, the node is non processed if its component is zero
        lnodes_numbers = scipy.extract(component_of_graph[lnodes_numbers] == 0,lnodes_numbers)
        tmp_nodes_to_process +=lnodes_numbers.tolist()
        component_of_graph[lnodes_numbers] = cur_comp
        # if there is no linked nodes, start processing of new connected component, and next unprocessed node
        if (len(tmp_nodes_to_process) == 0):
            cur_comp+=1
            tmp_arr = scipy.nonzero(component_of_graph==0)[0]
            if (len(tmp_arr)>0):tmp_nodes_to_process = [tmp_arr[0]] 

    list_of_comp = [] #collect list
    for i in range(cur_comp+1):
        tmp_arr=scipy.nonzero(component_of_graph==(i+1))[0].tolist()
        if (len(tmp_arr)>0):list_of_comp+=[tmp_arr]
    return list_of_comp

