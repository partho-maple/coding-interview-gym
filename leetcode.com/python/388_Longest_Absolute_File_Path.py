class Solution(object):
    def lengthLongestPath(self, input):
        maxPath = 0
        paths = [0]
        for subDir in input.splitlines():

            # getting the depth level of the current subpath
            level = subDir.count('\t')

            # increasing the size of the array of the parents subpaths, if needed
            if level >= len(paths):
                paths += [None]

            # updating the length of the current depth level
            if level > 0:
                paths[level] = paths[level - 1] + (len(subDir) - level) + 1
            else:
                paths[level] = len(subDir)

            # updating the maximum length
            if '.' in subDir:
                maxPath = max(maxPath, paths[level])

        return maxPath