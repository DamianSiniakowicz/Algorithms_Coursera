#!/usr/env/bin python


'''
maintain two heaps
one for lower half (inverted to that min gets you the largest number ie. instead of inserting x, you insert -x)
one for upper half

compare each new number to min of the upper half and max of the lower half
place it inside the appropriate half
if one heap is more than 1 item larger than other, move over its min to the other heap

get median
if odd number of elements, get min of larger heap
if even number of elements, get min of smaller heap


'''


from heapq import * 

import numpy, random

data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/median_data.txt')

medians = [data[0],min(data[0],data[1])]

lower = [-(min(data[0],data[1]))]
heapify(lower)

upper = [max(data[0],data[1])]
heapify(upper)

for k in range(2,10000):
	# add to the correct heap
	if data[k] >= nsmallest(1,upper)[0]:
		heappush(upper,data[k])
	elif data[k] <= -(nsmallest(1,lower)[0]):
		heappush(lower,-data[k]) # alias? no...
	else:
		up = random.choice([0,1])
		if up:
			heappush(upper,data[k])
		else:
			heappush(lower,-data[k])
	# rebalance heaps
	if abs(len(upper) - len(lower)) > 1:
		if len(lower) > len(upper):
			immigrant = -heappop(lower)
			heappush(upper,immigrant)			
		else:
			immigrant = heappop(upper)
			heappush(lower,-immigrant)
	# get median 
	if k % 2 == 1 or len(lower) > len(upper): 
		medians.append(-(nsmallest(1,lower)[0]))	
	else:
		medians.append(nsmallest(1,upper)[0])

print sum(medians) % 10000
		

# 1213















