class Solution(object):
    def threeSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # To avoid duplicate number
                continue
            left, right = i + 1, len(nums) - 1
            targetNum = target - nums[i]
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum == targetNum:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: # To avoid duplicate number
                        left += 1
                    while left < right and nums[right] == nums[right - 1]: # To avoid duplicate number
                        right -= 1
                    left += 1;
                    right -= 1
                elif currentSum < targetNum:
                    left += 1
                else:
                    right -= 1
        return results

    def fourSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]: # To avoid duplicate number
                threeResult = self.threeSum(nums[i + 1:], target - nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results
