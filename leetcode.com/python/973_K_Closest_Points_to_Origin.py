
import heapq

# Using MAX Heap
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if len(points) <= K:
            return points
        maxHeap = []
        for i in range(K):
            distance = self.getDistanceFromOrigin(points[i])
            heapq.heappush(maxHeap, (-distance, points[i]))

        for i in range(K, len(points)):
            destance, point = maxHeap[0]
            currentPointDistance = self.getDistanceFromOrigin(points[i])
            if currentPointDistance < -destance:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-currentPointDistance, points[i]))

        resultList = []
        for point in maxHeap:
            _, originalPoint = point
            resultList.append(originalPoint)

        return resultList


    def getDistanceFromOrigin(self, point):
        return ((point[0]*point[0]) + (point[1]*point[1]))