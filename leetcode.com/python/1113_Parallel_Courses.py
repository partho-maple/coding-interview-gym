from collections import deque
class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        courseTaken, semesterCount = [], 0

        # a. initialise the graph
        inDegree = {}
        graph = {}
        for i in range(1, N + 1):
            inDegree[i] = 0
            graph[i] = []

        # b. build graph
        for relation in relations:
            courseX, courseY = relation[0], relation[1]
            graph[courseX].append(courseY)
            inDegree[courseY] += 1

        # c. find all sources. all vertices with 0 inDegree
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. check for cycle. If we don't have any source course to start then there is a cycle and we are not ale to finish the courses
        courseCountForThisSemester = 0
        if len(sources) > 0:
            semesterCount += 1
            courseCountForThisSemester = len(sources)
        else:
            return -1

        # d. For each source, add it to the courseTaken and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        while sources:
            if courseCountForThisSemester <= 0: # We have taken all the course of this semester
                semesterCount += 1          # Start of a new semester
                courseCountForThisSemester = len(sources)  # Course we can take o the new semester that we are going to start

            courseCountForThisSemester -= 1  # take a course on this semester
            vertex = sources.popleft()
            courseTaken.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        if len(courseTaken) != N: # We were not able to take all the course because of a cyclic dependency
            return -1

        return semesterCount
