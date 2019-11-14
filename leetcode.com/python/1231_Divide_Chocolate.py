class Solution:


    # SOlution borrowed from here: https://tinyurl.com/w9wbcyl
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        """
        The problem asks us to divide the chocolate in a clever way in order to
        maximize the sweetness we can get, since our friends are greedy and
        always take the sweetest chunks. In essence, it is asking for the
        maximum of the minimum sum of continuous subarrays, since we always get
        the least sweet piece, which have the least sweet chunks (minimum sum of
        continuous subarray) as compared to our friend's, and we want to find
        the maximum we can get among all the dividing strategies.
        """

        def divide(target):
            """
            The function divides the given chocolate into a number of pieces, so
            that there must be at least one piece with a total sweetness less
            than or equal to the given target
            """
            # total sweetness of current piece and the number of pieces
            sum_, count = 0, 0
            for l in sweetness:
                # add the sweet level to the total
                sum_ += l
                # if the current piece has a total greater than or equal to the
                # given target, make a cut
                if sum_ >= target:
                    count += 1
                    sum_ = 0
            return count

        # the desired total sweetness must fall in the range from the minimum
        # sweetness to the average sweetness of the (K + 1) pieces - if we are
        # dumb enough to cut the least sweet chunk as a piece by itself, its
        # total sweetness is the sweet level of that single chunk; if we are
        # lucky enough that the sweetness is evenly distributed throughout the
        # chocolate bar, we can make even cuts so we have the same amount of
        # sweetness with our greedy friends. The real life is somewhere in
        # between, and we always hope for the best, so we move towards the
        # lucky side as much as we can
        lo, hi = min(sweetness), sum(sweetness) // (K + 1)
        while lo < hi:
            # try a number in the middle tentatively
            target = (lo + hi + 1) // 2
            # if it results in less than K + 1 chunks, some of our friends
            # cannot get a piece and may get mad, so we decrease the sweetness
            # we get to make our friends happy
            if divide(target) < K + 1:
                hi = target - 1
            # otherwise, we try to increase the sweetness (sneakily) as much as
            # we can right before being exposed...
            else:
                lo = target
        # this is the most we can get before being exposed...
        return lo



sol = Solution()
sweetness = [1,2,3,4,5,6,7,8,9]
K = 5
out = sol.maximizeSweetness(sweetness, K)
print('Res: ', out)