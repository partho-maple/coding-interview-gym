from collections import Counter

# Source: https://tinyurl.com/wzdp4yp
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for right in range(len(p) - 1, len(s)):
            sCounter[s[right]] += 1                             # include a new char in the window
            if sCounter == pCounter:                            # This step is O(1), since there are at most 26 English letters
                result.append(right - len(p) + 1)               # append the starting index
            sCounter[s[right - len(p) + 1]] -= 1                # decrease the count of oldest char in the window
            if sCounter[s[right - len(p) + 1]] == 0:
                del sCounter[s[right - len(p) + 1]]             # remove the count if it is 0
        return result

