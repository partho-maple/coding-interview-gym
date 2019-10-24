import collections
import bisect

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.internalMap = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.internalMap[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        valueList = self.internalMap.get(key, None)
        if valueList is None:
            return ""
        i = bisect.bisect(valueList, (timestamp, chr(127)))
        return valueList[i - 1][1] if i else ""

# Your TimeMap object will be instantiated and called as such:
kv = TimeMap()
kv.set("foo", "bar", 1); # store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  # output "bar"
kv.get("foo", 3); # output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); # output "bar2"
kv.get("foo", 5); # output "bar2"