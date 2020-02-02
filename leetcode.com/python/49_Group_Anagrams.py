# My initial solution. 100 / 101 test cases passed. Got wrong answer on the  last  test  case:  https://tinyurl.com/wfbeu8w
from collections import Counter
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seenMap = defaultdict(bool)
        resultMap = defaultdict(list)
        counterArr = []
        for currStr in strs:
            counter = Counter(currStr)
            counterArr.append(counter)
        for i in range(len(strs)):
            str1 = strs[i]
            counter1 = counterArr[i]
            if not seenMap[str1]:
                resultMap[str1].append(str1)
                seenMap[str1] = True
            else:
                continue
            for j in range(i + 1, len(counterArr)):
                str2 = strs[j]
                counter2 = counterArr[j]
                if not seenMap[str2]:
                    if counter1 == counter2:
                        resultMap[str1].append(str2)
                        seenMap[str2] = True
                elif str1 == str2:
                    resultMap[str2].append(str2)
        return resultMap.values()




from collections import Counter
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        resultMap = defaultdict(list)
        for s in strs:
            # resultMap[tuple(sorted(s))].append(s)
            resultMap[''.join(sorted(s))].append(s)
        return resultMap.values()