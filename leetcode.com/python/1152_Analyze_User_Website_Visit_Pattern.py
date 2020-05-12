from collections import defaultdict
from itertools import combinations
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        packed_tuple = zip(timestamp, username, website)  # ---> [(3, 'joe', 'career'),....]
        sorted_packed_tuple = sorted(packed_tuple)  # sort by timestamp (By default tuple always sorted by first item )

        user_site_mapping = defaultdict(list)
        for t, u, w in sorted_packed_tuple:  # joe: [home, about, career]  websites in list are in ascending timestamp order
            user_site_mapping[u].append(w)

        site_combination_counter = defaultdict(int)  # use a dict for counting the website visiting of for each user
        for website_list_of_each_user in user_site_mapping.values():
            combs = set(combinations(website_list_of_each_user, 3)) # combinations will be in sorted order as input list
            for comb in combs:
                site_combination_counter[comb] += 1  # Tuple as key, counter as value,  e.g. ('home', 'about', 'career') : 2

        sorted_counter_dict = sorted(site_combination_counter, key=lambda x: (-site_combination_counter[x], x))  # sort descending by value, then lexicographically
        return sorted_counter_dict[0]