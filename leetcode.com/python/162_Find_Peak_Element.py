# Recursive Approach
# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return self.findPeakElementHelper(nums, 0, len(nums) - 1)

#     def findPeakElementHelper(self, nums, left, right):
#         if left == right:
#             return left
#         mid = (left + right) // 2
#         if nums[mid] > nums[mid + 1]:
#             return self.findPeakElementHelper(nums, left, mid)
#         else:
#             return self.findPeakElementHelper(nums, mid + 1, right)


# Time: O(log n) uses Binary search
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


# Solution. during Mock test
# Time: O(n) uses Linear search
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak = 0
        if len(nums) <= 0:
            return peak
        for i in range(1, len(nums)):
            if nums[i] > nums[peak]:
                peak = i
        return peak
