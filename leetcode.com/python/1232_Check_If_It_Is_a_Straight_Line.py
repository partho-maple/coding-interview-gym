# https://tinyurl.com/ybhq39ka
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True

        coordinates.sort(key=lambda coord: (coord[0], coord[1]))
        for i in range(1, len(coordinates) - 2):
            prevC = coordinates[i - 1]
            currC = coordinates[i]
            nextC = coordinates[i + 1]
            if not self.inLine(prevC, currC, nextC):
                return False
        return True

    """
 (currC[1]- prevC[1])       (nextC[1]- currC[1])       (nextC[1]- prevC[1]) 
 ---------------------  ==  --------------------  ==   --------------------
 (currC[0]- prevC[0])       (nextC[0]- currC[0])      (nextC[0]- prevC[0])
    """

    def inLine(self, prevC, currC, nextC):
        # slopA = (currC[1]- prevC[1]) / (currC[0]- prevC[0])
        # slopB = (nextC[1]- currC[1]) / (nextC[0]- currC[0])
        if ((currC[1] - prevC[1]) * (nextC[0] - currC[0])) == ((currC[0] - prevC[0]) * (nextC[1] - currC[1])):
            return True
        else:
            return False
