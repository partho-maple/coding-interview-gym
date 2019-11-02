class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        answer = []
        self.backtrack(S, "", 0, answer)
        return answer


    def backtrack(self, originalString, path, index, cache):
        if index == len(originalString):
            cache.append(path)
            return
        if originalString[index].isalpha():
            self.backtrack(originalString, path+originalString[index].upper(), index + 1, cache)
            self.backtrack(originalString, path + originalString[index].lower(), index + 1, cache)
        else:
            self.backtrack(originalString, path + originalString[index], index + 1, cache)


