# Python program for iterative binary search
# https://www.geeksforgeeks.org/binary-search/

import math

def binary_search(input_array, start_index, end_index, target_number):

    while end_index >=1:
        mid = math.floor((end_index - start_index) / 2) + start_index
        if input_array[mid] == target_number:
            return mid
        elif input_array[mid] > target_number:
            end_index = mid - 1
        else:
            start_index = mid + 1

    else:
        return -1


array = [2, 3, 4, 10, 40]
num = 10

result = binary_search(array, 0, len(array) - 1, num)

print("The index of ", num, " is: ", result)