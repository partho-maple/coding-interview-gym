def numberOfBinaryTreeTopologies(n, cache={0: 1}):
    if n in cache:
		return cache[n]
	numbersOfTree = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - 1 - leftTreeSize
		numOfLeftTree = numberOfBinaryTreeTopologies(leftTreeSize, cache)
		numOfRigntTree = numberOfBinaryTreeTopologies(rightTreeSize, cache)
		numbersOfTree += numOfRigntTree * numOfLeftTree
	cache[n] = numbersOfTree
	return numbersOfTree