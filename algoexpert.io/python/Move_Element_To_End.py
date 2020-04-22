def moveElementToEnd(array, toMove):
    left, right = 0, len(array) - 1
	while left < right:
		if array[right] == toMove:
			right -= 1
		if array[left] != toMove:
			left += 1
		if array[left] == toMove and array[right] != toMove:
			array[left], array[right] = array[right], array[left]
	return array
