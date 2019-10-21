from collections import Counter


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = collections.Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]