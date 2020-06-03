"""
[1,1,2,3,3,4,4,8,8]
 0       4       8
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numLen = len(nums)
        if numLen == 1:
            return nums[-1]
        left, right = 0, numLen - 1
        while left <= right:
            mid = left + ((right - left) // 2)

            if mid + 1 < numLen and nums[mid] == nums[mid + 1]:
                if (right - mid - 1) % 2 == 1:
                    left = mid + 2
                else:
                    right = mid - 1
            elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                if (mid - left - 1) % 2 == 1:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]

        return nums[left]
