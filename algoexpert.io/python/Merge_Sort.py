

#   Solution  1
#   O(nlogn) time  |  O(nlogn) space
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf  = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArrays(leftHalf, rightHalf):
    sortedArrays = [None] * (len(leftHalf) + len(rightHalf))
    sortedArrayPtr = leftArrayPtr = rightArrayPtr = 0
    while leftArrayPtr < len(leftHalf) and rightArrayPtr < len(rightHalf):
        if leftHalf[leftArrayPtr] < rightHalf[rightArrayPtr]:
            sortedArrays[sortedArrayPtr] = leftHalf[leftArrayPtr]
            leftArrayPtr += 1
        else:
            sortedArrays[sortedArrayPtr] = rightHalf[rightArrayPtr]
            rightArrayPtr += 1
        sortedArrayPtr += 1
    while leftArrayPtr  < len(leftHalf):
        sortedArrays[sortedArrayPtr] = leftHalf[leftArrayPtr]
        sortedArrayPtr += 1
        leftArrayPtr += 1
    while rightArrayPtr < len(rightHalf):
        sortedArrays[sortedArrayPtr] = rightHalf[rightArrayPtr]
        sortedArrayPtr +=  1
        rightArrayPtr +=  1
    return sortedArrays








