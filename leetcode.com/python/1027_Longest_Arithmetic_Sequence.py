from collections import defaultdict


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = defaultdict(lambda: 1)  # setting the default value of defaultdict to 1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                ai, aj = A[i], A[j]
                dp[j, aj - ai] = dp[i, aj - ai] + 1
        return max(dp.values())


"""
[9,4,7,2,10]  >> [4,7,10]

 j>
i 9,4,7,2,10
V
9   x   
4     x    
7       x
2         x
10          x 

"""