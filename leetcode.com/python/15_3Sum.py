# Time Limit Exceeded

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         triplates = []
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             left = i + 1
#             right  = len(nums) - 1
#             while left < right:
#                 currentSum = nums[i] + nums[left] + nums[right]
#                 if currentSum == 0:
#                     if [nums[i], nums[left], nums[right]] not in triplates:
#                         triplates.append([nums[i], nums[left], nums[right]])
#                     left += 1
#                     right -= 1
#                 elif currentSum < 0:
#                     left += 1
#                 elif currentSum > 0:
#                     right -= 1
#         return triplates




class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result



# My solution during Mock
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 2:
            return []
        sortedNums = sorted(nums)
        results = []
        resultMap = {}
        for first in range(0, len(sortedNums) - 2):
            firstNum = sortedNums[first]
            second, third = first + 1, len(sortedNums) - 1
            while second < third:
                secondNum, thirdNum = sortedNums[second], sortedNums[third]
                if (firstNum + secondNum + thirdNum) == 0:
                    key = str(firstNum) + "-" + str(secondNum) + "-" + str(thirdNum)
                    if key not in resultMap:
                        results.append([firstNum, secondNum, thirdNum])
                        resultMap[key] = 1
                    second += 1
                    third -= 1
                elif (firstNum + secondNum + thirdNum) > 0:
                    third -= 1
                else:
                    second += 1
        return results




