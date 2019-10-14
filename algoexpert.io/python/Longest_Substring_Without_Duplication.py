
# O(n) time  |  O(min(n, a))  space
def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1] # Here 0 and 1 is the values in the 0 and 1 index. This variable stores the start and end index of of the longest string.
    startIndex = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIndex = max(startIndex, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIndex: # Here 0 and 1 is the index of the value of longest array
            longest = [startIndex, i + 1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]



