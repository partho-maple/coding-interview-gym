class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return path

        stack = []
        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or not directory:
                continue
            else:
                stack.append(directory)

        finalDirectoryPath = "/" + "/".join(stack)
        return finalDirectoryPath

