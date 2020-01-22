# Solution 1
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return unichr(258)
        return unichr(257).join(singleStr.encode('utf-8') for singleStr in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s == unichr(258):
            return []
        return s.split(unichr(257))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))





# Solution 2
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return unichr(258)
        return unichr(257).join(singleStr.encode('utf-8') for singleStr in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s == unichr(258):
            return []
        return s.split(unichr(257))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))