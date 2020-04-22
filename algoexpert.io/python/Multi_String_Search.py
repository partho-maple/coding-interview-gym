#   Solution 02
#   O(b^2 + ns) time | O(b^2 + n) space
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
    return [modifiedSuffixTrie.conntains(string) for string in smallStrings]

class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateModifiedSuffixTrieFrom(string)

    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartinngAt(i, string)

    def insertSubstringStartinngAt(self, idx, string):
        node = self.root
        for j in range(idx, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def conntains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True


#   Solution 03
#   O(bs + ns) time | O(ns) space
def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    containedString = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedString)
    return [string in containedString for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStringns):
    currentNode = trie.root
    for i in range(startIdx, len(string)):
        currentChar = string[i]
        if currentChar not in currentNode:
            break
        currentNode = currentNode[currentChar]
        if trie.endSymbol in currentNode:
            containedStringns[currentNode[trie.endSymbol]] = True

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = '*'

    def insert(self, string):
        current = self.root
        for i in range(len(string)):
            if string[i] not in current:
                current[string[i]] = {}
            current = current[string[i]]
        current[self.endSymbol] = string

