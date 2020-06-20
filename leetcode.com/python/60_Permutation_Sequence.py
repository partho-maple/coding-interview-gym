class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: (5040), 8: (40320), 9: (362880)}
        digits = [str(x) for x in range(1, n + 1)]

        number = []
        currentDigitCount = 1
        currentK = k - 1

        while currentDigitCount < n:
            chosenDigitIndex, currentK = divmod(currentK, factorial[n - currentDigitCount])
            number.append(digits.pop(chosenDigitIndex))
            currentDigitCount += 1

        number.append(digits[0])
        return ''.join(number)