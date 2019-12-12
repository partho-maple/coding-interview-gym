import heapq



# Official Definition for an Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



# Custom object definition to help operate the operations
class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval                    # interval representing employee's working hours
        self.employeeIndex = employeeIndex          # index of the list containing working hours of this employee
        self.intervalIndex = intervalIndex          # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        scheduleLength = len(schedule)
        freeIntervals = []
        if not schedule or scheduleLength <= 0:
            return freeIntervals
        minHeap = []
        for index, employeeSchedule in enumerate(schedule):                     # insert the first interval of each employee to the queue/minHeap
            minHeap.append(EmployeeInterval(employeeSchedule[0], index, 0))
        heapq.heapify(minHeap)                                                  # create the heap from the array
        previousInterval = minHeap[0].interval
        while minHeap:
            queueTop = heapq.heappop(minHeap)
            if previousInterval.end < queueTop.interval.start:                  # if previousInterval is not overlapping with the next interval, insert a free interval
                freeIntervals.append(Interval(previousInterval.end, queueTop.interval.start))
                previousInterval = queueTop.interval
            else:                                                               # overlapping intervals, update the previousInterval if needed
                if previousInterval.end < queueTop.interval.end:
                    previousInterval = queueTop.interval
            intervalsArrayOfEmployee = schedule[queueTop.employeeIndex]
            nextIntervalIndexOfCurrentEmployee = queueTop.intervalIndex + 1
            if len(intervalsArrayOfEmployee) > nextIntervalIndexOfCurrentEmployee:           # if there are more intervals available for the same employee, add their next interval
                heapq.heappush(minHeap, EmployeeInterval(intervalsArrayOfEmployee[nextIntervalIndexOfCurrentEmployee], queueTop.employeeIndex, nextIntervalIndexOfCurrentEmployee))
        return freeIntervals


