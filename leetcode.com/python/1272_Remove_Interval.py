class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        removeStart, removeEnd = toBeRemoved
        output = []
        for start, end in intervals:
            if end <= removeStart or start >= removeEnd:
                output.append([start, end])
            elif start < removeStart and end > removeEnd:
                output.append([start, removeStart])
                output.append([removeEnd, end])
            elif start < removeStart and end <= removeEnd:
                output.append([start, removeStart])
            elif start >= removeStart and end > removeEnd:
                output.append([removeEnd, end])
        return output
