class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        typedIdx = 0
        result = False
        for nameIdx in range(len(name)):
            if typedIdx >= len(typed):
                result = False
            while typedIdx < len(typed):
                if name[nameIdx] == typed[typedIdx]:
                    typedIdx += 1
                    result = True
                    break
                else:
                    typedIdx += 1
                    result = False
        return result