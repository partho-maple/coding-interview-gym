class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        previousEnd = float('-inf')
        erased = 0
        for interval in sorted(intervals, key= lambda x: x[1]):
            currentStart = interval[0]
            if currentStart >= previousEnd:
                previousEnd = interval[1]
            else:
                erased += 1
        return erased



sol = Solution()
intervals = [[1,2],[1,2],[1,2]]
out = sol.eraseOverlapIntervals(intervals)
print("Res: ", out)
