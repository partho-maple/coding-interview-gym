#   Solution 01:
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.inputKeyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])

    def addRecord(self, sentence, hotness):
        currentNode = self.root
        for char in sentence:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.isEnd = True
        currentNode.data = sentence
        currentNode.rank -= hotness  # The reason for making it negative is, becasue 'rank' later uses sorted() on the tuples. But we need to sort assending for senetce and descending for rank. So by negating the rank, it can easily just sort assending as the default for sorted is.

    def dfs(self, root):
        results = []
        if root:
            if root.isEnd:
                results.append((root.rank, root.data))
            for child in root.children:
                results.extend(self.dfs(root.children[child]))
        return results

    def search(self, sentence):
        currentNode = self.root
        for char in sentence:
            if char not in currentNode.children:
                return []
            currentNode = currentNode.children[char]
        return self.dfs(currentNode)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        results = []
        if c != "#":
            self.inputKeyword += c
            results = self.search(self.inputKeyword)
        else:
            self.addRecord(self.inputKeyword, 1)
            self.inputKeyword = ""
        return [item[1] for item in sorted(results)[:3]]  # First 3 items which is sentence, sorted by rank



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)



