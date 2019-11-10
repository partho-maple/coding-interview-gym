from collections import Counter
import heapq

class Solution(object):

    # # Using only HashMap/Dictionary
    # def topKFrequent(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     count = Counter(nums)
    #     elements = count.most_common(k)
    #     common_keys = [x[0] for x in elements]
    #     return common_keys


    # Using heap and map
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        keys = count.keys()
        common_keys = heapq.nlargest(k, keys, key=count.get) # key=count.get is used to sory y value in asending order
        return common_keys



sol = Solution()
nums = [4,1,-1,2,-1,2,3]
k = 2
out = sol.topKFrequent(nums, k)
print('Res: ',out)