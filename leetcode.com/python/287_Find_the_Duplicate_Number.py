class Solution(object):

    # Cyclic Sort approach, which actually modifies the input array
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentIndex, length = 0, len(nums)
        while currentIndex < length:
            expectedCurrentNum = currentIndex + 1
            actualCurrentNum = nums[currentIndex]
            if actualCurrentNum != expectedCurrentNum:
                finalIndexOfActualCurrentNum = nums[currentIndex] - 1
                if nums[finalIndexOfActualCurrentNum] != nums[currentIndex]:
                    nums[currentIndex], nums[finalIndexOfActualCurrentNum] = nums[finalIndexOfActualCurrentNum], nums[currentIndex]
                else:                   # we have found the duplicate
                    return nums[finalIndexOfActualCurrentNum]
            else:
                currentIndex += 1
        return -1
