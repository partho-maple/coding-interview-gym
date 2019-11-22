
# # Recursive approach
# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return self.findPeakElementHelper(nums, 0, len(nums) - 1)
#
#     def findPeakElementHelper(self, nums, left, right):
#         if left == right:
#             return left
#         mid = (left + right) // 2
#         if nums[mid] > nums[mid + 1]:
#             return self.findPeakElementHelper(nums, left, mid)
#         else:
#             return self.findPeakElementHelper(nums, mid + 1, right)

# Iterative solution
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
                right =  mid
            else:
                left = mid + 1
        return left

