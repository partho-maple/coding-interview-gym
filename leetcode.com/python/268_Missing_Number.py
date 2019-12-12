
# Bit-Manipulation approach
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing





# Cyclic-Sort approach
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentIndex, length = 0, len(nums)
        while currentIndex < length:
            finalIndex = nums[currentIndex]
            if nums[currentIndex] < length and nums[currentIndex] != nums[finalIndex]:
                nums[currentIndex], nums[finalIndex] = nums[finalIndex], nums[currentIndex]
            else:
                currentIndex += 1
        for index in range(length):     # find the first number missing from its index, that will be our required number
            if nums[index] != index:
                return index
        return length

