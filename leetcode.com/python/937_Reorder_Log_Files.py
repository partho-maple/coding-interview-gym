import re

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letterLogs = []
        digitLogs = []
        for log in logs:
            _id, words = log.split(' ')[:2]
            if words[0].isalpha():
                letterLogs.append((log, log.replace(_id + ' ', '') + ' ' + _id))
            else:
                digitLogs.append(log)
        letterLogs = [x[0] for x in sorted(letterLogs, key=lambda x: x[1])]
        return letterLogs + digitLogs


sol = Solution()
logFiles = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
sortedLogFiles = sol.reorderLogFiles(logFiles)
print("Sorted Files: ", sortedLogFiles)

