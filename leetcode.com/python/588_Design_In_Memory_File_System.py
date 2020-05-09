class TrieNode:
    def __init__(self):
        self.children = {}
        self.childDirSet = set()
        self.name = None
        self.fileContent = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.endSymbol = "/"

    def addFileContentToPath(self, path, content):
        currentNode = self.root
        directories = path.split("/")
        for i in range(1, len(directories)):
            directorie = directories[i]
            currentNode.childDirSet.add(directorie)
            for char in directorie:
                if char not in currentNode.children:
                    currentNode.children[char] = TrieNode()
                currentNode = currentNode.children[char]
            currentNode.name = directorie
        if content:
            currentNode.childDirSet.add(currentNode.name)
            currentNode.fileContent += content

    def addPath(self, path):
        self.addFileContentToPath(path, None)

    def readContentFromPath(self, path):
        currentNode = self.getLastNode(path)
        return currentNode.fileContent

    def getCurrentDirContent(self, path):
        currentNode = self.getLastNode(path)
        dirList = list(currentNode.childDirSet)
        dirList.sort()
        return dirList

    def getLastNode(self, path):
        currentNode = self.root
        directories = path.split("/")
        for i in range(1, len(directories)):
            currentDir = directories[i]
            for char in currentDir:
                currentNode = currentNode.children[char]
        return currentNode


class FileSystem(object):

    def __init__(self):
        self.trie = Trie()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        return self.trie.getCurrentDirContent(path)

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        self.trie.addPath(path)

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        self.trie.addFileContentToPath(filePath, content)

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.trie.readContentFromPath(filePath)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)