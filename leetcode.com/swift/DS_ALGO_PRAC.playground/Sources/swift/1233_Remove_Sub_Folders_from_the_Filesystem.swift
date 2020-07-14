import Foundation

// Brute force solution. Time O(n*n*l). Time limit exceed. 27 / 31 test cases passed.
class Solution {
    func removeSubfolders(_ folder: [String]) -> [String] {
        guard folder.count > 1 else {
            return folder
        }
        var sortedFolder = folder.sorted { $0.count < $1.count }
        
        var parentFolderIdx = 0
        while parentFolderIdx < sortedFolder.count - 1 {
            let parentFolder = sortedFolder[parentFolderIdx] + "/"
            var subFolderIdx = parentFolderIdx + 1
            while subFolderIdx < sortedFolder.count {
                let subFolder = sortedFolder[subFolderIdx] + "/"
                if subFolder.starts(with: parentFolder) {
                    sortedFolder.remove(at: subFolderIdx)
                } else {
                    subFolderIdx += 1
                }
            }
            parentFolderIdx += 1
        }
        return sortedFolder
    }
}


// Using Trie
public class TrieNode {
    public var value: String?
    public var children = [Character:TrieNode]()
    public var isEnd: Bool = false
}

public class Trie {
    public var root = TrieNode()
    
    @discardableResult
    func insert(_ folderName: String) -> Bool {
        var currentNode = self.root
        for char in folderName {
            if currentNode.children[char] == nil {
                currentNode.children[char] = TrieNode()
            }
            currentNode = currentNode.children[char]!
        }
        currentNode.value = folderName
        currentNode.isEnd = true
        return currentNode.isEnd
    }
    
    func contains(_ folderName: String) -> Bool {
        var currentNode = self.root
        for char in folderName {
            guard var nextNode = currentNode.children[char] else {
                return false
            }
            if nextNode.isEnd && char == Character("/"){
                return  nextNode.isEnd
            }
            currentNode = nextNode
        }
        return false
    }
}

class Solution {
    func removeSubfolders(_ folder: [String]) -> [String] {
        guard folder.count > 1 else {
            return folder
        }
        var sortedFolder = folder.sorted { $0.localizedCaseInsensitiveCompare($1) == ComparisonResult.orderedAscending }
        sortedFolder = sortedFolder.sorted { $0.count < $1.count }
        var trie = Trie()
        var result = Set<String>()
        for folder in sortedFolder {
            if !trie.contains(folder) {
                trie.insert(folder + "/")
                result.insert(folder)
            }
        }
        return Array(result)
    }
}
