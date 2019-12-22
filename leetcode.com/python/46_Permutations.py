# Source:   https://tinyurl.com/ujv54ef . This uses backtracking approach using DFS
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allPermutations, runningPermutation = [], []
        self.generatePermutation(nums, runningPermutation, allPermutations)
        return allPermutations

    def generatePermutation(self, originalNums, runningPermutation, allPermutations):
        if len(runningPermutation) == len(originalNums):
            allPermutations.append(list(runningPermutation))
            return

        # Every stack frame of this function call represents the expression of trying (almost) all items in every "slot" in the array.
        # The recursion stops when we are choosing on 1 past the final "slot".
        for i in range(len(originalNums)):
            num = originalNums[i]

            # Skip if element already exists in 'runningChoices'
            if num in runningPermutation:
                continue

            # 1.) Choose - Add the item to the 'runningChoices'
            runningPermutation.append(num)

            # 2.) Explore - Recurse on the choice
            self.generatePermutation(originalNums, runningPermutation, allPermutations)

            # 3.) Unchoose - We have returned from the recursion, remove the choice we made.
            # The next iteration will try another item in the "slot" we are working on.
            runningPermutation.pop()







from collections import deque
# Source:   https://tinyurl.com/s3ncxtn . This uses BFS to create all subsets of it's each levels.
class Solution(object):

    # Recursive solution
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allPermutations = []
        self.generatePermutation(nums, 0, [], allPermutations)
        return allPermutations

    def generatePermutation(self, originalNums, currentIndex, runningPermutation, allPermutations):
        if currentIndex == len(originalNums):
            # finalPermutation = list(runningPermutation)
            allPermutations.append(runningPermutation)
        else:
            # create a new permutation by adding the current number at every position
            for idx in range(len(runningPermutation) + 1):
                newPermutation = list(runningPermutation)
                newPermutation.insert(idx, originalNums[currentIndex])
                self.generatePermutation(originalNums, currentIndex + 1, newPermutation, allPermutations)





    # Iterative solution
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allPermutations = []
        currentPermutations = deque()
        currentPermutations.append([])
        for idx, currentNum in enumerate(nums):
            # we will take all existing permutations and add the current number to create new permutations
            currentPermutationsLength = len(currentPermutations)
            for _ in range(currentPermutationsLength):
                oldPermutation = currentPermutations.popleft()
                # create a new permutation by adding the current number at every position
                for position in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(position, currentNum)
                    if len(newPermutation) == len(nums):
                        allPermutations.append(newPermutation)
                    else:
                        currentPermutations.append(newPermutation)
        return allPermutations













sol = Solution()
input = [1,2,3]
output = sol.permute(input)
print('Res: ', output)