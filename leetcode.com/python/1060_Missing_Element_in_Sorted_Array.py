# Approach 1: one pass through the input array
# Time: O(n) | Space: O(1)
class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        countOfMissingNumber = 0
        for i in range(1, len(nums)):
            left = nums[i - 1]
            right = nums[i]
            if (left + 1) != right:
                # Number missing
                countOfMissingNumber = right - left - 1
                if countOfMissingNumber >= k:
                    # We have the missing number into this range
                    return left + k
                else:
                    # Update the missing numbers, because our missing number isn't in this range
                    k -= countOfMissingNumber
        return right + k


# Approach 2: Binary search
# Time: O(nlogn) | Space: O(1)
class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        actualLength = len(nums)
        expectedLength = nums[-1] - nums[0] + 1
        missingLength = expectedLength - actualLength
        if missingLength < k:  # missing number iss beyond the array
            return nums[-1] + (k - missingLength)

        leftIdx, rightIdx = 0, len(nums) - 1
        while leftIdx + 1 < rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            currentActualLength = midIdx - leftIdx
            currentExpectedLength = nums[midIdx] - nums[leftIdx]
            currentMissingLength = currentExpectedLength - currentActualLength
            if currentMissingLength < k:
                leftIdx = midIdx
                k -= currentMissingLength
            else:
                rightIdx = midIdx

        return nums[leftIdx] + k





