#!/usr/env/bin/ python


# goal : return true if there is a strongly connected component which contains all vertices exactly once. 

# var : each var has two vertices, one for true and one for false

# clause : each clause has two directed edges, pointing from one var to the other.

##############################################################################################################


# import data

# create graph. 

# calculate SCC's.

from collections import Set, defaultdict
import numpy, random, copy, sys

sys.setrecursionlimit(1000000000)

def papa(i):
	'''
	i : int
	'''


	prefix = '/home/damian/Dropbox/Algorithms/2_SAT_DATA_'
	number = str(i)
	suffix = '.txt'
	path = ''.join([prefix,number,suffix])
	File = open(path,'r')
	num_var_clause = File.readline()
	num_var_clause = int(''.join([char for char in num_var_clause if char.isalnum()]))
	data = numpy.genfromtxt(path,skip_header=1)
	data = [tuple(pair) for pair in data]
	clause_data = tuple(data)
	variables = {}
	
	for run in xrange(int(round(numpy.log2(num_var_clause)))):
		print "file:",i,"...","run:",run
		for variable in range(1,num_var_clause+1):
			if random.random() >= .5:
				variables[variable] = True
				variables[-variable] = False
			else:
				variables[variable] = False
				variables[-variable] = True
		for attempt in xrange(2*num_var_clause**2):
			for clause in clause_data:
				if not variables[clause[0]] and not variables[clause[1]]:
					if random.random() >= .5:
						variables[clause[0]] = True
						variables[-clause[0]] = False
					else:
						variables[clause[1]] = True
						variables[-clause[1]] = False
					break
			else:
				print "solution found for file",file_number
				return 							

	else:
		print "no solution found for file",file_number
		return	 
	
for file_number in range(1,7):
	papa(file_number)	
	
