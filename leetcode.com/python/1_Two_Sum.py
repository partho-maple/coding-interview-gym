# https://www.algoexpert.io/questions/Two%20Number%20Sum

class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        numIdxDict = {}
        for idx, num in enumerate(nums):
            numIdxDict[num] = idx
        for idx, num in enumerate(nums):
            expectedNum = target - num
            if expectedNum in numIdxDict:
                if idx != numIdxDict[expectedNum]:
                    indices.extend([idx, numIdxDict[expectedNum]])
                    break
        return sorted(indices)


sol = Solution()
# nums = [2, 7, 11, 15]
# target = 9
nums = [3,2,4]
target = 6
out = sol.twoSum(nums, target)
print("Res: ", out)
