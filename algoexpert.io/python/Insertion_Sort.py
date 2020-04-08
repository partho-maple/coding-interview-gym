


# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insertionSort(array):
 	for i in range(1, len(array)):
 		j = i
 		while j > 0 and array[j] < array[j - 1]:
 			swap(j, j - 1, array)
 			j -= 1
 	return array
def swap(i, j, array):
 	array[i], array[j] = array[j], array[i]


input_array = [8, 5, 2, 9, 5, 6, 3]
sorted_array = insertionSort(input_array)
print("Sorted Array: ", sorted_array)