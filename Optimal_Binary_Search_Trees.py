#!/usr/env/bin python


key_probability = {1 : .2 ,2: .05,3: .17,4: .1,5: .2,6: .03,7: .25}

contiguous_subset_optimal_cost = {}

# recurrence : = min over all choices of root of:  sum(all probabilities in the contig set) + left_tree + right_tree
########################



# fill in the table

for size in range(1,8):
	for i in range(1,9-size): 
		j = i + size - 1
		contig_set = range(i,j+1)
		if len(contig_set) == 1:
			contiguous_subset_optimal_cost[(i,j)] = key_probability[i]
			continue
		best = None
		possible = None
		for root in contig_set:
			if contig_set.index(root) != 0 and contig_set.index(root) != len(contig_set) - 1: # root in middle
				possible = sum([key_probability[index] for index in contig_set]) +  contiguous_subset_optimal_cost[(i,root-1)] + contiguous_subset_optimal_cost[(root+1,j)]
				if best == None or possible < best:
					best = possible
			elif contig_set.index(root) == 0: # root is left-most node
				possible = sum([key_probability[index] for index in contig_set]) + contiguous_subset_optimal_cost[(root+1,j)]
				if best == None or possible < best:
					best = possible
			else: # root is right-most node
				possible = sum([key_probability[index] for index in contig_set]) + contiguous_subset_optimal_cost[(i,root-1)]			
				if best == None or possible < best:
					best = possible
		contiguous_subset_optimal_cost[(i,j)] = best
	

print(contiguous_subset_optimal_cost[(1,7)])
