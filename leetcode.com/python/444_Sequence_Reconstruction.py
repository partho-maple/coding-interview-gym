from collections import deque

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        sortedOrder = []
        if len(org) <= 0:
            return False

        # a. Initialize the graph
        inDegree = {}                                       # count of incoming edges
        graph = {}                                          # adjacency list graph
        for seq in seqs:
            for num in seq:
                inDegree[num] = 0
                graph[num] = []

        # b. Build the graph
        for seq in seqs:
            for idx in range(0, len(seq) - 1):
                parent, child = seq[idx], seq[idx + 1]
                graph[parent].append(child)
                inDegree[child] += 1

        # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
        if len(inDegree) != len(org):
            return False

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        while sources:
            if len(sources) > 1:
                return False                                # more than one sources mean, there is more than one way to reconstruct the sequence
            if org[len(sortedOrder)] != sources[0]:
                return False                                # the next source(or number) is different from the original sequence

            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:                     # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
        return len(sortedOrder) == len(org)




