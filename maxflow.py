# Edmonds-Karp Max-Flow Algorithm for adjacency matrix representations

import copy
from collections import Set
def dataRoute(resource, server, network):
    edges = copy.deepcopy(network)
    max_flow = 0
    def find_path(paths=None,expanded_nodes=None):
        # return a path ('f/b',dest) or False
        # afterwards, update the residual network
        remaining_nodes = set(range(len(network)))
        if paths == None:
            paths = [[resource]]
            expanded_nodes = set()
        while paths:
            # pop the leftmost path
            # if the last node is server, return
            # otherwise expand the last node on the path
            # add one path to paths for each new node reachable from last node
            # add expanded node to explored nodes and remove from remaining_nodes
            path = paths.pop(0)
            last_node = path[-1]
            if last_node == server:
                return path
            elif last_node in expanded_nodes:
                continue 
            else:
                for node in remaining_nodes:
                    if edges[last_node][node] > 0:
                        next_path = path + [node]
                        paths.append(next_path)
            expanded_nodes.add(last_node)
            remaining_nodes.remove(last_node)
        return None 
    #######
    def get_path_flow(path):
        # return the flow on the path
        min_flow = float('inf')
        for node_index in range(len(path)):
            if node_index == len(path)-1:
                break
            s_node = path[node_index]
            d_node = path[node_index+1]
            f_flow = edges[s_node][d_node]
            if f_flow < min_flow:
                min_flow = f_flow
        return min_flow
            
    def update_resid_net(path,path_flow):
        
        for node_index in range(len(path)):
            if node_index == len(path)-1:
                break
            s_node = path[node_index]
            d_node = path[node_index+1]
            if edges[s_node][d_node] > 0:
                edges[s_node][d_node] -= path_flow
                edges[d_node][s_node] += path_flow
    count = 0
    while(True):
        path = find_path()
        if path == None:
            break
        else:
            path_flow = get_path_flow(path)
            max_flow += path_flow
            update_resid_net(path,path_flow)
    return max_flow