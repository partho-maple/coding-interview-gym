class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        currentIndex, length = 0, len(nums)
        duplicateNums = []
        while currentIndex < length:
            currentNum = nums[currentIndex]
            expectedCurrentIndex = currentNum - 1
            if nums[currentIndex] != nums[expectedCurrentIndex]:
                nums[currentIndex], nums[expectedCurrentIndex] = nums[expectedCurrentIndex], nums[currentIndex]
            else:
                currentIndex += 1
        for index in range(length):
            expectedCurrentNum = index + 1
            actualCurrentNum = nums[index]
            if actualCurrentNum != expectedCurrentNum:
                duplicateNums.append(nums[index])
        return duplicateNums