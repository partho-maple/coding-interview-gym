from collections import Counter
# Not Accepted. My initial code
class Solution(object):
    # We can't use Counter here, because the sequence matters.
    # As exmple, take "yyrrrrrjaappoooyybbbebbbbriiiiiyyynnnvvwtwwwwwooeeexxxxxkkkkkaaaaauuuu"
    # Counter will return "Y" = 7. but all 7 y are not consequtive. they are o differet spot. Which will give us the wrong result in this prolem context.
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if len(S) == 0 or len(words) == 0:
            return 0
        counterS = Counter(S)
        wordCount = 0
        for word in words:
            counterWord = Counter(word)
            if counterS.keys() != counterWord.keys():
                continue
            isStretchy = True
            for idx, char in enumerate(counterWord):
                if char not in counterS:
                    isStretchy = False
                    break
                if ((counterS[char] != counterWord[char]) and (counterS[char] < 3)) or (counterS[char] < counterWord[char]):
                    isStretchy = False
                    break
            if isStretchy:
                print("Word: ", word)
                wordCount += 1
        return wordCount


# SOurce: https://tinyurl.com/rzlvfn7 Accepted
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if len(S) == 0 or len(words) == 0:
            return 0
        charsS, counterS = self.counterPreservedBySequence(S)
        wordCount = 0
        for word in words:
            charsWord, counterWord = self.counterPreservedBySequence(word)
            if charsWord == charsS:
                validChars = 0
                for idx, char in enumerate(charsWord):
                    if (counterWord[idx] == counterS[idx]) or ((counterS[idx] >= 3) and (counterS[idx] > counterWord[idx])):
                        validChars += 1
                if validChars == len(charsWord):
                    wordCount += 1
        return wordCount

    def counterPreservedBySequence(self, word):
        if not word:
            return [], []
        chars, counters = [word[0], ], [1, ]
        for i in range(1, len(word)):
            if chars[-1] == word[i]:
                counters[-1] += 1
            else:
                chars.append(word[i])
                counters.append(1)
        return chars, counters




sol = Solution()
S = "yyrrrrrjaappoooyybbbebbbbriiiiiyyynnnvvwtwwwwwooeeexxxxxkkkkkaaaaauuuu"
words = ["yrrjappoyybbeebrriiynvvwwtwwoeexxkauu",
         "yyrjaappoybbeebriynnvvwwtwwooeexkaauu",
         "yrrjaappoybbeebrriyynnvvwwtwwooeexxkaauu"]
out = sol.expressiveWords(S, words)
out2 = sol.expressiveWords(S, words)
print("Res: ", out2)
