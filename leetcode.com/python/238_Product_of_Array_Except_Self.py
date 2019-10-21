# Time Limit Exceeded
# Time O(n^2)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0]*len(nums)
        for i in range(len(nums)):
            product1, product2 = 1, 1
            for j in range(0, i):
                product1 = product1*nums[j]
            for k in range(i+1, len(nums)):
                product2 = product2*nums[k]
            output[i] = product1*product2
        return output


# Accepted
# Time O(n) | Space O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        inputLength = len(nums)
        left, right, output = [0] * inputLength, [0] * inputLength, [0] * inputLength

        left[0] = 1
        for i in range(1, inputLength):
            left[i] = left[i - 1] * nums[i - 1]

        right[inputLength - 1] = 1
        for i in range(inputLength - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(inputLength):
            output[i] = left[i] * right[i]

        return output


# Accepted
# Time O(n) | Space O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        inputLength = len(nums)
        output = [0] * inputLength

        output[0] = 1  # Here, output array is acting as left product array
        for i in range(1, inputLength):
            output[i] = output[i - 1] * nums[i - 1]

        rightProduct = 1
        for i in range(inputLength - 1, -1, -1):
            output[i] = output[i] * rightProduct
            rightProduct *= nums[i]

        return output



sol = Solution()
input = [1, 2, 3, 4]
output = sol.productExceptSelf(input)
print("Result: ", output)