# 1e-6  :  https://www.quora.com/What-is-1e-6

# https://tinyurl.com/rrofyuq
# :::Thought:::
# Thanks to parenthesis, we don't need to consider the influence of operator priority on calculation order.
# We pick any two numbers, num1 and num2, and apply +, -, *, / between these two numbers. Assuming that they are surrounded with parenthesis,
# that is, their result rather than themselves will participate in the following calculations.
# Take numlist = [4, 3, 2, 1] for example, assuming that we pick 4, 3 and apply +, numlist becomes [7, 2, 1].
# We don't stop following the same pattern until there is only one element in numlist. We check if the element equals to 24, that is the exhaustion condition for backtracking.



# https://tinyurl.com/upssx25
# Search for all possible cases.
class Solution(object):
    def judgePoint24(self, nums):
        if len(nums) == 1:
            if abs(nums[0]-24) <= 1e-6:
                return True
            else:
                False
        for i in range(len(nums)):
            for j in range(0, i):  #  each time we pick up two number for computation
                a = nums.pop(i)
                b = nums.pop(j)
                nxt = [a+b, a-b, b-a, a*b]
                if abs(a) > 1e-6: # To pervent division by zero error. Since you're dividing some variables, your result might be dominated by round of errors.
                    nxt.append(float(b)/float(a))
                if abs(b) > 1e-6: # To pervent division by zero error. Since you're dividing some variables, your result might be dominated by round of errors.
                    nxt.append(float(a)/float(b))
                for n in nxt:
                    nums.append(n)
                    if self.judgePoint24(nums):
                        return True
                    nums.pop()
                nums.insert(j, b)
                nums.insert(i, a)
        return False





sol = Solution()
Input = [4, 1, 8, 7]
Output = sol.judgePoint24(Input)
print("Res: ",Output)
