
#   Solution 1
#   O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for i in array]
    lengths = [1 for i in array]
    maxLengthIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i
    return buildSequence(array, sequences, maxLengthIdx)


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequences.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))




