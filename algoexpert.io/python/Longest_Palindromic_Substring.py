# Algoexpert Provided Solution 1
# O(n^3) time | O(1) space
def longest_palindromic_substring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if len(substring) > len(longest) and is_palindrome(substring):
                longest = substring
    return longest


def is_palindrome(string):
    left_index = 0
    right_index = len(string) - 1
    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


# Algoexpert Provided Solution 2 - prefered solution
# O(n^2) time | O(1) space
def longest_palindromic_substring(string):
    current_longest = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_pelindrome_from(string, i - 1, i + 1)
        even = get_longest_pelindrome_from(string, i - 1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key = lambda x: x[1] - x[0])
    return string[current_longest[0]:current_longest[1] + 1]


def get_longest_pelindrome_from(string, left_index, right_index):
    while left_index >= 0 and right_index < len(string):
        if string[left_index] != string[right_index]:
            break
        left_index -= 1
        right_index += 1
    return [left_index + 1, right_index - 1]


# My solution - using 2d dp - preferd solution
def longestPalindromicSubstring(string):
    L = len(string)
    if L <= 1:
        return string

    dp = [[None for _ in range(L)] for _ in range(L)]

    # Populating diagonal line
    for i in range(L):
        dp[i][i] = string[i]

    maxPalStr = ""
    for startIdx in range(L - 1, -1, -1):
        for endIdx in range(startIdx + 1, L):
            if string[startIdx] == string[endIdx]:
                if endIdx - startIdx == 1 or dp[startIdx + 1][endIdx - 1]:
                    dp[startIdx][endIdx] = string[startIdx:endIdx + 1]
                    maxPalStr = max(maxPalStr, dp[startIdx][endIdx], key=len)
    return maxPalStr

strig = "abcdefghfedcbaa"
out = longestPalindromicSubstring(strig)
print("Out: ", out)