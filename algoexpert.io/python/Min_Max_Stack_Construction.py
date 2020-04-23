class MinMaxStack:
    def __init__(self):
        # only contains the min and max value at any given time
        # min_max_stack is an array of dictionary, which is the same length of stack
        self.min_max_stack = [] # an array of dictionary of min and max key
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # O(1) time | O(1) space
    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        new_min_max = {"min": number, "max": number}
        if len(self.min_max_stack):
            last_min_max = self.min_max_stack[len(self.min_max_stack) - 1]
            new_min_max["min"] = min(last_min_max["min"], number)
            new_min_max["max"] = max(last_min_max["max"], number)
        self.min_max_stack.append(new_min_max)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]["min"]

    # O(1) time | O(1) space
    def getMax(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]["max"]
