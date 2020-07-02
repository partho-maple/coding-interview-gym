import Foundation

class TrieNode {
    var children = [Character: TrieNode]()
    var isWord = false
}

class Trie {
    var root = TrieNode()
    
    func insert(_ word: String) {
        var node = self.root
        for char in word {
            guard let curNode = node.children[char] else {
                node.children[char] = TrieNode()
            }
            node = curNode
        }
        node.isWord = true
    }
    
    func search(_ word: String) -> Bool {
        var node = self.root
        for char in word {
            guard let curNode = node.children[char] else {
                return false
            }
            node = curNode
        }
        return node.isWord
    }
}

class Solution {
    func findWords(_ board: [[Character]], _ words: [String]) -> [String] {
        var presentWords = [String]()
        var trie = Trie()
        var node = trie.root
        for word in words {
            trie.insert(word)
        }
        var copyBoard = board
        for i in 0..<board.count {
            for j in 0..<board[0].count {
                dfsWordSearch(&copyBoard, &node, i, j, [], &presentWords)
            }
        }
        return presentWords
    }
    
    func dfsWordSearch(_ board: inout [[Character]], _ currentNode: inout TrieNode, _ i: Int, _ j: Int, _ currentPath: [Character], _ foundWords: inout [String]) {
        if currentNode.isWord {
            foundWords.append(currentPath.reduce(into: "", { $0 + String($1) }))
            currentNode.isWord = false
        }
        if i < 0 || i >= board.count || j < 0 || j >= board[0].count {
            return
        }
        var currChar = board[i][j]
        guard currentNode = currentNode.children[currChar] else {
            return
        }
        board[i][j] = Character("#")
        dfsWordSearch(&board, &currentNode, i + 1, j, currentPath + [currChar], &foundWords)
        dfsWordSearch(&board, &currentNode, i - 1, j, currentPath + [currChar], &foundWords)
        dfsWordSearch(&board, &currentNode, i, j + 1, currentPath + [currChar], &foundWords)
        dfsWordSearch(&board, &currentNode, i, j - 1, currentPath + [currChar], &foundWords)
        board[i][j] = currChar
    }
}
