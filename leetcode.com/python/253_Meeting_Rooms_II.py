import heapq


#   Solution 01: Official solution from leetcode itself
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 1:
            return 0
        # The heap initialization
        usedRooms = []

        # Sort the meetings in increasing order of their start time
        intervals.sort(key= lambda x: x[0])

        # Add  the first meetinng. we have to give a new room to the first meeting
        heapq.heappush(usedRooms, intervals[0][1])

        # For all the remaining meeting rooms
        for interval in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if interval[0] >= usedRooms[0]:
                heapq.heappop(usedRooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(usedRooms, interval[1])

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        return len(usedRooms)





#   Solution 02: Official solution from leetcode itself
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 1:
            return 0

        usedRooms = 0

        startTiming = sorted([i[0] for i in intervals])
        endTiming = sorted([i[1] for i in intervals])
        length = len(intervals)

        endPointer = 0
        startPointer = 0

        while startPointer < length:
            if startTiming[startPointer] >= endTiming[endPointer]:
                usedRooms -= 1
                endPointer += 1
            startPointer += 1
            usedRooms += 1

        return usedRooms





# sol = Solution()
# input = [[9,10],[4,9],[4,17]]
# output = sol.minMeetingRooms(input)
# print('Res: ',output)