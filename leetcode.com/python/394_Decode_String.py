from collections import deque


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque();
        currentNum = 0;
        currentString = ""
        for char in s:
            if char == '[':
                stack.append(currentString)
                stack.append(currentNum)
                currentString = ''
                currentNum = 0
            elif char == ']':
                num = stack.pop()
                previousString = stack.pop()
                currentString = previousString + num * currentString
            elif char.isdigit():
                currentNum = currentNum * 10 + int(
                    char)  # We need to take care the repeated time may be over one digit, like there's a test case "100[leetcode]", we can't pass it withcurNum = int(c)
            else:
                currentString += char
        return currentString


sol = Solution()
# s = "3[a]2[bc]"
s = "3[a2[c]]"
# s = "2[abc]3[cd]ef"
out = sol.decodeString(s)
print("Res: ", out)