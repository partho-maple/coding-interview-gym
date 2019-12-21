class Solution(object):

    # TODO: Bit Manipulation
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     nums.sort()
    #     for i in range(1 << len(nums)):
    #         tmp = []
    #         for j in range(len(nums)):
    #             if i & 1 << j:  # if i >> j & 1:
    #                 tmp.append(nums[j])
    #         res.append(tmp)
    #     return res

    # Backtracking approach
    def subsets(self, nums):
        allSubsets = []
        nums.sort()
        self.generateAllUniqueSubsets(nums, [], 0, allSubsets)
        return allSubsets

    def generateAllUniqueSubsets(self, originalNums, runingSubset, runingIndex, allSubsets):
        allSubsets.append(runingSubset)
        for i in range(runingIndex, len(originalNums)):
            choice = originalNums[i]
            node = runingSubset + [choice]
            print("runingSubset: ", runingSubset)
            print("choice: ", [choice])
            print("Node: ", node)
            print("-------")
            self.generateAllUniqueSubsets(originalNums, node, i + 1, allSubsets)





    # BFS approach: https://tinyurl.com/umzgkhr
    def subsets(self, nums):
        totalSubsets = []
        totalSubsets.append([])
        for currentNum in nums:
            currentSubsetsLen = len(totalSubsets)
            for idx in range(currentSubsetsLen):
                newSubset = list(totalSubsets[idx])
                newSubset.append(currentNum)
                totalSubsets.append(newSubset)
        return totalSubsets



sol = Solution()
input = [1,2,3]
out = sol.subsets(input)
print('Res: ', out)
