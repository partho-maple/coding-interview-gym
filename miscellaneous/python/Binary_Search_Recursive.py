# Python program forrecursive binary search
# https://www.geeksforgeeks.org/binary-search/

import math

# Recursive solution
# O(log(n)) time | O(log(n)) space
def binary_search(input_array, start_index, end_index, target_number):

    if end_index >= 1:
        mid = math.floor((end_index - start_index) / 2) + start_index
        if input_array[mid] == target_number:
            return mid
        elif input_array[mid] > target_number:
            return binary_search(input_array, 1, mid - 1, target_number)
        else:
            return binary_search(input_array, mid + 1, end_index, target_number)

    else:
        return -1


array = [2, 3, 4, 10, 40]
num = 4

result = binary_search(array, 0, len(array) - 1, num)

print("The inxex of ", num, " is: ", result)