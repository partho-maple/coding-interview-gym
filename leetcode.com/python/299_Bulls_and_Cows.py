from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secretCounter = Counter(secret)
        guessCounter = Counter(guess)
        bulls, cows = 0, 0
        for guessDigit in guessCounter.keys(): #    First get all the 'cows'. If you have cows then you may or may not have the bulls. So later you can convert the cows into bulls
            if secretCounter[guessDigit] > 0:
                cows += min(guessCounter[guessDigit], secretCounter[guessDigit])
        if cows > 0:
            for secretDigit, guessDigit in zip(secret, guess): # Convert the cows into bulls
                if secretDigit == guessDigit:
                    cows -= 1
                    bulls += 1
        return '%sA%sB' % (bulls, cows)
