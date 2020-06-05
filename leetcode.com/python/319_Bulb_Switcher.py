# My Initial solution. Got TLE offcourse
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [False] * n
        for i in range(1, n + 1):
            currentBuldIdx = 0
            while currentBuldIdx < n:
                currentBuldIdx += i
                if currentBuldIdx - 1 < n:
                    bulbs[currentBuldIdx - 1] = not bulbs[currentBuldIdx - 1]
                else:
                    break

        count = 0
        for bulb in bulbs:
            if bulb:
                count += 1
        return count


"""
[0, 0, 0]
n**2
"""




class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))