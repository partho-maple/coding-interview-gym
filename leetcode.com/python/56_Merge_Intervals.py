class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        mergedIntervals = []
        for i in range(len(intervals)):
            currentInterval = intervals[i]
            if mergedIntervals and currentInterval[0] <= mergedIntervals[-1][1]:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], currentInterval[1])
            else:
                mergedIntervals.append(currentInterval)
        return mergedIntervals



sol = Solution()
input = [[1,4],[0,4]]
output = sol.merge(input)
print('Res: ', output)