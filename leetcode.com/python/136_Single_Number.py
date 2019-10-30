class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueNum = 0
        for num in nums:
            uniqueNum ^= num
        return uniqueNum




sol = Solution()
input = [4,1,2,1,2]
output = sol.singleNumber(input)
print('Res: ',output)