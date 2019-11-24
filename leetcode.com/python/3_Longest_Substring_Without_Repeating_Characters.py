class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        charRecords = {}  # holds the last occarance index of character
        maxSubstringLength = 0
        startIdx = 0
        currentSubstringLength = 0
        for endIdx, currentChar in enumerate(s):
            # the substring begins at 'startIdx', ignore character occurrence before it
            # e.g. In 'abba', when startIdx=2 endIdx=3, position 0 for a is less than 2
            if currentChar in charRecords and charRecords[currentChar] >= startIdx:
                # duplicate char, update max substring
                maxSubstringLength = max(maxSubstringLength, currentSubstringLength)
                # update 'start' position, recalc substring length
                startIdx = charRecords[currentChar] + 1
                # substring length = end index - start index + 1
                currentSubstringLength = endIdx - startIdx + 1
                # substring_length = i - records[char]
            else:
                currentSubstringLength += 1
            # update char occurrence
            charRecords[currentChar] = endIdx

        # in case there's no duplicate, and  max() is never run before
        maxSubstringLength = max(maxSubstringLength, currentSubstringLength)
        return maxSubstringLength


sol = Solution()
s = "abcabcbb"
out = sol.lengthOfLongestSubstring(s)
print("Res: ", out)