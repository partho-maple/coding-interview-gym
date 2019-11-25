class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        startIdx, endIdx, maxSubStrLen, maxCountOfMostCommonCharInWindow = 0, 0, 0 ,0
        charFrequencyCountIntoWindow = [0 for _ in range(26)]
        while endIdx < len(s):
            currentCharIdx = ord(s[endIdx]) - ord('A')
            charFrequencyCountIntoWindow[currentCharIdx] += 1
            maxCountOfMostCommonCharInWindow = max(maxCountOfMostCommonCharInWindow, charFrequencyCountIntoWindow[currentCharIdx])
            slidingWindowLenght = endIdx - startIdx + 1
            numOfReplacement = slidingWindowLenght - maxCountOfMostCommonCharInWindow
            while numOfReplacement > k:
                idxOfStartingWindowCharIntoCharFrequenctArray = ord(s[startIdx]) - ord('A')
                charFrequencyCountIntoWindow[idxOfStartingWindowCharIntoCharFrequenctArray] -= 1
                startIdx += 1
                slidingWindowLenght = endIdx - startIdx + 1
                numOfReplacement = slidingWindowLenght - maxCountOfMostCommonCharInWindow
            maxSubStrLen = max(maxSubStrLen, slidingWindowLenght)
            endIdx += 1
        return maxSubStrLen




sol = Solution()
s = "AABABBA"
k = 1
out = sol.characterReplacement(s, k)
print("Res: ", out)