from heapq import heappush, heappop
from collections import Counter


# Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:

    # Uses Heap. inspired from https://tinyurl.com/rmlstk3
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskFrequencies = Counter(tasks)
        totalIntervals = 0
        priorityQueue = []
        for k, v in taskFrequencies.items():
            heappush(priorityQueue, (-v, k))
        while priorityQueue:
            currentCoolingInterval, tempTaskHolder = -1, []
            while currentCoolingInterval < n:
                if priorityQueue:
                    totalIntervals += 1
                    currentCoolingInterval += 1
                    taskFrequency, taskID = heappop(priorityQueue)
                    if taskFrequency != -1:
                        tempTaskHolder.append((taskFrequency + 1, taskID))
                else:
                    if tempTaskHolder: # We still have task to process
                        totalIntervals += (n - currentCoolingInterval)
                    break
            for item in tempTaskHolder:
                heappush(priorityQueue, item)
        return totalIntervals



sol = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
output = sol.leastInterval(tasks, n)
print('Res: ', output)