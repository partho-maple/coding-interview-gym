# Official solution
class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])
        return answers



# My own solution, wrong answer. Couldn't figure out the correct one by myself.
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        nums = list(num)
        ops = ["+", "-", "*", "no-op"]  # no-op means, just take this current num and then go
        currentExpression, allExpression = [], set()
        self.addOperatorsHelper(nums, target, 0, ops, currentExpression, 0, 0, allExpression)
        return list(allExpression)

    def addOperatorsHelper(self, nums, target, currentNumIdx, ops, currentExpression, currentExpressionValue,
                           previousOperand, allExpression):
        if currentNumIdx == len(nums):
            expression = "".join(currentExpression[1:])
            if currentExpression[0].isdigit():
                expression = "".join(currentExpression)
            value = eval(expression)
            if value == target:
                # expression = "".join(currentExpression[1:])
                allExpression.add(expression)
            return

        for op in ops:
            if op == "+" or op == "-":
                currentExpression.append(op)
                currentExpression.append(nums[currentNumIdx])
                self.addOperatorsHelper(nums, target, currentNumIdx + 1, ops, currentExpression, currentExpressionValue,
                                        previousOperand, allExpression)
                currentExpression.pop()  # backtrack
                currentExpression.pop()  # backtrack
            elif op == "*":
                currentExpression.append(op)
                currentExpression.append(nums[currentNumIdx])
                self.addOperatorsHelper(nums, target, currentNumIdx + 1, ops, currentExpression, currentExpressionValue,
                                        previousOperand, allExpression)
                currentExpression.pop()  # backtrack
                currentExpression.pop()  # backtrack
            else:
                if nums[currentNumIdx] != "0" and currentExpression and currentExpression[-1] != "0":
                    currentExpression.append(nums[currentNumIdx])
                    self.addOperatorsHelper(nums, target, currentNumIdx + 1, ops, currentExpression,
                                            currentExpressionValue, previousOperand, allExpression)
                    currentExpression.pop()  # backtrack


"""
Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 

generate all expression
    backtracking
evaluate the expression and take valid one
"""
