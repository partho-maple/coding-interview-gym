class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = -1
        maxIndex = -1
        for i in range(len(nums)):
            if nums[i] >= maxNum:
                maxNum = nums[i]
                maxIndex = i
        for i in range(len(nums)):
            num2X = nums[i] * 2
            if num2X > maxNum and i != maxIndex:
                return -1
        return maxIndex


sol = Solution()
inputNums = [0,0,2,3]
output = sol.dominantIndex(inputNums)
print('Output: ', output)