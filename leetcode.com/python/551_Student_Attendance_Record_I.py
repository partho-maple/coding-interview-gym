class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absentCount = 0
        lateCount = 0
        for char in s:
            if char == 'A':
                absentCount += 1
                lateCount = 0
            elif char == 'L':
                lateCount += 1
            else:
                lateCount = 0
            if absentCount > 1 or lateCount > 2:
                return False
        return True



