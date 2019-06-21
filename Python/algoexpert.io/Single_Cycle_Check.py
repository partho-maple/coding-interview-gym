# https://www.algoexpert.io/questions/Single%20Cycle%20Check


# O(n) time | O(1) space - where n is the length of the input array
def has_single_cycle(array):
    number_of_elements_visited = 0
    current_index = 0
    while number_of_elements_visited < len(array):
        if number_of_elements_visited > 0 and current_index == 0:
            return False
        number_of_elements_visited += 1
        current_index = get_next_index(current_index, array)
    return current_index == 0


def get_next_index(current_index, array):
    jump = array[current_index]
    next_index = (current_index + jump) % len(array)
    return next_index if next_index >= 0 else next_index + len(array)


input_array = [2, -1, 1, 2, 2]
print("Is Single Cycle: ", has_single_cycle(input_array))

