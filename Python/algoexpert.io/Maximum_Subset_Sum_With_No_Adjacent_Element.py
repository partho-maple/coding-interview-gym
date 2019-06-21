
# Solution 1
# O(n) time | O(n) space
def max_subset_sum_with_no_adjacent(array):
    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]
    max_sum = array[:]      # copying the array into max_sum
    max_sum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sum[i] = max_sum(max_sum[i - 1], max_sum[i - 2] + array[i])
    return max_sum[-1]      # -1 refers to the last index

# Solution 2
# O(n) time | O(1) space
def max_subset_sum_with_no_adjacent(array):
    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first

