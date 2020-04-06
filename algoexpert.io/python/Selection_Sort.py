# https://www.algoexpert.io/questions/Selection%20Sort


# Best: O(n^2) time | O(1) space
# Avarage: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):
    current_index = 0
    while current_index < len(array) - 1:
        smallest_index = current_index
        for i in range(current_index + 1, len(array)):
            if array[i] < array[smallest_index]:
                smallest_index = i
        swap(current_index, smallest_index, array)
        current_index += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

