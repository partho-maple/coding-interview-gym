class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = 'aeiou'
        for char in S:
            if char in vowels:
                S = S.replace(char, '')
        return S
