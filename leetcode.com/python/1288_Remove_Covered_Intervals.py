class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by start point.
        # If two intervals share the same start point
        # put the longer one to be the first.
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0

        prevEnd = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previous one
            if end > prevEnd:
                count += 1
                prevEnd = end
        return count
