class Solution(object):
    # Bit Manipulation
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res



sol = Solution()
input = [1,2,3]
out = sol.subsets(input)
print('Res: ', out)
