#!/usr/env/bin python


'''
# answer is 106

# goal : size 4 cluster max spacing


######

import numpy
from unionfind import *
from operator import itemgetter

# read in data

data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/cluster_1_data.txt',skip_header=1)

UF = unionfind(500) # how many nodes?

# sort a list of edge indices of length = number edges, where the sorting key is the edge length

edges = range(len(data))

sorted_edges = sorted(edges, key = lambda edge: data[edge,2])

# loop through the edges from cheapest to most expensive

print(max(sorted_edges))

for edge_index in sorted_edges:
	print sorted_edges.index(edge_index)
	first_node = int(data[edge_index,0] - 1) 
	second_node = int(data[edge_index,1] - 1)
	if not (UF.issame(first_node,second_node)):
		UF.unite(first_node,second_node)
		if len(UF.groups()) < 4:
			answer = data[edge_index,2]
			break

print answer
'''		
import numpy, time
from unionfind import *
from MTREE import *

def solve_problem():
	
	# Goal
	# find all pairs of nodes that are 0 away, then all pairs that are 1 away, and finally all pairs that are 2 away.
	# Problem
	# current implementation does the following
		# for each node .. there are 200,000
			# find all nodes 0 away. if doesn't form loop, join.
			# find all nodes 0 or 1 away. if dist not 0 and doesn't form loop, join.
			# find all nodes 0, 1 or 2 away. if dist not 0 or 1 and doesn't form loop, join
			# find all nodes 0, 1, 2 or 3 away
	# very redundant
		# looking at pairs too close to one another (ex. we're looking for 2 apart, but need to go through 0's and 1's again)
		# looking at pairs twice (ex. all nodes 0 away from node x might include y, then we do the same query for node y)
	# Solution to distance redundancy
		# key idea : first generate all neighbor_iterators for distance 3. neighbors listed in increasing distance order
		# initialize first_new_dist_neighbor {home: neighbor}
		# loop through distances 0 to 3
			# go through everything in first_new_dist_neighbor, then clear it. (if you add a dist3, break)
			# for each neighbor_iterator (as soon as you add a dist 3 break)
				# keep going until you hit a neighbor with distance+1 , put that guy in the first_new_dist
	# Pair Redundancy
	# just going through the 0-dist pairs will take 6 hours. Need to tackle redundancy

	# put everything in an M-Tree
	# loop through all nodes, query all nodes 0 away, check for cycles, unify, etc. will need to store nodes as a tuple (index,code) so i use UF
	# repeat until you add your first length 3 edge
	# it's pretty inefficient to query all nodes 0 away for every single node. would be get a list of pairs instead.

	data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/cluster_2_data.txt',skip_header=1)

	Clusters = unionfind(200000)

	def hamming_distance(x_index,y_index):
		'''
		x : numpy array
		y : numpy array
		
		return -> int
			the hamming distance between x and y
		'''
		x = data[x_index,:]
		y = data[y_index,:]
		answer = sum(x != y)
		return answer 

	lookup_tree = MTree(distance_function = hamming_distance)

	for index in range(200000):
		print "index",index
		lookup_tree.add(index)

	for distance in range(3,4): 
		print "looking at distance",distance
		for node_1_index in range(200000):
			print "looking at node",node_1_index,"'s neighbors"
			t8 = time.time()
			# neighbor lookup : this is fine
			neighbors = lookup_tree.get_nearest(node_1_index,distance)
			t9 = time.time()
			print t9-t8,"time needed to find neighbors"		
			# time neighbor calculations : this is taking too long
			t2 = time.time()
			# from here
			un_find_tot = 0
			for neighbor in neighbors:
				dist = neighbor[1]
				#if dist < distance:
				#	continue
				neighbor = neighbor[0]
				# to here, is too slow
				t0 = time.time()	
				if not Clusters.issame(node_1_index,neighbor): # union-find is fast
					Clusters.unite(node_1_index,neighbor)
					# need to break off if clust_dist >= 3
				t1 = time.time()
				un_find_tot += t1-t0
					
			t3 = time.time()
			tot = t3 - t2
			rest = tot - un_find_tot
			print un_find_tot, "time required for union-find operations"	
			print rest,"time required for other calculations"
