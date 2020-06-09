from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []

        for key in count1:
            if key in count2:
                minFreq = min(count1[key], count2[key])
                for i in range(minFreq):
                    result.append(key)

        return result