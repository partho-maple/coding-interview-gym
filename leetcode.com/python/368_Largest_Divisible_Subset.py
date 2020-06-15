# DP bottom-up tabulation
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}

        for num in sorted(nums):
            currentSubSets = []
            for key in subsets:
                if num % key == 0:
                    newSet = set(subsets[key])
                    newSet.add(num)
                    currentSubSets.append(newSet)
            if currentSubSets is not None:
                subsets[num] = max(currentSubSets, key=len)
            else:
                subsets[num] = {num}
        return list(max(subsets.values(), key=len))


# # DP top-down recursive - To Be Finished
# class Solution(object):
#     def largestDivisibleSubset(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # The container that holds all intermediate solutions.
#         # key: the largest element in a valid subset.
#         if not nums:
#             return []
#         nums.sort()
#         memo = {}
#         self.largestDivisibleSubsetHelper(nums, memo)
#         return list(max(memo.values(), key=len))

#     def largestDivisibleSubsetHelper(self, nums, memo):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         pass

"""
1,2,3
  i
    j

1%2=0 or 2%1=0 > 1,2
1%3=0 or 3%1=0 > 1,2


1,2,4,8

12 14 18 24 28 48 >>1248


1248

  1 2 4 8
1 1  
2   2 
4     4 
8       8

"""