'''
def do_it():

	import numpy
	from unionfind import * 
	from collections import defaultdict

	Clusters = unionfind(200000)

	data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/cluster_2_data.txt',skip_header=1)

	comparator = numpy.ones(24)

	num_dif_to_nodes = defaultdict(list)

	for node_index in range(200000):
		node = data[node_index,:]
		diff = sum(node != comparator)
		num_dif_to_nodes[diff].append(node_index)


	for difference_we_want in range(4): # as soon as you hit the first non-cycle 3 edge, break
		print "difference we want:",difference_we_want
		for node_difference in range(difference_we_want+1):
			print "difference we're looking at",node_difference
			for x_difference in range(25):
				print "xdif",x_difference
				y_difference = min((x_difference + node_difference),24)
				print "ydif",y_difference
				if x_difference == y_difference:
					if len(num_dif_to_nodes[x_difference]) < 2:
						continue 
					for node_index in range(len(num_dif_to_nodes[x_difference])-1): # need to compare all, not just consecutive
						node_1_index = num_dif_to_nodes[x_difference][node_index] - 1 # index of node in: data
						node_2_index = num_dif_to_nodes[x_difference][node_index+1] - 1 # index of node in: data
						node_1 = data[node_1_index,:]
						node_2 = data[node_2_index,:]
						diff = sum(node_1 != node_2)
						if diff == 3 and difference_we_want == 3 and Clusters.issame(node_1_index,node_2_index):
							Clusters.unite(node_1_index,node_2_index)
							print "the answer"
							print Clusters.groups()							
							return
						elif diff == difference_we_want and Clusters.issame(node_1_index,node_2_index):
							Clusters.unite(node_1_index,node_2_index)
				else:
					if len(num_dif_to_nodes[x_difference]) < 1 or len(num_dif_to_nodes[y_difference]) < 1:
						continue
					# loop through eligible node_pairs, unite if not the same
					for node_1_index in num_dif_to_nodes[x_difference]:
						for node_2_index in num_dif_to_nodes[y_difference]:
							node_1 = data[node_1_index,:]
							node_2 = data[node_2_index,:]
							diff = sum(node_1 != node_2)
							if diff == 3 and difference_we_want == 3 and Clusters.issame(node_1_index,node_2_index):
								Clusters.unite(node_1_index,node_2_index)
								return(Clusters.groups())
							elif diff == difference_we_want and Clusters.issame(node_1_index,node_2_index):
								Clusters.unite(node_1_index,node_2_index)

# if node A has x differences with 1111111111111111111
# and node B has y differences with 1111111111111111111
# then A and B have at most min(24, x+y) differences with one another and a least abs(x-y) differences with one another
# use a heap to store node pairs and their 


# we only need to look at edges with lengths 0, 1 and 2, the value of k when we first use a length 3 edge to connect clusters is our answer.

# length 0 edge candidates : edges connecting nodes whose differences with 111111111111 are x and y s.t. abs(x-y) = 0
# length 1 edge candidates : edges connecting nodes whose differences with 111111111111 are x and y s.t. abs(x-y) = 1
# length 2 edge candidates : edges connecting nodes whose differences with 111111111111 are x and y s.t. abs(x-y) = 2 
# etc. 
'''
'''
def take_two():
	import numpy, time
	from unionfind import *
	from heapq import *	

	data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/cluster_2_data.txt',skip_header=1)

	clusters = unionfind(200000)

	heap = []

	def hamming_distance(x_index,y_index):
		
		x = data[x_index,:]
		y = data[y_index,:]
		answer = sum(x != y)
		return answer
	
	# super fast double for loop over all nodes, store edges of length <= 2 in heap. Then heappop and if issame: unite until the heap is empty. Then return the number of clusters 
'''
import numpy, time
from unionfind import *
from heapq import * 


data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/cluster_2_data.txt',skip_header=1)

def hamming_distance(x_index,y_index):
	x = data[x_index,:]
	y = data[y_index,:]
	answer = sum(x != y)
	return answer



def take_three():

	X = 200000
	Y = 200000

	clusters = unionfind(200000)

	heap = []
	

	for i in range(X - 1):
		print i
		print "i = ",i
		for j in range(i+1,X):
			#print i,"...",j
			dist = hamming_distance(i,j)
			#print dist			
			if dist <= 2:
				heappush(heap,(dist,(i,j)))			
	while len(heap) > 0:
		dist, edge = heappop(heap)
		if not clusters.issame(edge[0],edge[1]):
			clusters.unite(edge[0],edge[1])
	print clusters.groups()	

'''
if __name__ == "__main__":
	take_three()
'''

take_three()


