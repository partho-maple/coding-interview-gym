class Solution(object):

    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         n = len(nums)
#         if n == 0:
#             return -1
#         if n == 1:
#             return 0 if nums[0] == target else -1
#         rotatingIdx = self.findRotatingIndex(nums, 0, n - 1)
#         if nums[rotatingIdx] == target:
#             return rotatingIdx
#         if rotatingIdx == 0:
#             return self.binarySearch(nums, target, 0, n - 1)
#         if target >= nums[0]:
#             return self.binarySearch(nums, target, 0, rotatingIdx - 1)
#         else:
#             return self.binarySearch(nums, target, rotatingIdx, n - 1)

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

#     def binarySearch(self, nums, target, left, right):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1



sol = Solution()
nums = [4,5,1,2,3]
target = 1
out = sol.search(nums, target)
print("Res: ", out)