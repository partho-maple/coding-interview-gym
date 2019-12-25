import heapq
from collections import defaultdict


# Custom object to store the required values
class Element:
    def __init__(self, frequency, sequence, number):
        self.frequency = frequency
        self.sequence = sequence
        self.number = number


    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency

        # if both elements have same frequency, return the element that was pushed later
        return self.sequence > other.sequence



class FreqStack(object):

    def __init__(self):
        self.sequence = 0
        self.frequencyMap = defaultdict(int)
        self.maxHeap = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.frequencyMap[x] += 1
        heapq.heappush(self.maxHeap, Element(self.frequencyMap[x], self.sequence, x))
        self.sequence += 1

    def pop(self):
        """
        :rtype: int
        """
        numberToPop = heapq.heappop(self.maxHeap).number
        self.frequencyMap[numberToPop] -= 1
        return numberToPop

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()