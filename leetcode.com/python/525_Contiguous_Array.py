# https://tinyurl.com/qmbd2vl
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, maxLenSoFar = 0, 0
        counterMap = {count: -1}  # count:index,

        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum == 0:
                count -= 1
            else:
                count += 1

            if count in counterMap:
                maxLenSoFar = max(maxLenSoFar, i - counterMap[count])
            else:
                counterMap[count] = i

        return maxLenSoFar
