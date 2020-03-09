import bisect

# My initial solution. Not correct solution
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = list(time)
        digits.pop(2)
        sortedDigits = sorted(digits)
        for idx in range(len(digits) - 1, -1, -1):
            digit = digits[idx]
            nextPossibleDigitIdx = bisect.bisect_right(sortedDigits, digit)
            if nextPossibleDigitIdx >= len(digits):
                continue
            if idx == 3:
                digits[3] = sortedDigits[nextPossibleDigitIdx]
                break
            elif idx == 2 and int(sortedDigits[nextPossibleDigitIdx]) < 6:
                digits[2] = sortedDigits[nextPossibleDigitIdx]
                break
            elif idx == 1:
                if int(digits[0]) < 2:
                    digits[1] = sortedDigits[nextPossibleDigitIdx]
                    break
                elif int(digits[0]) == 2 and int(sortedDigits[nextPossibleDigitIdx]) < 4:
                    digits[1] = sortedDigits[nextPossibleDigitIdx]
                    break
            elif idx == 0:
                if int(sortedDigits[nextPossibleDigitIdx]) < 3:
                    digits[0] = sortedDigits[nextPossibleDigitIdx]
                    break
                else:
                    digits[1] = digits[0]
                    digits[2] = digits[0]
                    digits[3] = digits[0]
        hours = digits[0:2]
        minuites = digits[2:]
        return "".join(hours) + ":" + "".join(minuites)


# https://tinyurl.com/vupwnhw
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minuite = time.split(":")

        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        digits = sorted(set(hour + minuite))
        twoDigitValues = [a+b for a in digits for b in digits]

        # Check if the next valid minute is within the hour
        minuiteIndex = twoDigitValues.index(minuite)
        if minuiteIndex + 1 < len(twoDigitValues) and twoDigitValues[minuiteIndex + 1] < "60":
            return hour + ":" + twoDigitValues[minuiteIndex + 1]

        # Check if the next valid hour is within the day
        hourIndex = twoDigitValues.index(hour)
        if hourIndex + 1 < len(twoDigitValues) and twoDigitValues[hourIndex + 1] < "24":
            return twoDigitValues[hourIndex + 1] + ":" + twoDigitValues[0]

        # Return the earliest time of the next day
        return twoDigitValues[0] + ":" + twoDigitValues[0]
