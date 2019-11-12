
# # My initial solution, which is wrong.
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         days = len(prices)
#         if days < 2:
#             return 0
#         totalProfit = 0
#         isCoolingDown = False
#         minimumPrice = prices[0]
#         for today in range(1, days):
#             if prices[today] < minimumPrice:
#                 minimumPrice = prices[today]
#                 isCoolingDown = False
#             elif minimumPrice < prices[today]:
#                 if not isCoolingDown:
#                     totalProfit += (prices[today] - minimumPrice)
#                     minimumPrice = prices[today]
#                     isCoolingDown = True
#                 else:
#                     isCoolingDown = False
#             else:
#                 isCoolingDown = False
#         return totalProfit


# Taken from this (Must read):  https://tinyurl.com/wlol23f   and   https://tinyurl.com/syuepe6
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        have_1_stock_and_sell = 'have 1 stock and sell'
        have_1_stock_and_keep = 'have 1 stock and keep'
        have_0_stock_and_buy = 'have 0 stock and buy'
        have_0_stock_and_rest = 'have 0 stock and rest'

        # The keys of this dictionary is the action taken on 'i'th day and the values represent the possible actions on the 'i + 1' day.
        action_to_next_day_possible_actions = {
            have_1_stock_and_sell: {have_0_stock_and_rest},  # Cool-down.
            have_1_stock_and_keep: {have_1_stock_and_keep, have_1_stock_and_sell},
            have_0_stock_and_buy: {have_1_stock_and_keep, have_1_stock_and_sell},
            have_0_stock_and_rest: {have_0_stock_and_rest, have_0_stock_and_buy},
        }

        # We initialize with the possible actions for the first day.
        possible_actions = [{have_0_stock_and_buy: 0, have_0_stock_and_rest: 0}]

        def set_max_action_to_gain(_today_actions_to_total_gain, _today_action, _previous_day_total_gain,
                                   _today_gain=0):
            if _today_action in _today_actions_to_total_gain:
                different_previous_action_today_gain = _today_actions_to_total_gain[_today_action]
                _today_actions_to_total_gain.update({_today_action: max(_previous_day_total_gain + _today_gain,
                                                                        different_previous_action_today_gain)})
            else:
                _today_actions_to_total_gain.update({_today_action: _previous_day_total_gain + _today_gain})

        # Start with the second day, compare all actions possible on the second day based on the possible actions of
        # the first day.
        i = 1
        while i < len(prices):

            today_actions_to_total_gain = dict()
            today_gain = prices[i] - prices[i - 1]

            for previous_day_action, previous_day_total_gain in possible_actions[-1].items():

                for today_action in action_to_next_day_possible_actions[previous_day_action]:

                    if previous_day_action == have_1_stock_and_sell:
                        # If we sold yesterday, we have to rest there, so no gain for today.
                        set_max_action_to_gain(today_actions_to_total_gain, today_action, previous_day_total_gain)

                    elif previous_day_action == have_1_stock_and_keep:
                        # Whether we keep or sell, the gain is the same:
                        set_max_action_to_gain(today_actions_to_total_gain, today_action, previous_day_total_gain,
                                               today_gain)

                    elif previous_day_action == have_0_stock_and_buy:
                        # In both cases, have_1_stock_and_keep and have_1_stock_and_sell would yield to the same gain:
                        set_max_action_to_gain(today_actions_to_total_gain, today_action, previous_day_total_gain,
                                               today_gain)

                    elif previous_day_action == have_0_stock_and_rest:
                        # In this case, the gain is 0 because we don't hold any stock, whether we rest or buy on this
                        # day.
                        set_max_action_to_gain(today_actions_to_total_gain, today_action, previous_day_total_gain)

            possible_actions.append(today_actions_to_total_gain)
            i += 1

        last_possible_actions = possible_actions[-1]
        print('last possible actions', last_possible_actions)

        return max(last_possible_actions.values())





sol = Solution()
prices = [1,2,4]
profit = sol.maxProfit(prices)
print("Profit: ", profit)


