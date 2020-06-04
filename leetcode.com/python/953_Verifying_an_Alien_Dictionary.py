class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        sequences = []
        left = 0
        while left < len(words) - 1:
            firstWord = words[left]
            secondWord = words[left + 1]
            for i in range(max(len(firstWord), len(secondWord))):
                ch1, ch2 = " ", " "
                if i < len(firstWord):
                    ch1 = firstWord[i]
                if i < len(secondWord):
                    ch2 = secondWord[i]
                if ch1 != ch2:
                    sequences.append([ch1, ch2])
                    break
            left += 1

        orderIdxMap = {}
        orderIdxMap[" "] = -1
        for i, char in enumerate(order):
            orderIdxMap[char] = i

        for sequence in sequences:
            ch1, ch2 = sequence
            if orderIdxMap[ch1] > orderIdxMap[ch2]:
                return False

        return True


"""
words >> [[w1,w2],[w2,w3],[w3,w4]]
orders >> map[] # char:idx
 while seqn
    if map[seq[0]] < map[seq[1]]
"""
