def binary_search(list,item):
	low = 0
	high = len(list)-1

	while low <= high:
		mid = (high+low)//2
		guess = list[mid]

		if guess == item:
			return mid
		if guess < item:
			low = mid + 1
		else:
			high = mid
	return None

num_list = [1,3,5,7,9]
print(binary_search(num_list,5))
