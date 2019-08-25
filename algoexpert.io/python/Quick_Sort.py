

# Best:     O(nlog(n))  time  |    O(log(n))  space
# Average:  O(nlog(n))  time  |    O(log(n))  space
# Worst:    O(n^2)  time      |    O(log(n))  space

def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIndex, endIndex):
    if startIndex >= endIndex:
        return
    pivotIndex = startIndex
    leftIndex = startIndex + 1
    rightIndex = endIndex
    while rightIndex >= leftIndex:
        if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
            array[leftIndex], array[rightIndex] = array[rightIndex], array[leftIndex]
        if array[leftIndex] <= array[pivotIndex]:
            leftIndex += 1
        if array[rightIndex] >= array[pivotIndex]:
            rightIndex -= 1
    array[rightIndex], array[pivotIndex] = array[pivotIndex],  array[rightIndex]
    leftSubArrayIsSmaller = rightIndex - 1 - startIndex < endIndex - (rightIndex + 1)
    if leftSubArrayIsSmaller:
        quickSortHelper(array, startIndex, rightIndex - 1)
        quickSortHelper(array, rightIndex + 1, endIndex)
    else:
        quickSortHelper(array, rightIndex + 1, endIndex)
        quickSortHelper(array, startIndex, rightIndex - 1)




