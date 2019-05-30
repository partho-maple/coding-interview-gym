# Solution 1 starts
# def twoNumberSum(array, targetSum):
#     result_list = []
#     for i in range(0, len(array) - 1):
#         first_number = array[i]
#         for j in range(i + 1, len(array)):
#             second_number = array[j]
#             sum = first_number + second_number
#             if sum == targetSum:
#                 result_list.append(first_number)
#                 result_list.append(second_number)
#
#     return sorted(result_list)
# Solution 1 ends

# # Solution 2 starts
# def twoNumberSum(array, targetSum):
#     result_list = []
#     for i in range(0, len(array) - 1):
#         first_number = array[i]
#         second_number_expected = targetSum - first_number
#         secondary_array = array[i + 1:len(array)]
#         if second_number_expected in secondary_array:
#             result_list.append(first_number)
#             result_list.append(second_number_expected)
#
#     return sorted(result_list)
# # Solution 2 ends

# Solution 3 starts
def twoNumberSum(array, targetSum):

    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return [array[left], array[right]]
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1

    return []
# Solution 3 ends


print(twoNumberSum([5, 3, -4, 8, 11, 1, -1, 6], 10))
