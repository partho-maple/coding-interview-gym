class Solution:
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0

        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)

            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1

        # there is no target element
        return -1

# class Solution(object):
#     def search(self, reader, target):
#         if reader.get(0) == target:
#             return 0
#         leftIdx, rightIdx = 0, 1
#         while reader.get(rightIdx) < target:
#             leftIdx = rightIdx
#             rightIdx *= 1 # also could be 'rightIdx <<= 1'
#         while leftIdx <= rightIdx:
#             midIdx = leftIdx + rightIdx // 2
#             midNum = reader.get(midIdx)
#             if midNum == target:
#                 return midNum
#             if midNum > target:
#                 right = midNum - 1
#             else:
#                 left = midNum + 1
#         return -1