from collections import defaultdict


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = []
        self.timestampHitMap = defaultdict(int)

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if timestamp < 1:
            return
        if not self.timestamps or self.timestamps[-1] != timestamp:
            self.timestamps.append(timestamp)
        self.timestampHitMap[timestamp] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        hitCount, startIdx = 0, 0
        for i in range(len(self.timestamps) - 1, -1, -1):
            startTime = self.timestamps[i]
            if timestamp - startTime < 300:
                hitCount += self.timestampHitMap[startTime]
                startIdx = i
            else:
                if startTime in self.timestampHitMap:
                    del self.timestampHitMap[startTime]
        self.timestamps = self.timestamps[startIdx:]
        return hitCount

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)