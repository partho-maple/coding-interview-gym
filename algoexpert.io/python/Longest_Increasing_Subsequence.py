#   Solution 1
#   O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    if len(array) <= 1:
        return array
    sequences = [None for _ in range(len(array))]
    lengths = [1 for _ in range(len(array))]
    maxLenIdx = 0
    for i in range(len(array)):
        curNum = array[i]
        for j in range(i):
            otherNum = array[j]
            if otherNum < curNum and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
                maxLenIdx = i
    print("--------------")
    print("lengths: ", lengths)
    print("sequences: ", sequences)
    print("maxLenIdx: ", maxLenIdx)
    print("")
    return buildSequence(array, sequences, maxLenIdx)

def buildSequence(nums, sequences, maxLenIdx):
    result = [nums[maxLenIdx]]
    while sequences[maxLenIdx] is not None:
        maxLenIdx = sequences[maxLenIdx]
        result.append(nums[maxLenIdx])
    return list(reversed(result))








