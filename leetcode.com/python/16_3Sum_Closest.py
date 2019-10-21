class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        triplate = []
        prevSum = float("-inf")
        prevDiff = target - prevSum
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                currentDiff = target - currentSum
                prevDiff = target - prevSum
                if abs(currentDiff) < abs(prevDiff):
                    triplate = [nums[i], nums[left], nums[right]]
                    prevDiff = currentDiff
                    prevSum = currentSum
                if currentSum < target:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif currentSum > target:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    return sum(triplate[:])
        return sum(triplate[:])



sol = Solution()
input = [1,1,1,0]
target = -100
tripletsSum = sol.threeSumClosest(input, target)
print("Result: ", tripletsSum)
