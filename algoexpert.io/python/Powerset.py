# Solution 1 - Recursive
# O(n*2^n) time | O(n*2^n) space
def power_set(array, index = None):
    if index is None:
        index  = len(array) - 1
    if index < 0:
        return [[]]
    ele = array[index]
    subset = power_set(array, index - 1)
    for i in range(len(subset)):
        current_subset = subset[i]
        subset.append(current_subset + [ele])
    return subset


# Solution 2 - Iterative
# O(n*2^n) time | O(n*2^n) space
def power_set(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [ele])
    return subsets


