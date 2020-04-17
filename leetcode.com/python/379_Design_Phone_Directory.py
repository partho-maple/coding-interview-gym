import heapq


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.phoneDictSts = {}
        self.availableNums = []
        for i in range(maxNumbers):
            self.phoneDictSts[i] = True
            heapq.heappush(self.availableNums, i)

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.availableNums) > 0:
            num = heapq.heappop(self.availableNums)
            self.phoneDictSts[num] = False
            return num
        else:
            return -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if self.phoneDictSts[number] == True:
            return True
        else:
            return False

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if self.phoneDictSts[number] == False:
            self.phoneDictSts[number] = True
            heapq.heappush(self.availableNums, number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)