class Solution(object):

    # outer for loop runs for all characters and the inner while loop processes each character only once,
    # therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N)
    # algorithm runs in constant space O(1)
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        return self.totalNumbberOfKFruit(tree, 2)

    # maxFruitType is similar to number  of baskets where each baskets can contain only one type of fruit
    def totalNumbberOfKFruit(self, tree, maxFruitType):
        windowStart = 0
        maxLength = 0
        fruitFrequency = {}

        # try to  extend the range [windowStart, windowEnd]
        for windowEnd in range(len(tree)):
            rightFruitType = tree[windowEnd]
            if rightFruitType not in fruitFrequency:
                fruitFrequency[rightFruitType] = 0
            fruitFrequency[rightFruitType] += 1

            # shrink the sliding window from the left side, until we are left with last 2 fruits
            while len(fruitFrequency) > maxFruitType:
                leftFruitType = tree[windowStart]
                fruitFrequency[leftFruitType] -= 1
                if fruitFrequency[leftFruitType] == 0:
                    del fruitFrequency[leftFruitType]
                windowStart += 1  # shrink the window
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        return maxLength




sol = Solution()
input = [1,1,2,3,2,2,2]
output = sol.totalFruit(input)
print('Total Fruit: ', output)
