#!/usr/env/bin python

# of bellman-ford : gets shortest path or returns a negative cycle. to detect negative cycle, check for difference between n-1 and n edge budget results. 

# weirdo bellman-ford:
# loop over edge budgets
	# on odd edge budgets
		# check vertices from 1 to n
		# only use forward edges. ie. 
		# recurrence is min of A[i-1,v] and A[i,u] + C_u_v where u < v
	# on even edge budgets 	
		# check vertices from n to 1 
		# only use backward edges. ie. (u,v) where u > v		
		# recurrence is min of A[i-1,v] and A[i,u] + C_u_v where u > v	

# Question : computes shortest path ...
# 3.) iff no negative cycle
# 4.) always and faster than Bellman-Ford

import numpy
from collections import defaultdict
'''
data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/bell_data.txt')


sink_to_sources = defaultdict(list)

budget_dest_to_dist = {}

edges_to_dist = {}


for entry in data:
	source = entry[0]
	dest = entry[1]
	dist = entry[2]
	sink_to_sources[dest].append(source)
	edges_to_dist[(source,dest)] = dist	

source = 0
n = 4

for edge_budget in range(4):
	if edge_budget % 2 == 0:
		for vertex in range(n-1,-1,-1):
			if edge_budget == 0 and vertex != source:
				budget_dest_to_dist[(edge_budget,vertex)] = float('inf')
				continue
			elif edge_budget == 0 and vertex == source:
				budget_dest_to_dist[(edge_budget,vertex)] = 0  
				continue
			one_less = budget_dest_to_dist[(edge_budget-1,vertex)]
			others = [budget_dest_to_dist[(edge_budget,new_dest)] + edges_to_dist.get((new_dest,vertex),float('inf')) for new_dest in sink_to_sources[vertex] if new_dest > vertex]			
			others.append(one_less)
			budget_dest_to_dist[(edge_budget,vertex)] = min(others)  		
	else:
		for vertex in range(n):
			if edge_budget == 0 and vertex != source:
				budget_dest_to_dist[(edge_budget,vertex)] = float('inf')
				continue
			elif edge_budget == 0 and vertex == source:
				budget_dest_to_dist[(edge_budget,vertex)] = 0
				continue
			one_less = budget_dest_to_dist[(edge_budget-1,vertex)]
			others = [budget_dest_to_dist[(edge_budget,new_dest)] + edges_to_dist.get((new_dest,vertex),float('inf')) for new_dest in sink_to_sources[vertex] if new_dest < vertex]	
			others.append(one_less)		
			budget_dest_to_dist[(edge_budget,vertex)] = min(others)			
		

for dest in range(4):
	print "dist to vertex",dest,"is",budget_dest_to_dist[(3,dest)]
'''

# weird floyd-warshall

# Question : what is it doing? What is A[i,j,n]?
# 1.) length of longest path from i to j
# 2.) number of shortest paths from i to j
# 3.) number of simple (cycle-free) paths from i to j ***
# 4.) none of the above

# algo
# A[i,j,0] = 1 iff (i,j) is an edge, 0 otherwise
# A[i,j,k] = A[i,j,k-1] + A[i,k,k-1] * A[k,j,k-1]

data_file = open('/home/damian/Dropbox/Algorithms/weird_floyd.txt','r')

num_vertices = data_file.readline()

num_vertices = int(''.join([char for char in num_vertices if char.isalnum()]))

data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/weird_floyd.txt',skip_header = 1)

i_j_has_edge = {}

for entry in data:
	i = entry[0]
	j = entry[1]
	i_j_has_edge[(i,j)] = True

i_j_k_val = {}

for vert_prefix in range(num_vertices+1):
	for source in range(1,num_vertices+1):
		for dest in range(1,num_vertices+1):
			if vert_prefix == 0:
				if i_j_has_edge.get((source,dest),False):
					i_j_k_val[(source,dest,vert_prefix)] = 1
				else:
					i_j_k_val[(source,dest,vert_prefix)] = 0
			else:
				i_j_k_val[(source,dest,vert_prefix)] = i_j_k_val[source,dest,vert_prefix-1] + i_j_k_val[source,vert_prefix,vert_prefix-1] * i_j_k_val[vert_prefix,dest,vert_prefix-1]

for source in range(1,num_vertices+1):
	for dest in range(1,num_vertices+1):
		print 'value for source vertex',source,'and destination vertex',dest,':',i_j_k_val[(source,dest,num_vertices)]


