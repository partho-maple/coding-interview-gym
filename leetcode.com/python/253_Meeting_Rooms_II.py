import heapq


#   Solution 01: Official solution from leetcode itself
#   Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


#   Official solution from leetcode itself
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        occupied_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        # We are storing the meeting's END time into the heap,  So that we can know which meetiing is going to end first and we can assign new meetings aaccordingly
        heapq.heappush(occupied_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for interval in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if occupied_rooms[0] <= interval[0]:
                heapq.heappop(occupied_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(occupied_rooms, interval[1])

        return len(occupied_rooms)






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