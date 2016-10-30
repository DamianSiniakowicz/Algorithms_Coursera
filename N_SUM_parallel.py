#!/usr/env/bin

# answer is 427 ?


import numpy

from multiprocessing import Pool

data = numpy.genfromtxt('/home/Damian/Dropbox/Algorithms/Sum2N_Data.txt')

data = list(data)

data.sort()

data_set = set(data)

def has_pair_sum(t):
	'''
	Determines whether or not there exist two distinct elements, x and y, in the data set s.t. x + y = t
	
	Parameters
	==========
	t : int
		the number we want to sum to

	Returns
	=======
	int: t or None
		returns t if such a pair exists, otherwise None 
	'''

	for index in range(1000000): # linear scan too slow, try binary search
		x = data[index]
		y = t - x
		if y in data_set and y != x:
			return t
			'''
				return t
			elif data.count(y) > 1:
				amount_found += 1
				return t
			'''
	else:
		return None
		

P =  Pool(20)
ans = P.map(has_pair_sum,range(-10000,10001))
ans = numpy.array(ans)

answers = map(lambda x: x is not None,ans)

print(sum(answers))


