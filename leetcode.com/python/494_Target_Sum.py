class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        totalSum = sum(nums)

        # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
        if totalSum < S or (S + totalSum) % 2 == 1:
            return 0

        return self.findTargetSumWaysHelper(nums, int((S + totalSum) / 2))


    def findTargetSumWaysHelper(self, nums, S):
        numsLen = len(nums)
        dp = [[0 for _ in range(S + 1)] for _ in range(numsLen)]

        # populate the sum = 0 columns, as we will always have an empty set for zero sum
        for i in range(numsLen):
            dp[i][0] = 1

        # with only one number, we can form a subset only when the required sum is
        # equal to the number
        for s in range(1, S + 1):
            dp[0][s] = 1 if nums[0] == s else 0

        # process all subsets for all sums
        for i in range(1, numsLen):
            for j in range(1, S + 1):
                dp[i][j] = dp[i - 1][j]     # exclude the number
                if S >= nums[i]:            # include the number, if it does not exceed the sum
                    # positive = dp[i][j] + dp[i - 1][j - nums[i]]
                    # negative = dp[i][j] + dp[i - 1][j - nums[i]]

                    positive = j + i
                    negative = j + (-i)
                    dp[i][j] = positive + negative

                    # dp[i][j] = dp[i][j] + dp[i - 1][j - nums[i]]

        # the bottom-right corner will have our answer.
        return dp[numsLen - 1][S]



sol = Solution()
nums = [0,0,0,0,0,0,0,0,1]
S = 1
out = sol.findTargetSumWays(nums, S)
print("Res: ", out)