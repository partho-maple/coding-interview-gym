

# Solution 1
# O(n^2) time | O(n) space
def is_palindrome(string):
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return string == reversed_string


# Solution 2
# O(n) time | O(n) space
def is_palindrome(string):
    reversed_chars = []
    for i in reversed(range(len(string))):
        reversed_chars.append(string[i])
    return string == "".join(reversed_chars)


# Solution 3. A tail-recursive solution
# O(n) time | O(n) space
def is_palindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= i else string[i] == string[j] and is_palindrome(string, i + 1)


# Solution 4
# O(n) time | O(1) space
def is_palindrome(string):
    left_index = 0
    right_index = len(string) - 1
    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


