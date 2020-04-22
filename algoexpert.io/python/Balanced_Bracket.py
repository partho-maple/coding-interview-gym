# https://www.algoexpert.io/questions/Balanced%20Brackets


# O(n) time | O(n space)
def balancedBrackets(string):
    opening_brackets = "([{"
    closing_brackets = ")]}"
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

