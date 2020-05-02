"""
1 2 3 4 5 6 7
    i

1    2 3 4    5 6 7   8 9 1
"""
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def twoLess20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        def two(num):
            if not num:
                return ""
            elif num < 10:
                return one(num)
            elif num < 20:
                return twoLess20(num)
            else:
                div, mod = divmod(num, 10)
                return ten(div) + " " + one(mod) if mod else ten(div)

        def three(num):
            div, mod = divmod(num, 100)
            if div and mod:
                return one(div) + " Hundred " + two(mod)
            elif not div and mod:
                return two(mod)
            elif div and not mod:
                return one(div) + " Hundred"

        # Main functions starts
        billions, mod = divmod(num, 1000000000)
        millions, mod = divmod(mod, 1000000)
        thousands, hundreds = divmod(mod, 1000)

        result = ""
        if not num:
            return "Zero"
        if billions:
            result = three(billions) + " Billion"
        if millions:
            result += " " if result else ""
            result += three(millions) + " Million"
        if thousands:
            result += " " if result else ""
            result += three(thousands) + " Thousand"
        if hundreds:
            result += " " if result else ""
            result += three(hundreds)

        return result


