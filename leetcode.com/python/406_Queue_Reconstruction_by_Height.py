class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for i in people:
            output.insert(i[1], i)
        return output



sol = Solution()
input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
output = sol.reconstructQueue(input)
print("Res:  ", output)
