import calendar


class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        monthDayDict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31,
                        '11': 30, '12': 31}
        days = monthDayDict[str(M)]
        if M == 2 and calendar.isleap(Y):
            days = 29

        return days
