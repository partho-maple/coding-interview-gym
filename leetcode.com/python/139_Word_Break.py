# Approach 1: Brute Force, Backtracking - TLE
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        canSegment = False
        for word in wordDict:
            if s.startswith(word):
                newS = s[len(word):]
                canSegment = self.wordBreak(newS, wordDict)
                if canSegment:
                    break
        return canSegment


# Approach 2: Brute Force, Backtracking with memoization - TLE
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.wordBreakHelper(s, 0, set(wordDict), [False]*len(s))

    def wordBreakHelper(self, s, start, wordSet, memo):
        if start == len(s):
            return True
        if memo[start]:
            return True
        for end in range(start + 1, len(s)):
            if s[start:end] in wordSet and self.wordBreakHelper(s, end, wordSet, memo):
                memo[start] = True
                return memo[start]
            else:
                memo[start] = False
        return memo[start]




# Approach 3: DP
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if word == s[i - len(word):i] and dp[i - len(word)]:
                    dp[i] = True
        return dp[-1]

