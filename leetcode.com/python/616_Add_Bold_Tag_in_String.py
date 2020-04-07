# Approach 1: Merge intervals
#   Step 1: create a list of tuples/intervals with opening/closing positions, e.g. (open_index, close_index)
#   Step 2: merge the list of intervals (see https://leetcode.com/problems/merge-intervals/)
#   Step 3: go through the merged interval list and insert the tags into the string
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        locations = []
        # generate the word intervals
        for word in dict:
            startIdx = s.find(word)
            while startIdx != -1:  # "s" can contain same word multiple times ad overlapped
                locations.append([startIdx, startIdx + len(word) - 1])
                startIdx = s.find(word, startIdx + 1)

        if not locations:
            return s

        # merge the intervals
        locations.sort(key=lambda x: x[0])
        locationsMerged = []
        startIdx, endIdx = locations[0][0], locations[0][1]
        for i in range(1, len(locations)):
            nextStart, nextEnd = locations[i][0], locations[i][1]
            if nextStart <= endIdx + 1:  # since, if the strings are consequtive
                endIdx = max(endIdx, nextEnd)
            else:
                locationsMerged.append([startIdx, endIdx])
                startIdx, endIdx = nextStart, nextEnd
        locationsMerged.append([startIdx, endIdx])

        # gennerate the old tagged string
        resultStr = ""
        startIdx, endIdx = locationsMerged[0][0], locationsMerged[0][1]
        resultStr += s[0:startIdx]
        for i in range(len(locationsMerged)):
            nextStart, nextEnd = locationsMerged[i][0], locationsMerged[i][1]
            if endIdx < nextStart:
                resultStr += s[endIdx + 1:nextStart]
            strToBold = s[nextStart:nextEnd + 1]
            if strToBold:
                resultStr += "<b>{}</b>".format(strToBold)
            else:
                resultStr += s[endIdx + 1:nextStart]
            startIdx, endIdx = nextStart, nextEnd
        resultStr += s[endIdx + 1:]
        return resultStr