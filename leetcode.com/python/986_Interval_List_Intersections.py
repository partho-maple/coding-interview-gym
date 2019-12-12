class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        mergedIntervals = []
        indexA, indexB, start, end = 0, 0, 0, 1
        while indexA < len(A) and indexB < len(B):
            a_overlaps_b = A[indexA][start] >= B[indexB][start] and A[indexA][start] <= B[indexB][end]          # check if intervals overlap and A[indexA]'s start time lies within the other B[indexB]
            b_overlaps_a = B[indexB][start] >= A[indexA][start] and B[indexB][start] <= A[indexA][end]          # check if intervals overlap and B[indexB]'s start time lies within the other A[indexA]
            if a_overlaps_b or b_overlaps_a:                                                                    # store the the intersection part
                newStart = max(A[indexA][start], B[indexB][start])                                              # find the start of overlapped part
                newEnd =   min(A[indexA][end], B[indexB][end])                                                  # find the end of overlapped part
                mergedIntervals.append([newStart, newEnd])
            if A[indexA][end] < B[indexB][end]:                                                                 # move next from the interval which is finishing first
                indexA += 1
            else:
                indexB += 1
        return mergedIntervals

