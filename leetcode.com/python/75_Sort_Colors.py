class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, high = 0, len(nums) - 1
        iteratorIdx = 0
        while iteratorIdx <= high:
            if nums[iteratorIdx] == 0:
                nums[iteratorIdx], nums[low] = nums[low], nums[iteratorIdx]
                iteratorIdx += 1
                low += 1
            elif nums[iteratorIdx] == 2:
                nums[iteratorIdx], nums[high] = nums[high], nums[iteratorIdx]
                high -= 1
            else:
                iteratorIdx += 1
        return nums
