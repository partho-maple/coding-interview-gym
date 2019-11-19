# Iterative + 2 variables (bottom-up)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The following 3 conditions are edge/special cases
        if len(nums) <= 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        include_1st_house = self.robHelper(nums, 0, len(nums) - 2)
        exclude_1st_house = self.robHelper(nums, 1, len(nums) - 1)
        return max(include_1st_house, exclude_1st_house)

    def robHelper(self, nums, leftHouseNumber, rightHouseHumber):
        previousRobbedMoney, currentRobbedMoney = 0, 0
        for i in range(leftHouseNumber, rightHouseHumber + 1):
            currentRobbedMoneyHolder = currentRobbedMoney
            currentRobbedMoney = max(nums[i] + previousRobbedMoney, currentRobbedMoney)
            previousRobbedMoney = currentRobbedMoneyHolder
        return currentRobbedMoney





sol = Solution()
nums = [1,2,3,1]
out = sol.rob(nums)
print("Res: ", out)