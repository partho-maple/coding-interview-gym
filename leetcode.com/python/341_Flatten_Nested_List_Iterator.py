# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """



from collections import deque
# Approach 1: Brite force ut not good for the interview. This approach, modifies the input list
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.q = deque()
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for l in nestedList:
            if l.isInteger():
                self.q.append(l.getInteger())
            else:
                self.flatten(l.getList())

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0




# Approach 2: This approach, doesn't modify the input list but depends on hasNext to be called, which is also not good and not the perfect implementation for the interview
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        print("nestedList: ", nestedList)
        self.__nestedList = nestedList
        self.__position = 0
        self.__lists = []

    def next(self) -> int:
        integer = self.__nestedList[self.__position].getInteger()
        self.__position += 1
        print("------")
        print("integer: ", integer)
        print("self.__nestedList: ", self.__nestedList)
        print("self.__position: ", self.__position)
        print("self.__lists: ", self.__lists)
        return integer

    def hasNext(self) -> bool:
        while not self.__isComplete():
            currNode = self.__nestedList[self.__position]

            if currNode.isInteger():
                return True
            else:
                self.__position += 1
                self.__lists.append((self.__nestedList, self.__position))
                self.__position = 0
                self.__nestedList = currNode.getList()

        if self.__isComplete() and not self.__listEmpty():
            self.__nestedList, self.__position = self.__lists.pop()
            return self.hasNext()

        return False

    def __listEmpty(self) -> bool:
        return len(self.__lists) == 0

    def __isComplete(self) -> bool:
        return self.__position >= len(self.__nestedList)



# Most optimal and preferd approach
# https://tinyurl.com/rotxca8
# Debug the code to get a clear idea
class NestedIterator(object):

    def __init__(self, nestedList):
        self.nestedListStack = [[nestedList, 0]]  # <list, current element index/position on the nested list>

    # Here, next method does't have any dependency over hasNext
    def next(self):
        currentNestedListStack = self.nestedListStack
        nestedList, currentPositionIdx = currentNestedListStack[-1]
        currentNestedListStack[-1][
            1] += 1  # updating currentPositionIdx by 1, since we are sending the current integer here, on next line
        return nestedList[currentPositionIdx].getInteger()

    def hasNext(self):
        currentNestedListStack = self.nestedListStack
        while currentNestedListStack:
            nestedList, currentPositionIdx = currentNestedListStack[-1]
            if currentPositionIdx == len(nestedList):  # we are done with this nested list, let's pop it out.
                currentNestedListStack.pop()
            else:
                currentItem = nestedList[currentPositionIdx]
                if currentItem.isInteger():
                    return True
                currentNestedListStack[-1][1] += 1  # incremets current nestedListStack index
                currentNestedListStack.append([currentItem.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())