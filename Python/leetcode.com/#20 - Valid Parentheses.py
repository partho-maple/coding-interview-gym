class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesesStack = []
        parenthesesDictionary = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in parenthesesDictionary.values():
                parenthesesStack.append(char)
                continue
            if char in parenthesesDictionary.keys():
                if len(parenthesesStack) != 0:
                    openBracket = parenthesesStack.pop()
                else:
                    return False
                if openBracket is not None and parenthesesDictionary[char] == openBracket:
                    continue
                else:
                    return False
        if len(parenthesesStack) != 0:
            return False
        return True



