import bisect

#  Not so easy and intuitive. Can be solve is a variety of way. I have used Binary search(A bit over engineered solution). Can be simplifies
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        occupiedSeats = []
        for i in range(len(seats)):
            if seats[i] == 1:
                occupiedSeats.append(i)
        maxDist = 1
        for i, seat in enumerate(seats):
            leftDist, rightDist = 1, 1
            if seat == 1:
                continue
            insertionIdx = bisect.bisect_left(occupiedSeats, i)

            if insertionIdx >= len(occupiedSeats):
                rightOccupiedSeatIdx = len(seats)
                rightDist = float("inf")
            else:
                rightOccupiedSeatIdx = occupiedSeats[insertionIdx]
                rightDist = rightOccupiedSeatIdx - i

            if insertionIdx <= 0:
                leftOccupiedSeatIdx = 0
                leftDist = float("inf")
            else:
                leftOccupiedSeatIdx = occupiedSeats[insertionIdx - 1]
                leftDist = i - leftOccupiedSeatIdx
            maxDist = max(maxDist, min(leftDist, rightDist))
        return maxDist