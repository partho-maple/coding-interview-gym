from heapq import heappush, heappop
from collections import Counter


# Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def inverse(self, num):
        return -1 * num

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # What are the inputs here
        #   - tasks - a list of strings the represent information we're processing
        #   - n - the time between tasks of the exact same time. This would leave us room to process other tasks
        # we asking for here?
        #   - We're looking for an int as an output. That's because we're returning a count
        #   - We're looking for the minimum number of intervals that we're going to use for the problem

        # How I think we're going to solve the problem
        # 1. We process the most important tasks often
        #   - That's because we want to process everything quickly, and processing it quickly means processing the most frequent tasks immediately after the cooldown time is over is necessary.
        # 2. Determine my interval
        #   - I want to be able to determine what step I'm at
        # 3. Create a dict of counts since I last processed my task

        # Task map to store if we've seen the item before
        task_count = Counter(tasks)
        current_time = 0
        current_heap = []

        # Sorting from least to greatest inside of the heap current_heap
        for k, v in task_count.items():
            heappush(current_heap,
                     (self.inverse(v), k))  # Pushes item from least to greatest (hence the negative values)

        # Here we're running through the entire heap and processing the sorted tasks
        while current_heap:  # We're running until this list runs out because we intend to pop elements from it
            index, temp = 0, []
            while index <= n:
                current_time += 1  # We're counting the interval time here
                if current_heap:
                    timing, taskid = heappop(current_heap)
                    # We're checking to see if it's at the end of the overall count.
                    # Remember that it was negative at the beginning
                    if timing != -1:
                        temp.append((timing + 1, taskid))
                # Checking to see if we're out of tasks. Exit the inner loop if both are true.
                # This will automatically exit out of the overall tasks
                if not current_heap and not temp:
                    break
                else:
                    index += 1
            # Because we transfered all of the items from the heap to temp, we're transferring them back to know if we should continue
            # heap -> If we're not out of tasks -> temp
            # temp -> Because we're not out -> heap
            for item in temp:
                heappush(current_heap, item)
            # We only stop if we're out of tasks
            # (Constantly checking the current_heap for if it's empty)
        return current_time



sol = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
output = sol.leastInterval(tasks, n)
print('Res: ', output)