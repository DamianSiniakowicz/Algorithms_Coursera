from collections import Set
import copy
my_tree = {"A": ["B","C"], "B":["D","E"], "C":["F","G"],"D":[],"E":[],"F":[],"G":[]}

def bfs(tree,goal,explored=set([]),start="A",paths=[]):
	paths.append([start])
	while paths != []:
		path = paths.pop(0)
		last_node = path[-1]
		if last_node == goal:
			print "path to goal: ",path
			return path
		for node in tree[last_node]: 
			if node not in explored:
				new_path = copy.copy(path)
				new_path.append(node)
				paths.append(new_path)
				print "new path: ", new_path
		explored.add(last_node)


	else:
		print "no path found"
		return None




def dfs(tree,goal,explored=set([]),start="A",paths=None):
	if paths == None:
		paths = [[start]]
	if paths == []:
		print "no path found"
		return None
	path = paths.pop()
	last_node = path[-1]
	if last_node == goal:
		print "found path to goal: ", path
		return path
	for node in tree[last_node]:
		if node not in explored:
			new_path = copy.copy(path)
			new_path.append(node)
			paths.append(new_path)
			print "new path: ", new_path
	explored.add(last_node)
	return dfs(tree,goal,paths=paths)


adj_list
adj_mat
import random
def get_min_cut(adj_list,adj_mat):
	def count_vertices_edges(adj_list):
		tot_vert = 0
		tot_edge = 0
		for x in adj_list:
			tot_vert +=1
			tot_edge += len(adj_list[x])
		return tot_vert, tot_edge/2
	def count_edges(adj_list)
	num_vert, num_edge = count_vertices(adj_list)
	for join in range(num_vert-2):
		while True:
			first_vert = random.choice(range(num_vert))
			second_vert = random.choide(range(num_vert))
			if adj_mat[(first_vert,second_vert)] == True:




def get_SCC(graph):
	pass




if __name__ == "__main__":
