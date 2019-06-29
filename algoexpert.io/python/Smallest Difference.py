# https://www.algoexpert.io/questions/Smallest%20Difference

# O(nlog(n) + mlon(m)) time | O(1) space
def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    result_pair = []
    index_one = 0
    index_two = 0
    smallest = float("inf")
    current = float("inf")
    while index_one < len(array_one) and index_two < len(array_two):
        first_num = array_one[index_one]
        second_num = array_two[index_two]
        if first_num < second_num:
            current = second_num - first_num
            index_one += 1
        elif second_num < first_num:
            current = first_num - second_num
            index_two += 1
        else:
            return [first_num, second_num]

        if smallest > current:
            smallest = current
            result_pair = [first_num, second_num]
    return result_pair
    

