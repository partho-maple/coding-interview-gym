class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        newS = list(S)
        for idx, source, target in zip(indexes, sources, targets):
            if not S[idx:].startswith(source):
                continue
            else:
                newS[idx] = target
                for i in range(idx + 1, idx + len(source)):
                    newS[i] = ""
        return "".join(newS)





