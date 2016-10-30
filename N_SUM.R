#!usr/env/bin python

import numpy
from collections import Set

data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/Sum2N_Data.txt')

nums_summed = set([])

# just do a double for loop

for i in range(1:1000000):
	for j in range(i:1000000):
		x_plus_y = data[i] + data[j]
		if x_plus_y not in nums_summed:
			nums_summed.add(x_plus_y)

print(len(nums_summed))


