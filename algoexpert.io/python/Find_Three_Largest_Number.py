# My solution using Hepa
import heapq
def findThreeLargestNumbers(array):
    hp = []
	for num in array:
		if len(hp) < 3:
			heapq.heappush(hp, num)
		else:
			if hp[0] < num:
				heapq.heappop(hp)
				heapq.heappush(hp, num)
	return sorted(hp)

# Solution providd by Algoexpert
# O(n) time | O(1) space
def find_three_largest_number(array):
    three_largest_number = [None, None, None]
    for num in array:
        update_largest(num, three_largest_number)
    return three_largest_number


def update_largest(number, three_largest_number):
    if three_largest_number[2] is None or number > three_largest_number[2]:
        shift_and_update(three_largest_number, number, 2)
    elif three_largest_number[1] is None or number > three_largest_number[1]:
        shift_and_update(three_largest_number, number, 1)
    elif three_largest_number[0] is None or number > three_largest_number[0]:
        shift_and_update(three_largest_number, number, 0)


def shift_and_update(three_largest_number, number, index):
    for i in range(index + 1):
        if i == index:
            three_largest_number[index] = number
        else:
            three_largest_number[i] = three_largest_number[i + 1]


given_numbers = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
largest_numbers = find_three_largest_number(given_numbers)
print("Largest numbers are: ", largest_numbers)


