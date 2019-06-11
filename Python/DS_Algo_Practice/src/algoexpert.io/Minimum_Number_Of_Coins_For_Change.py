# https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change

import math


# O(nd) time | O(n) space
# Where, 'n' is amount and 'd' is number of denominators
def min_number_of_coins_for_change(n, denoms):
    num_of_coins = [float(math.inf for amount in range(n + 1))]
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], num_of_coins[amount - denom] + 1)
    return num_of_coins[n] if num_of_coins[n] != float("inf") else -1


input_array = [1, 5, 10]
print("Answer: ", min_number_of_coins_for_change(7, input_array))

