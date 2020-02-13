import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valueIdxMap = {}
        self.valueList = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.valueIdxMap:
            return False
        self.valueIdxMap[val] = len(self.valueList)
        self.valueList.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.valueIdxMap:
            idx = self.valueIdxMap[val]
            lastVal = self.valueList[-1]
            self.valueList[idx] = lastVal
            self.valueIdxMap[lastVal] = idx
            self.valueList.pop()
            del self.valueIdxMap[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.valueList)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()