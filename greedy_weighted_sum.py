# 1.) 69119377652
# 2.) 67311454237


'''
import numpy

data = numpy.genfromtxt('/home/damian/Dropbox/wk1alg2data.txt',skip_header = 1)

Data = numpy.zeros([data.shape[0],3])

Data[:,0:2] = data

Data[:,2] = Data[:,0] - Data[:,1]

# decreasing order of weight length difference
# tie break by higher weight

from operator import itemgetter

Sorted_Data = sorted(Data, key = itemgetter(2,0), reverse = True)

# get the weighted completions. (keep running completion time)

completion_time = 0
weighted_completions = 0
for x in range(Data.shape[0]):
	completion_time += Sorted_Data[x][1]
	weighted_completions += completion_time * Sorted_Data[x][0]


# return sum of weighted completions


print(weighted_completions)


import numpy

data = numpy.genfromtxt('/home/damian/Dropbox/wk1alg2data.txt',skip_header = 1)

Data = numpy.zeros([data.shape[0],3])

Data[:,0:2] = data

Data[:,2] = Data[:,0] / Data[:,1]

# decreasing order of weight length difference
# tie break by higher weight

from operator import itemgetter

Sorted_Data = sorted(Data, key = itemgetter(2,0), reverse = True)

# get the weighted completions. (keep running completion time)

completion_time = 0
weighted_completions = 0
for x in range(Data.shape[0]):
	completion_time += Sorted_Data[x][1]
	weighted_completions += completion_time * Sorted_Data[x][0]


# return sum of weighted completions


print(weighted_completions)
'''

# get the cost of the min spanning tree

# skip_header = 1

# first_node second_node edge_cost

# edge_costs may be negative

# edge_costs need not be distinct

import numpy, random

#### algo

# visited : list of visited vertices
# not_visited : list of remaining vertices
# used_edge_lengths : list of edges

# randomly choose a vertex and put it in the visited list

# while there remain unvisited vertices
# loop through edges: choose the cheapest crossing edge WHAT ABOUT TIES??, update visited, not_visited, and used_edge_lengths

# sum up used_edge_lengths costs

# 500 verts 2184 edges

data = numpy.genfromtxt('/home/damian/Dropbox/mst_data.txt',skip_header = 1)

start_vertex = random.choice(range(1,501))

visited_vertices = [start_vertex]

not_visited_vertices = range(1,501)
not_visited_vertices.remove(start_vertex)

used_edge_lengths = []

while len(not_visited_vertices) > 0:
	print(len(not_visited_vertices))
	cheapest_length = None
	cheapest_edge = None
	connected_node = None
	for edge in range(len(data)):
		first_node = data[edge][0]
		second_node = data[edge][1] 		
		length = data[edge][2]
		if first_node in visited_vertices and second_node in not_visited_vertices: 
			if cheapest_length == None or cheapest_length > length:
				connected_node = second_node
				cheapest_edge = edge
				cheapest_length = length
		elif second_node in visited_vertices and first_node in not_visited_vertices: 
			if cheapest_length == None or cheapest_length > length:
				connected_node = first_node
				cheapest_edge = edge
				cheapest_length = length
	not_visited_vertices.remove(connected_node)
	visited_vertices.append(connected_node)
	used_edge_lengths.append(cheapest_length)

print(sum(used_edge_lengths))





# -3612829





































