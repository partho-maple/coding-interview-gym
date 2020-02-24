class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        aValWithIdxTupleArray = [[a, i] for i, a in enumerate(A)]
        aValWithIdxTupleArray = sorted(aValWithIdxTupleArray)
        for a, i in aValWithIdxTupleArray:
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        negative_aValWithIdxTupleArray = [[-a, i] for i, a in enumerate(A)]
        negative_aValWithIdxTupleArray = sorted(negative_aValWithIdxTupleArray)
        for a, i in negative_aValWithIdxTupleArray:
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher) # Why it's higher ?  Because we will always be starting with odd jumps which will go for next heigher numbers. Since we need to send all heigher 