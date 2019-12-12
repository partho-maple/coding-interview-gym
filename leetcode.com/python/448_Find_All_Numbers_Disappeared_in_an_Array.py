class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        currentIndex, length = 0, len(nums)
        missingNumbers = []
        while currentIndex < length:
            finalIndex = nums[currentIndex] - 1
            if nums[currentIndex] != nums[finalIndex]:
                nums[currentIndex], nums[finalIndex] = nums[finalIndex], nums[currentIndex]
            else:
                currentIndex += 1
        for index in range(length):     # find the first number missing from its index, that will be our required number
            if nums[index] != index + 1:
                missingNumbers.append(index + 1)
        return missingNumbers