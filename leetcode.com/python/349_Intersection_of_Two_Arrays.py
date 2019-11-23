class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        # # Using manual  Set Intersection
        # if len(set1) < len(set2):
        #     return self.setIntersection(set1, set2)
        # else:
        #     return self.setIntersection(set2, set1)

        # Using Build-in Set Intersection
        return list(set1 & set2)

    def setIntersection(self, set1, set2):
        return [x for x in set1 if x in set2]


