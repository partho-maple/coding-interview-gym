
#   Approach 1: Typical DP
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        length = [1 for _ in nums]
        for i in range(len(nums)):
            currentNum = nums[i]
            for j in range(0, i):
                otherNum = nums[j]
                if otherNum < currentNum and length[j] + 1 >= length[i]:
                    length[i] = length[j] + 1
        return max(length)



#   Approach 2: DP with Binary Search
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """




sol = Solution()
nums = [10,9,2,5,3,7,101,18]
ourput = sol.lengthOfLIS(nums)
print('Res: ', ourput)

