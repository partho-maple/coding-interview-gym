# Source: https://tinyurl.com/t59zg3e
# Approach 3: Line Sweep
# Time Complexity: O(N^2 log N) , nlogn is for sorting. the intervals and n is for the length. of intervals
# https://tinyurl.com/v9mdkla
class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # Pre processing, populate events
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        active = []
        prevY = events[0][0]
        area = 0
        for currY, itervalType, openX1, closeX2 in events:
            # For all vertical ground covered, update answer
            height = currY - prevY
            width = self.mergeInterval(active)
            area += width * height

            if itervalType is OPEN:
                active.append((openX1, closeX2))
                active.sort()
            else:
                active.remove((openX1, closeX2))

            prevY = currY

        return area % (10 ** 9 + 7)

    # This calculates the total horizontal length of our active intervals
    def mergeInterval(self, activeIntervals):
        width, prevX1 = 0, -1
        for x1, x2 in activeIntervals:
            prevX1 = max(prevX1, x1)
            width += max(0, x2 - prevX1)
            prevX1 = max(prevX1, x2)
        return width
