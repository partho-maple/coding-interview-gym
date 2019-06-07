# https://www.algoexpert.io/questions/Selection%20Sort


# Best: O(n^2) time | O(1) space
# Avarage: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selection_sort(input_array):
    current_index = 0
    while current_index < len(input_array) - 1:
        smallest_index = current_index
        for i in range(current_index + 1, len(input_array)):
            if input_array[i] < input_array[current_index]:
                smallest_index = i
            swap(current_index, smallest_index, input_array)
            current_index += 1
    return input_array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

