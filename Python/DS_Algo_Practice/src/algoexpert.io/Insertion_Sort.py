


# Best: O(n) time | O(1) space
# Avarage: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insersion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


input_array = [8, 5, 2, 9, 5, 6, 3]
sorted_array = insersion_sort(input_array)
print("Sorted Array: ", sorted_array)