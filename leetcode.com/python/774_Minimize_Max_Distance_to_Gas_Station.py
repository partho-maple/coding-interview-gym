# Approach 1: Brute force. time limit exceeded
# Time: O(nk)
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        initialStationCount = len(stations)
        stationIntervalDistances = [float(stations[i + 1] - stations[i]) for i in range(initialStationCount - 1)]
        stationCountInInterval = [1] * (
                    initialStationCount - 1)  # initially we have only one station between any interval

        for _ in range(K):
            maxIntervalIdx = 0
            for i, interval in enumerate(stationIntervalDistances):
                currentInterval = interval / stationCountInInterval[i]
                maxInterval = stationIntervalDistances[maxIntervalIdx] / stationCountInInterval[maxIntervalIdx]
                if currentInterval > maxInterval:
                    maxIntervalIdx = i
            stationCountInInterval[maxIntervalIdx] += 1

        minInterval = 0.0
        for i, interval in enumerate(stationIntervalDistances):
            minInterval = max(minInterval, interval / stationCountInInterval[i])

        return minInterval




# Approach 2: Heap
# Time: O(k log n)
import heapq
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        heap = []   # (-part_length, original_length, num_parts)
        for i in range(len(stations) - 1):
            startStationDistace = stations[i]
            endStationDistance = stations[i + 1]
            heap.append(-(endStationDistance - startStationDistace), (endStationDistance - startStationDistace), 1) #  In Python, we use a negative priority to simulate a max heap with a min heap.
        heapq.heapify(heap)

        for _ in range(K):
            negativePartitionedDistance, originalDistance, stationCount = heapq.heappop(heap)
            stationCount += 1
            heapq.heappush(heap, (-(originalDistance / float(stationCount)), originalDistance, stationCount))

        return -heap[0][0]




# Approach 3: Binary Search
# Time: O(k log n)
class Solution(object):
    def checkValidDistance(self, distance, stations, K):
        totalStationCount = 0
        for i in range(len(stations) - 1):
            intervalDistance = stations[i + 1] - stations[i]
            currentIntervalDistanceStationCount = int(intervalDistance / distance)
            totalStationCount += currentIntervalDistanceStationCount
        return totalStationCount <= K

    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        low, high = 0, 10 ** 8
        while high - low > 1e-6:
            mid = (low + high) / 2.0
            isValid = self.checkValidDistance(mid, stations, K)
            if isValid:
                high = mid
            else:
                low = mid
        return low
