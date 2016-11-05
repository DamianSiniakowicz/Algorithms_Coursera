#!/usr/env/bin python

'''
import numpy, itertools

tsp_data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/tsp_data.txt',skip_header=1)

# 

node_distances = numpy.zeros([25,25])

for i in range(25):
	for j in range(i,25):
		if i == j:
			node_distances[i][j] = 0
		else:
			node_distances[i][j] = numpy.sqrt((tsp_data[i][0] - tsp_data[j][0])**2 + (tsp_data[i][1] - tsp_data[j][1])**2)	
			node_distances[j][i] = node_distances[i][j]



global_min_cost = float("inf")

# do we have to cycle through all the start vertices? yeah i guess so...

for i in range(25):
	print "start node",i
	Answers = {}
	max_set = None
	for path_length in range(25):
		print "path length",path_length
		candidates = range(25)
		candidates.remove(i)
		sets = itertools.combinations(candidates,path_length)
		# for each set of nodes of this size, loop over all possible destinations
		counter = 0
		for Set in sets:
			counter += 1
			print "count: ",counter
			Set = list(Set)
			Set.append(i)
			if len(Set) == 25:
				max_set = Set
			for j in Set:
				if j == i and path_length == 0:
					Answers[(tuple(Set),j)] = 0
				elif j == i and path_length != 0:
					Answers[(tuple(Set),j)] = float("inf")
				else: 
					possible = [Answers[(tuple([x for x in Set if x!=j]),k)] + node_distances[j][k] for k in Set if k!=j]
					Answers[(tuple(Set),j)] = min(possible)		
	# loop over max_size set's possible destination nodes, tack on hop back to i. take the min and compare to global_min_cost
	distances = [Answers[(tuple(max_set),j)] + node_distances[i][j] for j in range(25)]					
	# round down to nearest integer
	cheapest = int(min(distances)//1)
	if cheapest < global_min_cost:
		global_min_cost = cheapest
'''



# for every start and destination pair ij, find the shortest path that uses each node in S exactly once. 

# what should it look like

# define the special cases, when the Set includes only the start vertex and the destination vertex == the start vertex.

# how do i build the set S? Includes source and destination

# set size C from 0 to 24, get combination of size C, tack on source vertex to each combination, loop over possible destinations

# recurrence : take destination out of set, randomly choose a new destination from set. Return dist_from_new_to_old_dest + shortest path to new.
# we want the minimum over all choices of new destination. 

# base cases
# if source == new_dest and S has only source inside it then dist = 0
# if source == new_dest and S has other stuff inside it then dist is INF  

# after done, need to loop over all source-dest pairs of size S = 25, tack on cost of final hop back to source, find the min of all those



# strategy for reducing problem-space

# 1.) Sets considered : all node indices must be distance <= 5 from each other
# 2.) subproblems from which to calculate problem : all node indices must be distance <= 5 from each other (AFTER new_dest k is removed) 


import numpy, itertools

def satisfies_constraint(the_set):
	'''
	Ensures that all consecutive indices are within 5 of one another

	the_set : list

	Returns : bool	
	'''
	for i in range(len(the_set)-1):
		if abs(the_set[i] - the_set[i+1]) > 5:
			return False
	else:
		return True
			

import copy

def satisfies_constraint_without(the_set,*args):
	'''
	Checks whether the set satisfies the constraint once k is removed

	args : int

	the_set : list

	Returns : bool
	'''
	safe = copy.copy(the_set) 
	for arg in args:
		safe.remove(arg)
	return satisfies_constraint(safe)	



tsp_data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/tsp_data.txt',skip_header=1)

# 

node_distances = numpy.zeros([25,25])

for i in range(25):
	for j in range(i,25):
		if i == j:
			node_distances[i][j] = 0
		else:
			node_distances[i][j] = numpy.sqrt((tsp_data[i][0] - tsp_data[j][0])**2 + (tsp_data[i][1] - tsp_data[j][1])**2)	
			node_distances[j][i] = node_distances[i][j]



global_min_cost = float("inf")

# do we have to cycle through all the start vertices? yeah i guess so...

for i in range(1):
	print "start node",i
	Answers = {}
	max_set = None
	for path_length in range(25):
		print "path length",path_length
		candidates = range(25)
		candidates.remove(i)
		sets = itertools.combinations(candidates,path_length)
		# for each set of nodes of this size, loop over all possible destinations
		counter = 0
		for Set in sets:
			counter += 1
			print 'count',counter
			Set = list(Set)
			Set.append(i)
			if len(Set) == 25:
				max_set = Set
			safe_copy = copy.copy(Set)
			safe_copy = sorted(safe_copy)
			if not satisfies_constraint(safe_copy):
				continue
			for j in Set:
				if not satisfies_constraint_without(safe_copy,j):
					continue
				if j == i and path_length == 0:
					Answers[(tuple(Set),j)] = 0
				elif j == i and path_length != 0:
					Answers[(tuple(Set),j)] = float("inf")
				else: 
					possible = [Answers[(tuple([x for x in Set if x!=j]),k)] + node_distances[j][k] for k in Set if k!=j and satisfies_constraint_without(safe_copy,j,k)]
					Answers[(tuple(Set),j)] = min(possible)		
	# loop over max_size set's possible destination nodes, tack on hop back to i. take the min and compare to global_min_cost
	distances = [Answers.get((tuple(max_set),j),float('inf')) + node_distances[i][j] for j in range(25)]					
	# round down to nearest integer
	cheapest = int(min(distances)//1)
	if cheapest < global_min_cost:
		global_min_cost = cheapest



'''
TSP review

read in data
store nodes in a vector of 2-arrays. 

loop over nodes, where indices <=10 of each other
store distances between pairs in a map. store both permutations of vertices ex. {(x,y) -> 5, (y,x) -> 5}




loop over set size (btwn 2 and 25)
	loop over sets of that size (each set must contain 1, and consecutive elements' indices must be within 10 of each other)
		loop over nodes in the set (each member except 1 gets to try out being the destination node)
			base case : set size is 2. Path length is distance between nodes. 
			otherwise use the recurrence: dist from j to k plus min path to j using nodes in S except k.


'''
		























