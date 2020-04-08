def maxSumIncreasingSubsequence(array):
    sequeces = [None for _ in array]
	sums = [num for num in array]
	maxSumIdx = 0
	for i in range(len(array)):
		currentum = array[i]
		for j in range(0, i):
			otherum = array[j]
			if otherum < currentum and sums[j] + currentum >= sums[i]:
				sums[i] = sums[j] + currentum
				sequeces[i] = j
		if sums[maxSumIdx] <= sums[i]:
			maxSumIdx = i
	increasigSequence = buildSequece(array, sequeces, maxSumIdx)
	return [sums[maxSumIdx], increasigSequence]

def buildSequece(array, sequeces, curIdx):
	sequen = []
	while curIdx is not None:
		sequen.append(array[curIdx])
		curIdx = sequeces[curIdx]
	return list(reversed(sequen))

