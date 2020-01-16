from collections import defaultdict
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) <= 1:
            return 1
        dp = defaultdict(int)
        words = sorted(words, key=len)
        for word in words:
            for i in range(len(word)):
                possiblePredecessor = word[:i] + word[i + 1:]
                dp[word] = max(dp[possiblePredecessor] + 1, dp[word])
        return max(dp.values())