# # Simple recursive approach.    Time Limit Exceeded
# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         return self.isInterleaveHelper(s1, s2, s3, 0, 0, 0)
#
#
#     def isInterleaveHelper(self, s1, s2, s3, s1Idx, s2Idx, s3Idx):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         s1Len, s2Len, s3Len = len(s1), len(s2), len(s3)
#
#         # if we have reached the end of the all the strings,  because we have consumed all the string and the string in interleaving
#         if s1Idx == s1Len and s2Idx == s2Len and s3Idx == s3Len:
#             return True
#
#         # if we have reached the end of 'p' but 'm' or 'n' still has some characters left
#         if s3Idx == s3Len:
#             return False
#
#         c1, c2 = False, False
#         if s1Idx < s1Len and s1[s1Idx] == s3[s3Idx]:
#             c1 = self.isInterleaveHelper(s1, s2, s3, s1Idx + 1, s2Idx, s3Idx + 1)
#
#         if s2Idx < s2Len and s2[s2Idx] == s3[s3Idx]:
#             c2 = self.isInterleaveHelper(s1, s2, s3, s1Idx, s2Idx + 1, s3Idx + 1)
#
#         return c1 or c2




class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1Len, s2Len, s3Len = len(s1), len(s2), len(s3)
        # dp[mIndex][nIndex] will be storing the result of string interleaving
        # up to p[0..mIndex+nIndex-1]
        dp = [[False for _ in range(s2Len + 1)] for _ in range(s1Len + 1)]

        # for the empty pattern, we have one matching
        if s1Len + s2Len != s3Len:
            return False

        for s1Index in range(s1Len + 1):
            for s2Index in range(s2Len + 1):
                # if 'm' and 'n' are empty, then 'p' must have been empty too.
                if s1Index == 0 and s2Index == 0:
                    dp[s1Index][s2Index] = True
                # if 'm' is empty, we need to check the interleaving with 'n' only
                elif s1Index == 0 and s2[s2Index - 1] == s3[s1Index + s2Index - 1]:
                    dp[s1Index][s2Index] = dp[s1Index][s2Index - 1]
                # if 'n' is empty, we need to check the interleaving with 'm' only
                elif s2Index == 0 and s1[s1Index - 1] == s3[s1Index + s2Index - 1]:
                    dp[s1Index][s2Index] = dp[s1Index - 1][s2Index]
                else:
                    # if the letter of 'm' and 'p' match, we take whatever is matched till mIndex-1
                    if s1Index > 0 and s1[s1Index - 1] == s3[s1Index + s2Index - 1]:
                        dp[s1Index][s2Index] = dp[s1Index - 1][s2Index]
                    # if the letter of 'n' and 'p' match, we take whatever is matched till nIndex-1 too
                    # note the '|=', this is required when we have common letters
                    if s2Index > 0 and s2[s2Index - 1] == s3[s1Index + s2Index - 1]:
                        dp[s1Index][s2Index] |= dp[s1Index][s2Index - 1]

        return dp[s1Len][s2Len]
