# Source:   https://tinyurl.com/ujv54ef . This uses backtracking approach using DFS
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allPermutations, runningPermutation = [], []
        if not nums:
            return allPermutations
        used = [False for _ in nums]
        nums.sort()
        self.generatePermutation(nums, used, runningPermutation, allPermutations)
        return allPermutations

    def generatePermutation(self, originalNums, used, runningPermutation, allPermutations):
        if len(runningPermutation) == len(originalNums):
            allPermutations.append(list(runningPermutation))
            return

        # Every stack frame of this function call represents the expression of trying (almost) all items in every "slot" in the array.
        # The recursion stops when we are choosing on 1 past the final "slot".
        for i in range(len(originalNums)):
            num = originalNums[i]

            if used[i]: # Skip the usage of same number
                continue
            if i > 0 and originalNums[i] == originalNums[i - 1] and used[i - 1]:  # Skip the duplicates
                continue
            used[i] = True

            # 1.) Choose - Add the item to the 'runningChoices'
            runningPermutation.append(num)

            # 2.) Explore - Recurse on the choice
            self.generatePermutation(originalNums, used, runningPermutation, allPermutations)

            # 3.) Backtrack - We have returned from the recursion, remove the choice we made.
            # The next iteration will try another item in the "slot" we are working on.
            runningPermutation.pop()
            used[i] = False