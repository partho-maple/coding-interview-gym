class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = [-1] * len(nums)
        return self.robHelper(nums, len(nums) - 1, cache)

    def robHelper(self, nums, currentHouse, cache):
        if currentHouse < 0:
            return 0
        if cache[currentHouse] >= 0:
            return cache[currentHouse]
        robbedMoney = max(self.robHelper(nums, currentHouse - 2, cache) + nums[currentHouse],
                          self.robHelper(nums, currentHouse - 1, cache))
        cache[currentHouse] = robbedMoney
        return robbedMoney



sol = Solution()
nums = [1,2,3,1]
out = sol.rob(nums)
print("Res: ", out)