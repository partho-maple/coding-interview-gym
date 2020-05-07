import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        sticksHeap = list(sticks)
        heapq.heapify(sticksHeap)
        minCost = 0
        while len(sticksHeap) > 1:
            firstNum = heapq.heappop(sticksHeap)
            secondNum = heapq.heappop(sticksHeap)
            minCost += firstNum
            minCost += secondNum
            sumNum = firstNum + secondNum
            heapq.heappush(sticksHeap, sumNum)
        return minCost


"""
Example 1
sticks = [2,4,3]

Step 1:
cost -> 2+3 = 5
result -> [5,4]

Step 2:
cost -> 5+4 = 9
result -> [9]

FINAL COST =5 + 9 = 14

2,4=6
>6,3=9

6+9=15
"""