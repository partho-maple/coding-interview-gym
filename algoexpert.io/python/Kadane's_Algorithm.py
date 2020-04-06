# https://www.algoexpert.io/questions/Kadane's%20Algorithm


# O(n) time | O(1) space - where n is the length of the   input array
def kadanesAlgorithm(array):
    maxEdingHere, maxSoFar = array[0], array[0]
	for i in range(1, len(array)):
		num = array[i]
		maxEdingAtPrevIdx = maxEdingHere
		maxEdingHere = max(num, num + maxEdingAtPrevIdx)
		maxSoFar = max(maxSoFar, maxEdingHere)
	return maxSoFar

