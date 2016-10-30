#!/usr/env/bin python
'''
import numpy

data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/knapsack_1_data.txt', skip_header = 1)

knapsack_capacity = 10000 
number_items = 100

weight_numitems_to_value = {}

for w in range(knapsack_capacity+1):
	for n in range(number_items+1):
		if w == 0 or n == 0:
			weight_numitems_to_value[(w,n)] = 0
		elif w - data[n-1,1] < 0:
			weight_numitems_to_value[(w,n)] = weight_numitems_to_value[(w,n-1)]
		else:
			option_1 = weight_numitems_to_value[(w,n-1)]
			option_2 = weight_numitems_to_value[(w-data[n-1,1],n-1)] + data[n-1,0]
			weight_numitems_to_value[(w,n)] = max(option_1,option_2)


print weight_numitems_to_value[(knapsack_capacity,number_items)]
'''

# answer = 2493893

import numpy
data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/knapsack_2_data.txt',skip_header = 1)

weight_numitems_to_value = {}

knapsack_capacity = 2000000

number_items = 2000

# value, weight
x = 0
def knapsack_recurse(w,n):
	'''
	w : int
	n : int
	
	return -> int
	''' # weight_numitems_to_value[(w,n)] =
	#print "w =",w,"... n =",n
	global x
	x += 1
	print "recursive call",x
	if w == 0 or n == 0:
		return 0
	elif w - data[n-1,1] < 0:
		if weight_numitems_to_value.get((w,n-1),'not_calculated') == 'not_calculated':
			weight_numitems_to_value[(w,n-1)] = knapsack_recurse(w,n-1)
		return weight_numitems_to_value[(w,n-1)]
		
	else:
		if weight_numitems_to_value.get((w,n-1),'not_calculated') == 'not_calculated':
			weight_numitems_to_value[(w,n-1)] = knapsack_recurse(w,n-1)
		if weight_numitems_to_value.get((w-data[n-1,1],n-1),'not_calculated') == 'not_calculated':
			weight_numitems_to_value[(w-data[n-1,1],n-1)] = knapsack_recurse(w-data[n-1,1],n-1)			
		return max(weight_numitems_to_value[(w,n-1)], (weight_numitems_to_value[(w-data[n-1,1],n-1)] + data[n-1,0]))

answer = knapsack_recurse(knapsack_capacity,number_items)

print answer

# ^ 10,629,293 recursive calls vs. 400,000,000 with Brute Force



