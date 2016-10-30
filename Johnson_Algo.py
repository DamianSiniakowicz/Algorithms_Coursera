#!/usr/env/bin python

# line 1 : num vert ... num edge
# rest : tail vert ... head vert ... edge length ... each entry is an edge

# may have negative cycles

# return shortest shortest path or NULL

######################################################################

import itertools

# the heap deletion and update  entry code is from https://docs.python.org/2/library/heapq.html

pq = []                         # list of entries arranged in a heap
#entry_finder = {}               # mapping of tasks to entries
#REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    count = next(counter)
    entry = [priority, count, task]
    #entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task[1] not in explored_nodes:
            return task[0], task[1], priority
    raise KeyError('pop from an empty priority queue')


# how to map tasks to entries? task = dest_node : entry = (min_dist, count, dest_node)



import numpy
from collections import defaultdict
from heapq import * 


def pset_4(path):
	'''
	path : str
		the full path to your data

	return : None or int
		None if there exits a negative cycle, int for the shortest shortest path
	'''

	
	def add_task(task, priority=0):
	    'Add a new task or update the priority of an existing task'
	    count = next(counter)
	    entry = [priority, count, task]
	    #entry_finder[task] = entry
	    heappush(pq, entry)

	def remove_task(task):
	    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
	    entry = entry_finder.pop(task)
	    entry[-1] = REMOVED

	def pop_task():
	    'Remove and return the lowest priority task. Raise KeyError if empty.'
	    while pq:
		priority, count, task = heappop(pq)
		if task[1] not in explored_nodes:
		    return task[0], task[1], priority
	    raise KeyError('pop from an empty priority queue')



	data_1 = numpy.genfromtxt(path, skip_header = 1)
	the_file = open(path, 'r')
	header = the_file.readline()
	header = header.split(' ') 
	clean_header = [''.join(char for char in string if char.isalnum()) for string in header]
	num_vertices = int(clean_header[0])
	num_edges = int(clean_header[1])

	# how would you solve this if negative cycles weren't a problem? n Bellman Fords or 1 Johnson

	# add imaginary vertex : just set all shortest paths of length 1 to be the min of actual edges leading to sink and 0.



	### find shortest paths from imaginary vertex to each node. (Bellman Ford. )

	# need quick access to edge length, given (source,sink) key. ... hashtable (source,sink):length
	# need quick access to sources of a sink. ... hashtable sink:[source1,source2,...], use default dict

	SS_length = {}
	sink_sources = defaultdict(list)
	x_to_y_length = defaultdict(list)

	for edge_index in range(num_edges):
		sink = data_1[edge_index,1]
		source = data_1[edge_index,0]
		length = data_1[edge_index,2]
		SS_length[(source,sink)] = length
		sink_sources[sink].append(source)
		x_to_y_length[source].append((sink,length))

	budget_dest_to_path_length = {}
	print "starting bellman"
	for edge_budget in range(1,num_vertices+2):
		print "edge_budget",edge_budget
		for sink in range(1,num_vertices+1):		
			if edge_budget == 1:
				budget_dest_to_path_length[(1,sink)] = 0
			else:
				case_1 = budget_dest_to_path_length[(edge_budget - 1, sink)]
				case_2 = [(budget_dest_to_path_length[(edge_budget-1,source)] + SS_length.get((source,sink),float("inf"))) for source in sink_sources[sink]]				
				case_2.append(case_1)
				budget_dest_to_path_length[(edge_budget,sink)] = min(case_2)
	print "finished bellman"		
	for sink in range(1,num_vertices+1):
		if budget_dest_to_path_length[(num_vertices,sink)] > budget_dest_to_path_length[(num_vertices+1,sink)]:
			print "we found a negative cyce"
			return None

	# we know length of shortest modified path to each vertex, need to assign each vertex a weight equal to the shortest modified path toit			
	# really though, need to take each edge in SS_length[(x,y)] = SS_length[(x,y)] + budget_dest_to_path_length[(num_vertices-1,x)] - ""[(nv,y)]

	for SS in SS_length.keys():
		SS_length[SS] = SS_length[SS] + budget_dest_to_path_length[(num_vertices,SS[0])] - budget_dest_to_path_length[(num_vertices,SS[1])]

	# we have our non-negative edge lengths

	complete_SS_length = {}

	############
	for vertex_index in range(1,num_vertices+1): # run djikstra n times
		complete_SS_length[(vertex_index,vertex_index)] = 0
		explored_nodes = [vertex_index]
		unexplored_nodes = range(1,num_vertices+1)
		unexplored_nodes.remove(vertex_index)
		# need to make a heap 
		pq = []                         # list of entries arranged in a heap
		entry_finder = {}               # mapping of tasks to entries
		REMOVED = '<removed-task>'      # placeholder for a removed task
		counter = itertools.count()     # unique sequence count
		
		
		for unexplored_node in unexplored_nodes:
			if vertex_index in sink_sources[unexplored_node]:
				add_task((vertex_index,unexplored_node),SS_length[(vertex_index,unexplored_node)])
			else:
				add_task((vertex_index,unexplored_node),float('inf'))
		
		for x in range(num_vertices - 1): # add all n-1 shortest paths from vert
			print "djikstra",vertex_index,"round",x
			# need a heap containing all edges emanating from the explored nodes. like this (length, (source,sink))
			# need to be adding the minimum djikstra greedy score path crossing the cut, not just the last edge of that path
			'''
			for each round of dijkstra
				put unexplored nodes in a heap
				the key of each node is the length of the edge from the source to the node, or infinity
				for 1 to n-1	
					extract the minimum node from the heap and add it to the explored nodes
					for outgoing edge of the extracted node
						if the edge ends in a unexplored node
							if source_to_extracted + extracted_to_unexplored < source_to_unexplored:
								reset the key of unexplored

			after done with all djikstras, still need to unmodify edges
			'''
			previous_node, dest_node, path_distance = pop_task()
			explored_nodes.append(dest_node)
			unexplored_nodes.remove(dest_node)
			for next_node, dist in x_to_y_length[dest_node]: # should we be using x_to_y_length ??
				if next_node in unexplored_nodes:
					dist = SS_length[(dest_node,next_node)]
					add_task((dest_node,next_node),path_distance+dist)  			
			

			# heapq evaluates priority like this [first look at this, second look at this, etc.]
			# [distance, counter, end_node]



			complete_SS_length[(vertex_index,dest_node)] = path_distance
			


	# we have all modified shortest paths. now unmodify them and return the value of the smallest one.

	shortest_shortest = None

	for SS in complete_SS_length.keys():
		tail_weight = budget_dest_to_path_length[(num_vertices,SS[0])]
		head_weight = budget_dest_to_path_length[(num_vertices,SS[1])]
		unmodified = complete_SS_length[SS] - tail_weight + head_weight
		if shortest_shortest is None or unmodified < shortest_shortest:
			shortest_shortest = unmodified

	print "length of shortest shortest path:", shortest_shortest
	return


	# transform all dijkstra paths

'''
test = "/home/damian/Dropbox/Algorithms/johnson_test_5.txt"
#test2 = "/home/damian/Dropbox/Algorithms/johnson_test_4.txt"

if __name__ == "__main__":
	pset_4(test)
	#pset_4(test2)
'''


if __name__ == "__main__":
	# dataset 1 and 2 have negative cycles
	pset_4("/home/damian/Dropbox/Algorithms/johnson_data_3.txt")

'''
data_2 = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/johnson_data_1.txt', skip_header = 1)
the_file = open('/home/damian/Dropbox/Algorithms/johnson_data_1.txt', 'r')
header = the_file.readline()
header = header.split(' ') 
clean_header = [''.join(char for char in string if char.isalnum()) for string in header]
num_vertices = int(clean_header[0])
num_edges = int(clean_header[1])


data_3 = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/johnson_data_1.txt', skip_header = 1)
the_file = open('/home/damian/Dropbox/Algorithms/johnson_data_1.txt', 'r')
header = the_file.readline()
header = header.split(' ') 
clean_header = [''.join(char for char in string if char.isalnum()) for string in header]
num_vertices = int(clean_header[0])
num_edges = int(clean_header[1])
'''
