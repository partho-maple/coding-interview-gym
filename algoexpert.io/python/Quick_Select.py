


def quickSelect(array, k):
    position = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, position)


def quickSelectHelper(array, startIndex, endIndex, position):
    while True:
        if startIndex > endIndex:
            raise Exception('Algorithm should never arrive here!')
        pivotIndex = startIndex
        leftIndex = startIndex + 1
        rightIndex = endIndex
        while leftIndex <= rightIndex:
            if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
                swap(leftIndex, rightIndex, array)
            if array[leftIndex] <= array[pivotIndex]:
                leftIndex += 1
            if array[rightIndex] >= array[pivotIndex]:
                rightIndex -= 1
        swap(pivotIndex, rightIndex, array)
        if rightIndex == position:
            return array[rightIndex]
        elif rightIndex < position:
            startIndex = rightIndex + 1
        else:
            endIndex = rightIndex - 1


def swap(one, two, array):
    array[one], array[two] = array[two], array[one]