
# Best: O(n) time | O(1) space
# Avarage: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubblesort(input_array):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(input_array) - 1 - counter):
            if input_array[i] > input_array[i + 1]:
                swap(i, i + 1, input_array)
                is_sorted = False
            counter += 1
    return input_array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


