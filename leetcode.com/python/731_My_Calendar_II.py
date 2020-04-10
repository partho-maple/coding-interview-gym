class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # self.bookings  = sorted(self.bookings)
        overlapCount = 0
        for slot in self.bookings:
            st, ed = slot
            if st < start < ed or st <= end < ed:
                overlapCount += 1
        if overlapCount >= 3:
            return False
        else:
            self.bookings.append([start, end])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)