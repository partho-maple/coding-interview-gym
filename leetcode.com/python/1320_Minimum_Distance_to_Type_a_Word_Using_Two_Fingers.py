# https://tinyurl.com/u5fcb3z
# Approach 1: Top-Down DFS with memoization, DP
import string
class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Preprocessing
        alphabet = string.ascii_uppercase
        keyboardDict = {}
        for idx, char in enumerate(alphabet):
            keyboardDict[char] = (idx // 6, idx % 6)
        memo = {}
        return self.minimumDistanceHelper(word, keyboardDict, memo, 0, None, None)


    def minimumDistanceHelper(self, word, keyboard, memo, nextCharPosition, currentFingure1Char, currentFingure2Char):
        if nextCharPosition >= len(word):   # we have processed all the character and we have reached the end
            return 0
        if (nextCharPosition, currentFingure1Char, currentFingure2Char) in memo:
            return memo[(nextCharPosition, currentFingure1Char, currentFingure2Char)]

        choice1 = self.distance(currentFingure1Char, word[nextCharPosition], keyboard) + self.minimumDistanceHelper(word, keyboard, memo, nextCharPosition + 1, word[nextCharPosition], currentFingure2Char) # we  are moving finger 1 here, finger 2 stays still
        choice2 = self.distance(currentFingure2Char, word[nextCharPosition], keyboard) + self.minimumDistanceHelper(word, keyboard, memo, nextCharPosition + 1, currentFingure1Char, word[nextCharPosition]) # we  are moving finger 2 here, finger 1 stays still
        memo[(nextCharPosition, currentFingure1Char, currentFingure2Char)] = min(choice1, choice2)
        return memo[(nextCharPosition, currentFingure1Char, currentFingure2Char)]


    def distance(self, startChar,  destChar, keyboard):
        if startChar is None:
            return 0
        x1, y1 = keyboard[startChar]
        x2, y2 = keyboard[destChar]
        return abs(x1 - x2) + abs(y1 - y2)