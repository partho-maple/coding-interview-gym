# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n == 0:
#             return -1
#         if n == 1:
#             return nums[0]
#         rotatingIdx = self.findRotatingIndex(nums, 0, n - 1)
#         return nums[rotatingIdx]
#
#     def findRotatingIndex(self, nums, left, right):
#         if nums[left] < nums[right]:  # nums is not rotated, it's already sorted
#             return 0
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[mid + 1]:  # we have found our rotating index
#                 return mid + 1
#             elif (nums[mid] < nums[mid + 1]) and (nums[mid] < nums[mid - 1]):  # we have found our rotating index
#                 return mid
#             else:
#                 if nums[mid] > nums[left]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
