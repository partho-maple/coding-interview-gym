class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allPermutations = []
        runningChoices = []
        self.generatePermutation(runningChoices, nums, allPermutations)
        return allPermutations

    def generatePermutation(self, runningChoices, originalNums, allPermutations):
        if len(runningChoices) == len(originalNums):
            finalPermutation = [choice for choice in runningChoices]
            allPermutations.append(finalPermutation)
            return

        # Every stack frame of this function call represents the expression of trying (almost) all items in every "slot" in the array.
        # The recursion stops when we are choosing on 1 past the final "slot".
        for i in range(len(originalNums)):
            choice = originalNums[i]

            # Skip if element already exists in 'runningChoices'
            if choice in runningChoices:
                continue

            # 1.) Choose - Add the item to the 'runningChoices'
            runningChoices.append(choice)

            # 2.) Explore - Recurse on the choice
            self.generatePermutation(runningChoices, originalNums, allPermutations)

            # 3.) Unchoose - We have returned from the recursion, remove the choice we made.
            # The next iteration will try another item in the "slot" we are working on.
            runningChoices.pop()





sol = Solution()
input = [1,2,3]
output = sol.permute(input)
print('Res: ', output)