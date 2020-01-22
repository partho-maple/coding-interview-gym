# Source: https://tinyurl.com/u2hnq84 and https://tinyurl.com/w3j4yqp
from collections import defaultdict
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occurrences, nextNums = defaultdict(int), defaultdict(int)
        for num in nums:
            occurrences[num] += 1
        for num in nums:
            if occurrences[num] == 0:
                continue
            elif nextNums[num] > 0:
                nextNums[num] -= 1
                nextNums[num + 1] += 1
            elif occurrences[num + 1] > 0 and occurrences[num + 2] > 0:
                occurrences[num + 1] -= 1
                occurrences[num + 2] -= 1
                nextNums[num + 3] += 1
            else:
                return False
            occurrences[num] -= 1
        return True