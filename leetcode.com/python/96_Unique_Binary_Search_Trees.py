# Source:   https://tinyurl.com/ut8wh4u   and    https://tinyurl.com/wuzpywc    and     https://tinyurl.com/vb3s4jm
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]





# Source:   https://tinyurl.com/yx2ktbup
# Getting TLE
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        totalBstCount = 0
        for nodeIdx in range(1, n + 1):
            # making 'i' root of the tree
            bstCountOfLeftSubTree = self.numTrees(nodeIdx - 1)
            bstCountOfRightSubTree = self.numTrees(n - nodeIdx)
            totalBstCount += (bstCountOfLeftSubTree * bstCountOfRightSubTree)
        return totalBstCount




from collections import defaultdict
# Source:   https://tinyurl.com/yx2ktbup
# Memoized version of the above solution
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        resultCache = defaultdict()
        return self.numTreesHelper(n, resultCache)

    def numTreesHelper(self, n, resultCache):
        """
        :type n: int
        :rtype: int
        """
        if n in resultCache:
            return resultCache[n]
        if n <= 1:
            return 1
        totalBstCount = 0
        for nodeIdx in range(1, n + 1):
            # making 'i' root of the tree
            bstCountOfLeftSubTree = self.numTreesHelper(nodeIdx - 1, resultCache)
            bstCountOfRightSubTree = self.numTreesHelper(n - nodeIdx, resultCache)
            totalBstCount += (bstCountOfLeftSubTree * bstCountOfRightSubTree)
        resultCache[n] = totalBstCount
        return totalBstCount
