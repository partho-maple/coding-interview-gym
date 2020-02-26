# Time and space both O(n)
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and popped and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
        return len(stack) == 0





# Time : :(n) | Space: O(1)
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        