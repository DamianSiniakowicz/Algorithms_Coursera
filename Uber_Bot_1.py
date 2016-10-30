
#address : string ... user input (located at [0,0])
#objects : list int ... locations of names either [x,y] or [x_start,y_start,x_end,y_end]
#names : list string ... names of locations
import math
def closestLocation(address, objects, names):

	def same_prefix(user_string,location):
		location = location.lower()
		try:
			test = location[len(user_string)-1]
			location = location[:len(user_string)]
			return location == user_string
		except IndexError:
			return False

	def diff_by_one(user_string,location):
		location = location.lower()
		try:
			test = location[len(user_string)-1]
			tot_diff = 0
			location = location[:len(user_string)]
			for index in range(len(user_string)):
				if user_string[index] != location[index]:
					tot_diff += 1
					if tot_diff > 1:
						return False
			if tot_diff == 1:
				return True
			else:
				return False
		except:
			return False

	def has_extra(user_string,location):
		location = location.lower()
		try:
			test = location[len(user_string)-2]
			location = location[:len(user_string)-1]
			extra_char_index = None
			for index in range(len(location)):
				if user_string[index] != location[index]:
					extra_char_index = index
					break
			else:
				extra_char_index = len(location)
			user_index = 0
			for index in range(len(location)):
				if index == extra_char_index:
					user_index += 1
				if location[index] != user_string[user_index]:
					return False
				user_index += 1
			else:
				return True
		except IndexError:
			return False

	def missing_one(user_string,location):
		location = location.lower()
		try:
			test = location[len(user_string)]
			extra_char_index = None
			for index in range(len(user_string)):
				if location[index] != user_string[index]:
					extra_char_index = index
					break
			else:
				extra_char_index = len(user_string)
			location_index = 0
			for index in range(len(user_string)):
				if index == extra_char_index:
					location_index += 1
				if user_string[index] != location[location_index]:
					return False
				location_index += 1
			else:
				return True
		except IndexError:
			return False

	def point_point_distance(first,second):
		return math.sqrt((first[0]-second[0])**2 + (first[1]-second[1])**2)

	def point_segment_distance(point,segment):
		if len(segment) == 2:
			return point_point_distance(point,segment)
		seg_x_range, seg_y_range = [segment[0],segment[2]], [segment[1],segment[3]]
		seg_x_max, seg_x_min = max(seg_x_range), min(seg_x_range)
		seg_y_max, seg_y_min = max(seg_y_range), min(seg_y_range)
		point_x, point_y = point[0], point[1]
		if seg_x_max == seg_x_min:
			if point_y >= seg_y_min and point_y <= seg_y_max:
				return abs(point_x - seg_x_max)
			elif point_y > seg_y_max:
				return point_point_distance(point,[seg_x_max,seg_y_max])
			else:
				return point_point_distance(point,[seg_x_max,seg_y_min])

		else:
			if point_x >= seg_x_min and point_x <= seg_x_max:
				return abs(point_y - seg_y_min)
			elif point_x > seg_x_max:
				return point_point_distance(point,[seg_x_max,seg_y_min])
			else:
				return point_point_distance(point,[seg_x_min,seg_y_max])

	functions = [same_prefix,diff_by_one,has_extra,missing_one]
	address = address.lower()
	user_location = [0,0]
	potential_matches = [ [funk(address,destination) for funk in functions] for destination in names ]
	match_boolean = [any(match_criteria) for match_criteria in potential_matches]
	matches = [x for x in range(len(match_boolean)) if match_boolean[x]]
	for match in matches: print names[match]
	distances = [point_segment_distance(user_location,objects[match]) for match in matches]
	return names[matches[distances.index(min(distances))]] # return the nearest matching object

	# pass 4 string functions to map or something awesome like that

# distance = euclidean dist between closest two points
# match = look at prefix (stuff before first space). not case sensitive 
	# if user and address the same : MATCH
	# if user and address differ by one char : MATCH
	# if user's input has one extra symbol : MATCH
	# if user's input has one missing symbol : MATCH
# distance from segment to point
	# if segment is vertical
		# if point's y coor is in the y-range of segment then dist = difference in x's
		# else : if point is above seg, take dist to seg's highest point, else take dist to seg's lowest point 
	# elif segment is horizontal
		# if point's x coor is in the x-range of segment then dist = difference in y's
		# else : if point is left of seg, take dist to seg's leftest point, else take dist to seg's rightest point 

'''
Functions to test

1.) get_prefix
2.) same_prefix
3.) diff_by_one
4.) has_extra
5.) missing_one
6.) point_point_distance
7.) point_segment_distance



'''





















