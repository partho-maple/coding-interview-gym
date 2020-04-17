class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nLen = len(nums) - 1
        nums.sort()
        fidx = nLen // 2
        sidx = nLen // 2 + 1

        swapIdx = 0
        while swapIdx < nLen - 1:
            nums[swapIdx], nums[fidx] = nums[fidx], nums[swapIdx]
            swapIdx += 1
            fidx += 1

            nums[swapIdx], nums[sidx] = nums[sidx], nums[swapIdx]
            swapIdx += 1
            sidx += 1
