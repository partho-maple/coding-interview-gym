# https://tinyurl.com/r35ffgt
from collections import deque
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        tokensDeque = deque(tokens)
        stack = []
        opes = ["+", "-", "*", "/"]
        while tokensDeque:
            currentToken = tokensDeque.popleft()
            if currentToken in opes:
                firstNum = int(stack.pop())
                secondNum = int(stack.pop())
                result = 0
                if currentToken == "+":
                    result = secondNum + firstNum
                elif currentToken == "-":
                    result = secondNum - firstNum
                elif currentToken == "*":
                    result = secondNum * firstNum
                else:
                    if firstNum*secondNum < 0 and secondNum%firstNum != 0:
                        result = secondNum // firstNum + 1
                    else:
                        result = secondNum // firstNum
                stack.append(str(result))
            else:
                stack.append(currentToken)
        return stack[-1]
