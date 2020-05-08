# # plain and simle recursion without memo
# # 31 / 39 test cases passed.
# # TLE
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         wordSet = set(wordDict)
#         allSequece = []
#         self.wordreakHelperDFS(s, wordSet, 0, [], allSequece)
#         return allSequece

#     def wordreakHelperDFS(self, s, wordSet, srtIdx, currSqn, allSqn):
#         if srtIdx >= len(s):
#             allSqn.append(" ".join(currSqn))
#             return

#         for i in range(srtIdx, len(s)):
#             currentWord = s[srtIdx:i + 1]
#             if currentWord in wordSet:
#                 currSqn.append(currentWord)
#                 self.wordreakHelperDFS(s, wordSet, i + 1, currSqn, allSqn)
#                 currSqn.pop()


# # plain and simle recursion with memo
# # 27 / 39 test cases passed.
# # Getting wrong answer at 28th test case
# from collections import defaultdict
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         wordSet = set(wordDict)
#         allSequece = []
#         memo = {}
#         self.wordreakHelperDFS(s, wordSet, 0, [], allSequece, memo)
#         return allSequece

#     def wordreakHelperDFS(self, s, wordSet, srtIdx, currSqn, allSqn, memo):
#         if srtIdx >= len(s):
#             allSqn.append(" ".join(currSqn))
#             return

#         if s[srtIdx:] in memo:
#             currSqn.append(memo[s[srtIdx:]])
#             allSqn.append(" ".join(currSqn))
#             return

#         for i in range(srtIdx, len(s)):
#             currentWord = s[srtIdx:i + 1]
#             if currentWord in wordSet:
#                 currSqnLen = len(currSqn)
#                 currSqn.append(currentWord)

#                 self.wordreakHelperDFS(s, wordSet, i + 1, currSqn, allSqn, memo)

#                 resultOfTheRest = list(currSqn[currSqnLen:])
#                 memo[s[srtIdx:]] = " ".join(resultOfTheRest)
#                 for j in range(currSqnLen, len(currSqn)):
#                     currSqn.pop()


# https://tinyurl.com/yc9jvbpl
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.wordreakHelperDFS(s, wordDict, {})

    def wordreakHelperDFS(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.wordreakHelperDFS(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res




