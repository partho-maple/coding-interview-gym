# First attempt:    26 / 61 test cases passed. Segment tree + prefixSum. Not accepted
# https://leetcode.com/submissions/detail/316497775/
class SegmentTreeNode(object):
    def __init__(self, rangeStartIdx, rangeEndIdx):
        self.rangeStartIdx = rangeStartIdx
        self.rangeEndIdx = rangeEndIdx
        self.rangeSum = 0
        self.rangeSumCount = 0
        self.leftNode = None
        self.rightNode = None

class Solution(object):

    def createSegmetTree(self, nums, rangeStartIdx, rangeEndIdx, queryStart, queryEnd):
        if rangeStartIdx > rangeEndIdx:
            return None

        if rangeStartIdx == rangeEndIdx:
            leafNode = SegmentTreeNode(rangeStartIdx, rangeEndIdx)
            leafNode.rangeSum = nums[rangeStartIdx]
            if queryStart <= leafNode.rangeSum <= queryEnd:
                leafNode.rangeSumCount += 1
            return leafNode

        midIdx = (rangeStartIdx + rangeEndIdx) // 2
        curretRoot = SegmentTreeNode(rangeStartIdx, rangeStartIdx)
        curretRoot.leftNode = self.createSegmetTree(nums, rangeStartIdx, midIdx, queryStart, queryEnd)
        curretRoot.rightNode = self.createSegmetTree(nums, midIdx + 1, rangeEndIdx, queryStart, queryEnd)
        curretRoot.rangeSum = curretRoot.leftNode.rangeSum + curretRoot.rightNode.rangeSum
        curretRoot.rangeSumCount = curretRoot.leftNode.rangeSumCount + curretRoot.rightNode.rangeSumCount
        if queryStart <= curretRoot.rangeSum <= queryEnd:
            curretRoot.rangeSumCount += 1
        return curretRoot

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        rootNode = self.createSegmetTree(nums, 0, len(nums) - 1, lower, upper)
        return rootNode.rangeSumCount


# Source: https://tinyurl.com/rlmha9k
# Approach : Prefix-sum + Hashmap
from collections import defaultdict
class Solution(object):

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sumRecords = defaultdict(int)
        prefixSums = [0]
        for num in nums:
            prefixSums.append(prefixSums[-1] + num)

        count = 0
        for prefixSum in prefixSums:
            for targerSum in range(lower, upper + 1):
                if prefixSum - targerSum in sumRecords:
                    count += sumRecords[prefixSum - targerSum]
            sumRecords[prefixSum] += 1

        return count



# Source: https://tinyurl.com/rlmha9k
# Source: https://leetcode.com/problems/count-of-range-sum/discuss/77987/Java-SegmentTree-Solution-36ms/82533
# Approach 1: Prefix-sum + SegmentTree
class SegmentTreeNode(object):
    # This is a binary tree, each node contains a range formed by "minPrefixSum" and "maxPrefixSum".
    # the "minPrefixSum" of a parent node is determined by the minimum lower boundary of all its children
    # the "maxPrefixSum" is determined by the maximum upper boundary of all its children.
    # And remember, the boundary value must be a sum of a certain range(i, j). And values between
    # minPrefixSum and maxPrefixSum may not corresponding to a valid prefixSum;
    # This node also contains a "subRangeCount" property which marks how many sub ranges under this node.
    def __init__(self, minPrefixSum, maxPrefixSum):
        self.minPrefixSum = minPrefixSum
        self.maxPrefixSum = maxPrefixSum
        self.subRangeCount = 0 #  "subRangeCount" property marks how many sub ranges under this node.
        self.leftNode = None
        self.rightNode = None

class Solution(object):
    def createSegmetTree(self, prefixSum, prefixSumRangeStartIdx, prefixSumRangeEndIdx):
        currentRoot = SegmentTreeNode(prefixSum[prefixSumRangeStartIdx], prefixSum[prefixSumRangeEndIdx])
        if prefixSumRangeStartIdx == prefixSumRangeEndIdx:
            return currentRoot

        prefixSumRangeMidIdx = (prefixSumRangeStartIdx + prefixSumRangeEndIdx) // 2
        currentRoot.leftNode = self.createSegmetTree(prefixSum, prefixSumRangeStartIdx, prefixSumRangeMidIdx)
        currentRoot.rightNode = self.createSegmetTree(prefixSum, prefixSumRangeMidIdx + 1, prefixSumRangeEndIdx)
        return currentRoot

    def update(self, rootNode, prefixSumValue):
        if not rootNode:
            return
        if rootNode.minPrefixSum <= prefixSumValue <= rootNode.maxPrefixSum:
            rootNode.subRangeCount += 1
            self.update(rootNode.leftNode, prefixSumValue)
            self.update(rootNode.rightNode, prefixSumValue)

    def query(self, rootNode, minPrefixSumQueryRange, maxPrefixSumQueryRange):
        if (minPrefixSumQueryRange <= rootNode.minPrefixSum) and (maxPrefixSumQueryRange >= rootNode.maxPrefixSum): # Queried range completely overlapped
            return rootNode.subRangeCount
        if (maxPrefixSumQueryRange < rootNode.minPrefixSum) or (minPrefixSumQueryRange > rootNode.maxPrefixSum): # Queried range does't have any overlapping
            return 0
        return self.query(rootNode.leftNode, minPrefixSumQueryRange, maxPrefixSumQueryRange) + self.query(rootNode.rightNode, minPrefixSumQueryRange, maxPrefixSumQueryRange)

    # prefix-sum + SegmentTree | O(nlogn)
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        prefixSums = [0]
        for num in nums:
            prefixSums.append(prefixSums[-1] + num)

        # Removing the duplicates, because what really matters is the range of sum. So duplicates has no use at all.
        # prefixSums now contains all sum of range(i, j) where i = 0 and j from 0 to nums.length - 1
        # You must sort here. Because we are going to extract the range of sum. Or, you will Orz
        prefixSums = sorted(list(prefixSums))
        rootNode = self.createSegmetTree(prefixSums, 0, len(prefixSums) - 1)

        count = 0
        for prefixSum in prefixSums:
            minPrefixSumQueryRange = prefixSum - upper
            maxPrefixSumQueryRange = prefixSum - lower
            count += self.query(rootNode, minPrefixSumQueryRange, maxPrefixSumQueryRange)
            self.update(rootNode, prefixSum)

        return count
