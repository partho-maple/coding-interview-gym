from collections import defaultdict

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(list)

        for i in range(1, N + 1):
            graph[i] = []

        for trustPair in trust:
            parent, child = trustPair
            graph[parent].append(child)

        judges = []
        # Checks for first condition. If someone doesn't trust anyone then he/she is a probable candidate for town judge
        for i in range(1, N + 1):
            if not graph[i] or len(graph[i]) == 0:
                judges.append(i)

        # Violets second conditions. Because there is someone else or noone that doesn't truse the town judge
        if len(judges) != 1:
            return - 1

        # Checking for third condition
        for i in range(1, N + 1):
            childSet = set(graph[i])
            if judges[-1] != i and judges[-1] not in childSet:
                return -1

        return judges[-1]


"""
outDegree/edgeList is 0

"""