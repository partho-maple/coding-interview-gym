from collections import defaultdict


class Solution(object):

    def numMatchingSubseq(self, S, words):
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])




sol = Solution()
S = "abcde"
words = ["a", "bb", "acd", "ace"]
out = sol.numMatchingSubseq(S, words)
print('Res: ', out)