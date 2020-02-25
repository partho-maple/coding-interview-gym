from collections import defaultdict

# Brute force approach. Time Limit Exceeded. 48 / 64 test cases passed.
class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        numCount = 0
        cache = defaultdict()
        for num in range(1, N + 1):
            isValid, rotatedNum = self.confusingNumberIIHelper(str(num), cache)
            if isValid and int(rotatedNum) != num:
                # print("confusingNumberII num: ", num)
                numCount += 1
        return numCount

    def confusingNumberIIHelper(self, currentNum, cache):
        rules = {"0": "0", "1": "1", "2": "-1", "3": "-1", "4": "-1", "5": "-1", "6": "9", "7": "-1", "8": "8", "9": "6"}
        if currentNum in cache:
            return cache[currentNum]
        firstDigit = currentNum[0:1]
        firstDigitRotated = rules[firstDigit]
        if firstDigitRotated != "-1":
            if len(currentNum) > 1:
                nextDigits = currentNum[1:]
                isValid, nextDigitsRotated = self.confusingNumberIIHelper(nextDigits, cache)
                allDigitRotated = nextDigitsRotated + firstDigitRotated

                # print("----------")
                # print(" firstDigitRotated: ", firstDigitRotated)
                # print(" nextDigitsRotated: ", nextDigitsRotated)
                # print(" allDigitRotated: ", allDigitRotated)
                # print(" currentNum: ", currentNum)
                # print(" isValid: ", isValid)

                cache[currentNum] = (isValid, allDigitRotated if isValid else "-1")
                return cache[currentNum]
            else:
                cache[currentNum] = (True, firstDigitRotated)
                return cache[currentNum]
        else:
            cache[currentNum] = (False, "-1")
            return cache[currentNum]




# https://tinyurl.com/wby5h93
class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        validDigits = [0, 1, 6, 8, 9]
        m = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        def dfs(currentNum, currentNumRotated, digitsInCurrentNum):
            res = 0
            if currentNum != currentNumRotated:
                res += 1

            # add one more digit with currentNum, from the list of valid digits rather than adding all 10 digits (from 0 to 9).
            for digit in validDigits:
                if digit == 0 and currentNum == 0:
                    continue
                nextNum = currentNum*10 + digit
                if nextNum <= N:
                    nextNumRotated = m[digit] * digitsInCurrentNum + currentNumRotated
                    digitsInNextNum = digitsInCurrentNum * 10
                    res += dfs(nextNum, nextNumRotated, digitsInNextNum)
            return res

        return dfs(0, 0, 1)



