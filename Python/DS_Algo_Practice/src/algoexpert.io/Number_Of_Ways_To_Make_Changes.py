# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change


# O(nd) time | O(n) space
# Where, 'n' is amount and 'd' is number of denominators
def number_of_ways_to_make_change(n, denoms):
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]

