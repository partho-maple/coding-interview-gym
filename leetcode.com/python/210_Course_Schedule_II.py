from collections import deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        sortedOrder = []
        if numCourses <= 0:
            return sortedOrder

        # a. Initialize the graph
        inDegree = {i: 0 for i in range(numCourses)}  # count of incoming edges
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[1], prerequisite[
                0]  # according to the prolem statement, 1st element will be child and second one will e parent
            graph[parent].append(child)  # put the child into it's parent's list
            inDegree[child] += 1  # increment child's inDegree

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
        # will not be able to schedule all tasks
        if len(sortedOrder) != numCourses:
            return []

        return sortedOrder



