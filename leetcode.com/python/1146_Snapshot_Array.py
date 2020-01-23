import bisect
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = [[[-1, 0]] for _ in range(length)]
        self.currentSnapID = 0
        self.length = length

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index].append([self.currentSnapID, val])

    def snap(self):
        """
        :rtype: int
        """
        self.currentSnapID += 1
        return self.currentSnapID - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        recordIdxforSnapAtIdx = bisect.bisect(self.array[index], [snap_id + 1]) - 1
        return self.array[index][recordIdxforSnapAtIdx][1]



# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0,5)
param_2 = obj.snap()
obj.set(0,6)
v  = param_3 = obj.get(0,0)
print(v)