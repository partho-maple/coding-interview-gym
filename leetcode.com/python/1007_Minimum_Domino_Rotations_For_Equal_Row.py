# Source: https://tinyurl.com/v3zqer7
# Approach 1
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        result = float("inf")
        for domino in range(1, 7):  # Since each domino can have only 1 to 6 values. So check all values if we can make it
            isPossible = True
            topRorationCount, bottomRotationCount = 0, 0
            for a, b in zip(A, B):
                if domino != a and domino != b: #
                    isPossible = False
                    break
                if domino == a and domino != b:
                    bottomRotationCount += 1
                elif domino != a and domino == b:
                    topRorationCount += 1
            if isPossible:
                result = min(result, min(topRorationCount, bottomRotationCount))
        return -1 if result == float("inf") else result



# Source: https://tinyurl.com/v3zqer7
# Approach 2
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        rotations = self.checkRotationFor(A, B, A[0])
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations
        # If one could make all elements in A or B equal to B[0]
        else:
            return self.checkRotationFor(A, B, B[0])

    def checkRotationFor(self, A, B, num):
        """
        Return minimum number of swaps,
        if one could make all elements in A or B equal to 'num'.
        Else return -1
        """
        # How many rotations should be done
        # to have all elements in A equal to 'num'
        # and to have all elements in B equal to 'num'
        length = len(A)
        rotations_A, rotations_B = 0, 0
        for i in range(length):
            if A[i] != num and B[i] != num:
                return -1
            elif A[i] != num:
                rotations_A += 1
            elif B[i] != num:
                rotations_B += 1
        return min(rotations_A, rotations_B)


