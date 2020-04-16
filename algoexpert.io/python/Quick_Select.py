def quickselect(array, k):
    position = k - 1
	return quickSelectHelper(array, 0, len(array) - 1, position)

def quickSelectHelper(array, srtIdx, endIdx, position):
	while True:
		if srtIdx > endIdx:
			raise Exception("Algorrithm should never be here!")
		pivotIdx = srtIdx
		leftIdx = srtIdx + 1
		rightIdx = endIdx
		while leftIdx <= rightIdx:
			if array[leftIdx] > array[pivotIdx] > array[rightIdx]:
				array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
			if array[leftIdx] <= array[pivotIdx]:
				leftIdx += 1
			if array[rightIdx] >= array[pivotIdx]:
				rightIdx -= 1
		array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]
		if rightIdx == position:
			return array[position]
		elif rightIdx > position:
			endIdx = rightIdx - 1
		else:
			srtIdx = rightIdx + 1
