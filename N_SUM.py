#!usr/env/bin python

import numpy
from collections import Set

data = numpy.genfromtxt('/home/damian/Dropbox/Algorithms/Sum2N_Data.txt')

data.sort()

data = list(data)

data_set = set(data)

'''
nums_summed = set([])

# just do a double for loop

def find_min_index(x,end=1000000):
	
	Parameters
	==========
	x : int
		>= 0
	end : int
		<= 1000000

	Return
	======
	int : the smallest index such that the sum of data[x] and data[returned_index] is >= -10000
	
	if x == end:
		return corresponding_index
	number = data[x]
	rest_of_data = data[x:end]
	y = (x + end) // 2
	x_plus_y = number + data[y]
	if x_plus_y < -10000:
		return find_min_index((y+1),end) 	
	elif x_plus_y > -10000:
		if lowest_valid_sum is None or x_plus_y < lowest_valid_sum:
			global lowest_valid_sum
			lowest_valid_sum = x_plus_y
			global corresponding_index
			corresponding_index = y
		return find_min_index(x,y)
	else:
		return y	
 


for x in range(1000000):
	print "x =",x
	# using binary search, find the smallest y s.t. x + y >= -10000, then keep going until you hit a y s.t. x + y >= 10000 
	global lowest_valid_sum	
	lowest_valid_sum = None
	global corresponding_index
	corresponding_index = None	
	y = find_min_index(x)
	if y is None:
		continue
	print "start y =",y
	while y < 1000000 and data[x] + data[y] <= 10000 :
		number = data[x] + data[y]
		if number not in nums_summed:
			nums_summed.add(number)
		y += 1
	print "end y =",y

print(len(nums_summed))
'''
'''
def search_neighbors(index):
	
	Parameters
	==========
	index: int
		
	Returns
	=======
	boolean : does the index have identical neighbors
	
	val = data[index]
	below = index - 1
	above = index + 1
	if data[below] == val or data[above] == val:
		return True
	else:
		return False

def has_partner(index, x, t, start=0, end=1000000):
	
	Parameters
	==========
	index : int
		the index of x
	x : int
	
	t : int

	Return
	======
	boolean	: whether or not a partner exists at an index other than index
	
	if start == end:
		return False
	mid = (start + end) // 2
	if data[mid] == t - x:
		if mid != index:
			return True
		else:
			search_neighbors(index)			
	elif data[mid] > t - x :
		return has_partner(index,x,t,start,mid)
	else :
		return has_partner(index,x,t,(mid+1),end)

amount_found = 0

for t in range(-10000,10001):
	print t
	# start a beginning of data, look for y = t - x
	for index in range(1000000):
		x = data[index]
		found_partner = has_partner(index, x, t)
		if found_partner:
			amount_found += 1
			break
'''

for t in range(-10000,10001):
	print t
	for index in range(1000000): # linear scan too slow, try binary search
		x = data[index]
		y = t - x
		if y in data_set:
			if y != x:
				amount_found += 1
				break
			elif data.count(y) > 1:
				amount_found += 1
				break
		




print amount_found

































