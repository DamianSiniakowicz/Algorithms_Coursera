def computerNetwork(n, network):
	# use undirected djikstra to get from 1 to n
	
	from collections import Set

	class edge(object):
		def __init__(self,edge_list):
			self.origin = edge_list[0]
			self.destination = edge_list[1]
			self.distance = edge_list[2]
		def __lt__(self,other):
			if self.distance < other.distance:
				return True
			else:
				return False
		def get_origin(self):
			return self.origin
		def get_destination(self):
			return self.destination
		def get_distance(self):
			return self.distance
		def set_distance(self,distance):
			self.distance = distance

	def update_edges(list_of_edges,visited_nodes,greedy_dists,newly_added):
		keep_edges = []
		for index in range(len(list_of_edges)):
			edge = list_of_edges[index]
			if edge.get_destination() not in visited_nodes or edge.get_origin() not in visited_nodes:
				keep_edges.append(index)
				if edge.get_destination() == newly_added or edge.get_origin() == newly_added:
					edge.set_distance(greedy_dists[newly_added] + edge.get_distance())
					list_of_edges[index] = edge
		edge_list = [list_of_edges[edge] for edge in keep_edges]
		edge_list = sorted(edge_list)

		return edge_list

	edges = [edge(network_edge) for network_edge in network]
	edges = sorted(edges)

	greedy_distances = {}
	greedy_distances[1] = 0

	visited = set([1])
	while n not in visited:
		for index in range(len(edges)):
			edge = edges[index]
			if edge.get_origin() in visited and edge.get_destination() not in visited:
				greedy_distances[edge.get_destination()] = edge.get_distance()
				edges.pop(index)
				visited.add(edge.get_destination())
				edges = update_edges(edges,visited,greedy_distances,edge.get_destination())
				break
			elif edge.get_destination() in visited and edge.get_origin() not in visited:
				greedy_distances[edge.get_origin()] = edge.get_distance()
				edges.pop(index)
				visited.add(edge.get_origin())
				edges = update_edges(edges,visited,greedy_distances,edge.get_origin())
				break
	return greedy_distances[n]
