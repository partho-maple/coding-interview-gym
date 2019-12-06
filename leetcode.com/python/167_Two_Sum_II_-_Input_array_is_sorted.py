class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftIdx, rightIdx = 0, len(numbers) - 1
        while leftIdx < rightIdx:
            twoSum = numbers[leftIdx] + numbers[rightIdx]
            if twoSum == target:
                break
            elif twoSum < target:
                leftIdx += 1
            else:
                rightIdx -= 1
        return [leftIdx + 1, rightIdx + 1]

