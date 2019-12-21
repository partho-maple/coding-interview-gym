# Source: https://tinyurl.com/wfkx3jt
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        totalSubsets = []
        totalSubsets.append([])
        startIndex, endIndex = 0, 0
        for idx in range(len(nums)):
            startIndex = 0
            if idx > 0 and nums[idx] == nums[idx - 1]:
                startIndex = endIndex + 1
            endIndex = len(totalSubsets) - 1
            for j in range(startIndex, endIndex + 1):
                newSubset = list(totalSubsets[j])
                newSubset.append(nums[idx])
                totalSubsets.append(newSubset)
        return totalSubsets
