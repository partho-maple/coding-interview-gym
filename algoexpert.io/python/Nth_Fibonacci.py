

# Sodution 1: Recursive solusion
# O(2^n) time | O(n) space
def get_Nth_fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return get_Nth_fibonacci(n - 1) + get_Nth_fibonacci(n - 2)

# Solution 2: using memoization
# O(n) time | O(n) space
# https://www.quora.com/What-is-memoization
def get_Nth_fibonacci(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_Nth_fibonacci(n - 1, memoize) + get_Nth_fibonacci(n - 2, memoize)
        return memoize[n]

# Solution 3: iterative
# O(2^n) time | O(1) space
def get_Nth_fibonacci(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


number_of_fib = 6
print(number_of_fib, "th Fibonacci number is: ", get_Nth_fibonacci(number_of_fib))
