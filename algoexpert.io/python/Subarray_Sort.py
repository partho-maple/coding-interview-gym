import math

def subarraySort(array):
    minOutOfOrder = math.inf
    maxOutOfOrder = -math.inf
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == math.inf:
        return [-1, -1]
    subArrayLeftIdx = 0
    while array[subArrayLeftIdx] <= minOutOfOrder:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayLeftIdx, subArrayRightIdx]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num < array[i - 1] or num > array[i + 1]
