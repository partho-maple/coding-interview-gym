class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        mergedIntervals = []
        index, start, end = 0, 0, 1
        while index < len(intervals) and intervals[index][end] < newInterval[start]:            # skip (and add to output) all intervals that come before the 'new_interval'
            mergedIntervals.append(intervals[index])
            index += 1
        while index < len(intervals) and intervals[index][start] <= newInterval[end]:           # merge all intervals that overlap with 'new_interval'
            newInterval[start] = min(intervals[index][start], newInterval[start])
            newInterval[end] = max(intervals[index][end], newInterval[end])
            index += 1
        mergedIntervals.append(newInterval)                                                     # insert the new_interval
        while index < len(intervals):                                                           # add all the remaining intervals to the output
            mergedIntervals.append(intervals[index])
            index += 1
        return mergedIntervals



