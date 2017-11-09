def findSmallest(arr):
	smallest = arr[0]
	smallest_index=0
	for i in range(1,len(arr)):
		if smallest>arr[i]:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	newArr = []
	for i in range(1,len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

list= [5,2,6,9,22,54,23,67]
print(findSmallest(list))
print(selectionSort(list))
