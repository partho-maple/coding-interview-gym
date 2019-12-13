class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentIndex, length = 0, len(nums)
        while currentIndex < length:
            currentNum = nums[currentIndex]
            expectedCurrentIndex = currentNum - 1
            if currentNum > 0 and currentNum <= length and currentNum != nums[expectedCurrentIndex]:
                nums[currentIndex], nums[expectedCurrentIndex] = nums[expectedCurrentIndex], nums[currentIndex]
            else:
                currentIndex += 1
        for index in range(length):
            expectedCurrentNum = index + 1
            actualCurrentNum = nums[index]
            if actualCurrentNum != expectedCurrentNum:
                return expectedCurrentNum
        return length + 1