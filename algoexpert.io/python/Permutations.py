# Solution 1
# Upper Bound: O(n^2*n) time | O(n*n!) space
# Roughly: O(n*n!)  time | O(n*n!) space
def ge_permutation(array):
    permutations = []
    permutation_helper(array, [], permutations)
    return permutations


def permutation_helper(remaining_input_array, current_permutation, total_permutations):
    if not len(remaining_input_array) and len(current_permutation):
        total_permutations.append(current_permutation)
    else:
        for i in range(len(remaining_input_array)):
            new_array = remaining_input_array[:i] + remaining_input_array[i + 1:]
            new_permutation = current_permutation + [remaining_input_array[i]]
            permutation_helper(new_array, new_permutation, total_permutations)


# Solution 2
# O(n*n!)  time | O(n*n!) space
def ge_permutation(array):
    permutations = []
    permutation_helper(0, array, permutations)
    return permutations


def permutation_helper(i, array, total_permutations):
    if i == len(array) - 1:
        total_permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutation_helper(i + 1, array, total_permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# -----------------------


# My solution
def getPermutations(array):
	if len(array) <= 0:
		return []
    result = []
	permutationHelper(array, 0, [], result)
	return result

def permutationHelper(nums, currentNumIdx, currentPermutation, result):
	if currentNumIdx == len(nums):
		result.append(currentPermutation)
	else:
		for i in range(len(currentPermutation) + 1):  # create a new permutation by adding the current number at every position
			newPerm = list(currentPermutation)
			newPerm.insert(i, nums[currentNumIdx])
			permutationHelper(nums, currentNumIdx + 1, newPerm, result)




