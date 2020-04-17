class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        nsg = ["2", "3", "4", "5", "7"]
        sg = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        newNum = ""
        for n in num:
            if n in nsg:
                return False
            else:
                newNum += sg[n]
        newNum = newNum[::-1]
        return num == newNum
