class MinStack(object):

    def __init__(self):
        self.main = []
        self.mins = []

    def push(self, x):
        self.main.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        item = self.main.pop()
        if item == self.mins[-1]:
            self.mins.pop()

    def top(self):
        return self.main[-1]

    def getMin(self):
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()