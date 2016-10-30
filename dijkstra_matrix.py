def nightRoute(city):
	# use djikstra
	from collections import Set
	greedy_scores = {}
	for index in range(len(city)):
		if index == 0:
			greedy_scores[index] = 0
		elif city[0][index] > -1:
			greedy_scores[index] = city[0][index]
		else:
			greedy_scores[index] = float('inf')
	visited = set([0])
	while (len(city)-1) not in visited:
		closest_new_island = None
		new_island_score = None
		for island in visited:
			for next_island in range(len(city)):
				if next_island not in visited and city[island][next_island] > -1:
					score = greedy_scores[island] + city[island][next_island]
					if new_island_score == None or new_island_score > score:
						new_island_score = score
						closest_new_island = next_island
		greedy_scores[closest_new_island] = new_island_score
		visited.add(closest_new_island)
		for island in range(len(city)):
			if island not in visited and city[closest_new_island][island] > -1:
				if greedy_scores[island] > new_island_score + city[closest_new_island][island]:
					greedy_scores[island] = new_island_score + city[closest_new_island][island]
	return greedy_scores[len(city)-1]


# needs to be prettier, add functions