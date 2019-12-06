class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefixSum = [0] * (len(nums) + 1)
        currentSum = 0
        for idx, num in enumerate(nums):
            currentSum += num
            self.prefixSum[idx + 1] = currentSum


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        rangeSum = self.prefixSum[j + 1] - self.prefixSum[i]
        return rangeSum

# Your NumArray object will be instantiated and called as such:
nums = [-2,0,3,-5,2,-1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(2,5)
param_3 = obj.sumRange(0,5)
param_4 = obj.sumRange(4,3)
print("Res: ", param_4)