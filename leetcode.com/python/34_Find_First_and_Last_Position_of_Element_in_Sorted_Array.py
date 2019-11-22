# # Iterative  approach. O(n) time worst case
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         left, right = 0, len(nums) - 1
#         startIdx, endIdx = -1, -1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:  # we have found our first match, now perform BS to it's left and right to find the range
#                 startIdx, endIdx = mid, mid
#                 while startIdx >= 0 and startIdx <= len(nums) - 1 and nums[startIdx] == target:
#                     startIdx -= 1
#                 while endIdx >= 0 and endIdx <= len(nums) - 1 and nums[endIdx] == target:
#                     endIdx += 1
#                 return [startIdx + 1, endIdx - 1]
#         return [startIdx, endIdx]




# Iterative  approach. O(log n) time at worst case
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        startIdx, endIdx = -1, -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # we have found our first match, now perform BS to it's left and right to find the range
                startIdx, endIdx = mid, mid
                while startIdx > left:
                    leftMid = (left + startIdx) // 2
                    if nums[leftMid] < target:
                        left = leftMid + 1
                    else:
                        startIdx = leftMid
                while endIdx + 1 <= right:
                    rightMid = (right + endIdx + 1) // 2
                    if nums[rightMid] > target:
                        right = rightMid - 1
                    else:
                        endIdx = rightMid
                return [startIdx, endIdx]
        return [startIdx, endIdx]



sol = Solution()
nums = [0,0,0,8,8,10]
target = 0
out = sol.searchRange(nums, target)
print("Res: ", out)