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


sol = Solution()
# input = [82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324,1202,-90885,-2989,-95597,-34333,35528,5680,89093,-90606,50360,-29393,-27012,53313,65213,99818,-82405,-41661,-3333,-51952,72135,-1523,26377,74685,96992,92263,15929,5467,-99555,-43348,-41689,-60383,-3990,32165,65265,-72973,-58372,12741,-48568,-46596,72419,-1859,34153,62937,81310,-61823,-96770,-54944,8845,-91184,24208,-29078,31495,65258,14198,85395,70506,-40908,56740,-12228,-40072,32429,93001,68445,-73927,25731,-91859,-24150,10093,-60271,-81683,-18126,51055,48189,-6468,25057,81194,-58628,74042,66158,-14452,-49851,-43667,11092,39189,-17025,-79173,13606,83172,92647,-59741,19343,-26644,-57607,82908,-20655,1637,80060,98994,39331,-31274,-61523,91225,-72953,13211,-75116,-98421,-41571,-69074,99587,39345,42151,-2460,98236,15690,-52507,-95803,-48935,-46492,-45606,-79254,-99851,52533,73486,39948,-7240,71815,-585,-96252,90990,-93815,93340,-71848,58733,-14859,-83082,-75794,-82082,-24871,-1
input = [-1, 0, 1, 2, -1, -4]
triplets = sol.threeSum(input)
print("Result: ", triplets)




