import itertools
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        sequeces = []
        for i in range(len(tiles)):
            sequeces.extend(list(itertools.permutations(tiles, i + 1)))
        return len(set(sequeces))