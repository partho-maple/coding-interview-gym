def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        shiftDown(0, endIdx - 1, array)
    return array



def buildMaxHeap(array):
    firstParentIndex = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIndex + 1)):
        shiftDown(currentIdx, len(array) - 1, array)



def shiftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            indexToSwap = childTwoIdx
        else:
            indexToSwap = childOneIdx
        if heap[indexToSwap] > heap[currentIdx]:
            swap(currentIdx, indexToSwap, heap)
            currentIdx = indexToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return



def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

