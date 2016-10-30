def merge_sort(my_array):
	'''
	sort in increasing order
	'''
	if len(my_array) == 1:
		return my_array
	else:
		mid = len(my_array) / 2
		left = merge_sort(my_array[:mid])
		right = merge_sort(my_array[mid:])
		together = []
		left_ind = 0
		right_ind = 0
		while True:
			if left[left_ind] < right[right_ind]:
				together.append(left[left_ind])
				left_ind += 1
				if left_ind == len(left):
					together.extend(right[right_ind:])
					break
			else:
				together.append(right[right_ind])
				right_ind += 1
				if right_ind == len(right):
					together.extend(left[left_ind:])
					break
		return together


def quick_sort(my_array):
	'''
	sort in increasing order
	'''
	pivot_index = len(my_array) - 1
	next_cmp_index = 0

	if my_array == []:
		return []

	if len(my_array) == 1:
		return my_array
	
	while pivot_index - next_cmp_index > 1:
		if my_array[next_cmp_index] <= my_array[pivot_index]:
			next_cmp_index += 1
		else:
			my_array[next_cmp_index],my_array[pivot_index-1],my_array[pivot_index] = my_array[pivot_index-1], my_array[pivot_index], my_array[next_cmp_index] 
			pivot_index -= 1
	else:
		if my_array[pivot_index] < my_array[next_cmp_index]:
			my_array[pivot_index],my_array[next_cmp_index] = my_array[next_cmp_index],my_array[pivot_index]
			pivot_index -= 1
	return quick_sort(my_array[:pivot_index]) + [my_array[pivot_index]] + quick_sort(my_array[pivot_index+1:])