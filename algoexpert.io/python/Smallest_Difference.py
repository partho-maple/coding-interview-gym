# O(nlog(n) + mlon(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
	array_one, array_two = sorted(arrayOne), sorted(arrayTwo)
    index_one, index_two = 0, 0
    smallestDiff = float("inf")
	result_pair = []
    while index_one < len(array_one) and index_two < len(array_two):
        first_num = array_one[index_one]
        second_num = array_two[index_two]
		currentDiff = abs(first_num - second_num)
        if currentDiff < smallestDiff:
			smallestDiff = currentDiff
			result_pair = [first_num, second_num]
		if first_num <= second_num:
			index_one += 1
		else:
			index_two += 1
    return result_pair
    

