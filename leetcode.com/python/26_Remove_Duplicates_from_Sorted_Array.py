class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        left, right = 0, 1
        while left < right and right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(left)
            else:
                left += 1
                right += 1
        return len(nums)

