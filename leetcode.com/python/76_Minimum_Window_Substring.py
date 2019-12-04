from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)                                                                   # hash table to store char frequency
        missing = len(t)                                                                    # total number of chars we care
        left, minWindowStart, minWindowEnd = 0, 0, 0
        for right, char in enumerate(s, 1):                                                 # right pointer startes at second character of 's'
            if need[char] > 0:                                                              # char is in 't'
                missing -= 1
            need[char] -= 1
            if missing == 0:                                                                # condition to shrink window, which means it's the time to advance left. Because all target char currently is in current window
                while left < right and need[s[left]] < 0:                                   # remove chars to find the real start
                    need[s[left]] += 1
                    left += 1
                if minWindowEnd == 0 or (right - left <= minWindowEnd - minWindowStart):    #update window
                    minWindowStart, minWindowEnd = left, right
        return "" if missing > 0 else s[minWindowStart:minWindowEnd]



sol = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"
s = "ab"
t = "a"
out = sol.minWindow(s, t)
print("Res: ", out)