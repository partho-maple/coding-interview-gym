# https://www.algoexpert.io/questions/Kadane's%20Algorithm


# O(n) time | O(1) space - where n is the length of the   input array
def kadanes_algorithm(array):
    max_ending_here = array[0]
    max_so_far = array[0]
    for i in range(1, len(array)):
        num = array[i]
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

