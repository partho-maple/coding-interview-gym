

# Solution 1
# Upper Bound: O((n*(2nn)!) / (n!(n+1)!))  time | O(n) space
def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
    numberOfTotalTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTree = numberOfBinaryTreeTopologies(leftTreeSize)
        numberOfRightTree = numberOfBinaryTreeTopologies(rightTreeSize)
        numberOfTotalTrees += numberOfLeftTree * numberOfRightTree
    return numberOfTotalTrees



# Solution 2
# Upper Bound: O(n^2)  time | O(n) space
def numberOfBinaryTreeTopologies(n, cache = {0: 1}):
    if n in cache:
        return cache[n]
    numberOfTotalTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTree = numberOfBinaryTreeTopologies(leftTreeSize, cache)
        numberOfRightTree = numberOfBinaryTreeTopologies(rightTreeSize, cache)
        numberOfTotalTrees += numberOfLeftTree * numberOfRightTree
    cache[n] = numberOfTotalTrees
    return numberOfTotalTrees



# Solution 3
# O(n^2)  time | O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for m in range(1, n + 1):
        numberOfTotalTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTree = cache[leftTreeSize]
            numberOfRightTree = cache[rightTreeSize]
            numberOfTotalTrees += numberOfLeftTree * numberOfRightTree
        cache.append(numberOfTotalTrees)
    return cache[n]




