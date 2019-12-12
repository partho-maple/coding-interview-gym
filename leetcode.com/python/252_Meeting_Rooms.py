class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        start, end = 0, 1
        intervals.sort(key = lambda x: x[end])
        for idx in range(1, len(intervals)):
            if intervals[idx - 1][end] > intervals[idx][start]:
                return False
        return True