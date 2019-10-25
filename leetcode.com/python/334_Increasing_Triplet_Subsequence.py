

#   Solution 1: Two pointer technique
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        firstNum, secondNum = float('inf'), float('inf')
        for num in nums:
            if num <= firstNum:
                firstNum = num
            elif num <= secondNum:
                secondNum = num
            else:
                return True
        return False


#   Solution 2: generic solution that checks for K increasing numbers in an array. So the triplet solution is just K=3.
class Solution:
    def increasingTriplet(self, nums):
        return self.increasingKlet(nums, 3)

    def increasingKlet(self, nums, k):
        '''
        Approach: start with k-1 very large values, as soon as we
        find a number bigger than all k-1, return true.
        Time: O(n*k)
        Space: O(k)
        this is the generic solution for this problem
        '''
        small_arr = [float('inf') for _ in range(k)]

        for num in nums:
            for i in range(k-1):
                if num <= small_arr[i]:
                    small_arr[i] = num
                    break

            if num > small_arr[-1]:
                return True

        return False
