#!usr/env/bin python

# Stack in DFS_1 and 2 should be a stack

from collections import Set
import numpy, random, copy, sys

sys.setrecursionlimit(1000000000)

edge_list = numpy.genfromtxt('/home/Damian/Dropbox/Algorithms/SCC_HW_Input.txt',dtype=int) # fill in the rest of the path

# test number of rows, does it equal 875,635 or whatever?

# construct vertex and reverse-vertex adjacency lists

forward_vertex_list = [[] for x in range(875714)]
reverse_vertex_list = [[] for x in range(875714)]

for i in range(len(edge_list)):
	edge = edge_list[i,:]

	# check lengths, add stuff if necessary
#	if len(forward_vertex_list) < edge[0]:
#		addition = [[] for x in range(len(forward_vertex_list),edge[0])]
#		forward_vertex_list.extend(addition)

#	if len(reverse_vertex_list) < edge[1]:
#		addition = [[] for x in range(len(reverse_vertex_list),edge[1])]	
#		reverse_vertex_list.extend(addition)		
	# add edge[0] to reverse_vertex_list[edge[1]]
	# add edge[1] to forward_vertex_list[edge[0]]

	forward_vertex_list[edge[0]-1].append(edge[1])
	reverse_vertex_list[edge[1]-1].append(edge[0])

# DFS-loop the rev-list and construct the finishing time to vertex dictionary
finish_time_to_vertex = [0 for x in range(len(forward_vertex_list))] # could just be a list
visited_nodes = set([]) # might be faster as a set
global finish_time
finish_time = 0

def DFS_1(Stack=None,start=None): # Stack could be an actual stack
	'''
	Stack : list
	start : int
	'''
	
	print "size of stack: ", len(Stack)

	if start != None:
		Stack.append(start)
		visited_nodes.add(start)
	if len(Stack) == 0:
		return
	
	next_up_list = reverse_vertex_list[Stack[len(Stack)-1]-1]
	add_to_stack = []	
	for next_up in next_up_list:
		if next_up not in visited_nodes:
			add_to_stack.append(next_up)
			visited_nodes.add(next_up)
	if len(add_to_stack) == 0:
		global finish_time
		finish_time_to_vertex[finish_time] = Stack[len(Stack)-1]
		finish_time += 1		
		dummy = Stack.pop()
		DFS_1(Stack)
		return
	else:
		Stack.extend(add_to_stack)
		DFS_1(Stack)
		return 

for node in range(1,len(forward_vertex_list)+1):
	print "part 1"
	print node,"/",875714
	if node not in visited_nodes:	
		DFS_1([],node)

# DFS loop the forward-list and count up the sizes of the SCCs.

SCC_Sizes = []
global last_stack_size
stack_size_before = 0
visited_nodes = set([]) # could be a set

def DFS_2(Stack=None,start=None): # Stack could be an actual stack
	'''
	Stack : list
	start : int
	'''
	
	print "size of stack: ", len(Stack)

	if start != None:
		Stack.append(start)	
		visited_nodes.add(start)
	if len(Stack) == 0:
		global stack_size_before		
		size = len(visited_nodes) - stack_size_before
		stack_size_before = len(visited_nodes)
		SCC_Sizes.append(size)  
		return 

	next_up_list = forward_vertex_list[Stack[len(Stack)-1]-1]
	add_to_stack = []	
	for next_up in next_up_list:
		if next_up not in visited_nodes:
			add_to_stack.append(next_up)
			visited_nodes.add(next_up)
	if len(add_to_stack) == 0:		
		dummy = Stack.pop()
		DFS_2(Stack)
		return
	else:
		Stack.extend(add_to_stack)
		DFS_2(Stack)
		return 
			


for finished in range(len(forward_vertex_list)-1, -1, -1):
	print "part 2"
	print finished,"/",0
	if finish_time_to_vertex[finished] not in visited_nodes:
		DFS_2([],finish_time_to_vertex[finished])	

# sort and return top 5

SCC_Sizes.sort()

print SCC_Sizes

if len(SCC_Sizes) >= 5:
	SCC_Sizes = SCC_Sizes[0:5]

else:	
	add_on = [0 for x in range(len(SCC_Sizes),5)]
	SCC_Sizes.extend(add_on)













	


