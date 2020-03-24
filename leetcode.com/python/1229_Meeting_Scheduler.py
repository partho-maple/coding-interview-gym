import heapq
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        schedules = list(slots1 + slots2)
        schedules = filter(lambda slot: slot[1] - slot[0] >= duration, schedules)
        heapq.heapify(schedules)
        while len(schedules) > 1:
            if heapq.heappop(schedules)[1] >= schedules[0][0] + duration:
                return [schedules[0][0], schedules[0][0] + duration]
        return []