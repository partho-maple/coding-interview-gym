from collections import deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 0:
            return ""

        # a. Initialize the graph
        inDegree = {}                                           # count of incoming edges
        graph = {}                                              # adjacency list graph
        for word in words:
            for character in word:
                inDegree[character] = 0
                graph[character] = []

        # b. Build the graph
        for i in range(0, len(words) - 1):
            # find ordering of characters from adjacent words
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                parent, child = word1[j], word2[j]
                if parent != child:                             # if the two characters are different
                    graph[parent].append(child)                 # put the child into it's parent's list
                    inDegree[child] += 1                        # increment child's inDegree
                    break                                       # only the first different character between the two words will help us find the order

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        sortedOrder = []
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:                         # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
        # will not be able to find the correct ordering of the characters
        if len(sortedOrder) != len(inDegree):
            return ""

        return "".join(sortedOrder)





