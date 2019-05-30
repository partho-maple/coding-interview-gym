

# Print element of an array, using tail recursion
# def print_array(arr, len):
#     if len == 0:
#         return
#     else:
#         print(arr[len-1], " ")
#         len -= 1
#         print_array(arr, len)
#
#
# input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_array(input_array, 9)


# Using basic recursion
# def a_raised_to_the_power_of_b(a, b):
#     if b <= 1:
#         return a
#     else:
#         return a*a_raised_to_the_power_of_b(a, (b-1))


# Using tail recursion
def a_raised_to_the_power_of_b(a, b, res):
    if b <= 1:
        return a*res
    else:
        new_res = res*a
        return a_raised_to_the_power_of_b(a, (b-1), new_res)


base = 2
pow = 4
print(base, "rais to the power of ", pow, "is: ", a_raised_to_the_power_of_b(base, pow, 1))


