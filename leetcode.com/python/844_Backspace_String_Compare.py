# O(N + N)  time |  # O(N + N)  space
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.getOriginalString(S) == self.getOriginalString(T)

    def getOriginalString(self, givenStr):
        originalStr = []
        for char in givenStr:
            if char != "#":
                originalStr.append(char)
            else:
                if originalStr:
                    originalStr.pop()
        return "".join(originalStr)


# O(N + N)  time |  # O(1)  space -- Two Pointer solution
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # use two pointer approach to compare the strings
        idxS = len(S) - 1
        idxT = len(T) - 1
        while idxS >= 0 or idxT >= 0:
            nextIdxS = self.getNextValidCharIndex(S, idxS)
            nextIdxT = self.getNextValidCharIndex(T, idxT)
            if nextIdxS < 0 and nextIdxT < 0:           # reached the end of both the strings
                return True
            if nextIdxS < 0 or nextIdxT < 0:            # reached the end of one of the strings
                return False
            if S[nextIdxS] != T[nextIdxT]:              # check if the characters are equal
                return False
            idxS = nextIdxS - 1
            idxT = nextIdxT - 1
        return True

    def getNextValidCharIndex(self, givenStr, givenIndex):
        backspaceCount = 0
        while givenIndex >= 0:
            if givenStr[givenIndex] == '#':     # found a backspace character
                backspaceCount += 1
            elif backspaceCount > 0:            # a non-backspace character
                backspaceCount -= 1
            else:
                break
            givenIndex -= 1                     # skip a backspace or a valid character
        return givenIndex



# My solution during Leetcode Mock Interview
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sV = []
        for sc in S:
            if sc == "#":
                if sV and len(sV) > 0:
                    sV.pop()
            else:
                sV.append(sc)

        tV = []
        for tc in T:
            if tc == "#":
                if tV and len(tV) > 0:
                    tV.pop()
            else:
                tV.append(tc)

        return "".join(sV) == "".join(tV)