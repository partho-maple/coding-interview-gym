# https://leetcode.com/problems/fibonacci-number/


class Solution(object):
    def fib(self, N):
        if N == 0:
            return 0
        last_two = [1, 1]
        counter = 3
        while counter <= N:
            next_fib = last_two[0] + last_two[1]
            last_two[0] = last_two[1]
            last_two[1] = next_fib
            counter += 1
        return last_two[1] if N > 1 else last_two[0]
