class Solution(object):

    # # Backtracking Approach - TLE
    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     return self.canJumpHelper(nums, 0)
    #
    # def canJumpHelper(self, nums, currentIdx):
    #     if currentIdx == len(nums) - 1:
    #         return True
    #     nextMaxJumpIdx = min(currentIdx + nums[currentIdx], len(nums) - 1)
    #     for i in range(nextMaxJumpIdx, currentIdx,
    #                    -1):  # Python for loop decrementing index >> https://stackoverflow.com/questions/28650128/python-for-loop-decrementing-index/28650284
    #         if self.canJumpHelper(nums, i):
    #             return True
    #     return False
    #
    # # DP top-down with memoization Approach - TLE
    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     memo = [0] * len(nums)
    #     memo[-1] = True  # Here True means reachable and True means not rechable
    #     return self.canJumpHelper(nums, 0, memo)
    #
    # def canJumpHelper(self, nums, currentIdx, memo):
    #     if memo[currentIdx] != 0:
    #         return memo[currentIdx]
    #     nextMaxJumpIdx = min(currentIdx + nums[currentIdx], len(nums) - 1)
    #     for i in range(nextMaxJumpIdx, currentIdx, -1):
    #         if self.canJumpHelper(nums, i, memo):
    #             memo[currentIdx] = True
    #             return True
    #     memo[currentIdx] = False
    #     return False
    #
    # # DP bottom-up with memoization Approach - TLE
    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     memo = [0] * len(nums)
    #     memo[-1] = True  # Here True means reachable and True means not rechable
    #     for i in range(len(nums) - 1, -1, -1):
    #         nextMaxJumpIdx = min(i + nums[i], len(nums) - 1)
    #         for j in range(i + 1, nextMaxJumpIdx + 1):
    #             if memo[j] is True:
    #                 memo[i] = True
    #                 break
    #     return True if memo[0] == True else False

    # Greedy
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPosition = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            nextMaxJump = i + nums[i]
            if nextMaxJump >= lastPosition:
                lastPosition = i
        return True if lastPosition == 0 else False


sol = Solution()
# input = [2,3,0,1,4]
input = [3,2,1,0,4]
# input = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
output = sol.canJump(input)
print('res: ', output)