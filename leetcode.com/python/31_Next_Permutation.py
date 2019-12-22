
# Must check this video:    https://tinyurl.com/vfmnqt4
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:                                          # nums are in descending order
            nums.reverse()
            return
        k = i - 1                                           # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        leftIdx, rightIdx = k + 1, len(nums) - 1            # reverse the second part
        while leftIdx < rightIdx:
            nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
            leftIdx += 1
            rightIdx -= 1




