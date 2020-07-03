
import Foundation

class TrieNode {
    var children = [Character: TrieNode]()
    var isWord = false
    var word: String?
}

class Trie {
    var root = TrieNode()
    
    func insert(_ word: String) {
        var node = self.root
        for char in word {
            if node.children[char] == nil {
                node.children[char] = TrieNode()
                
            }
            node = node.children[char]!
        }
        node.isWord = true
        node.word = word
    }
}

class Solution {
    func findWords(_ board: [[Character]], _ words: [String]) -> [String] {
        var presentWords = [String]()
        var trie = Trie()
        for word in words {
            trie.insert(word)
        }

        var copyBoard = board
        for i in 0..<board.count {
            for j in 0..<board[0].count {
                dfsWordSearch(&copyBoard, &trie.root, i, j, &presentWords)
            }
        }
        return presentWords
    }
    
    func dfsWordSearch(_ board: inout [[Character]], _ currentNode: inout TrieNode, _ i: Int, _ j: Int, _ foundWords: inout [String]) {
        if currentNode.isWord {
            foundWords.append(currentNode.word!)
            currentNode.isWord = false
        }
        if i < 0 || i >= board.count || j < 0 || j >= board[0].count || board[i][j] == "#" {
            return
        }
        let currChar = board[i][j]
        guard var nextNode = currentNode.children[currChar] else {
            return
        }
        board[i][j] = Character("#")
        for (nexti, nextj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] {
            dfsWordSearch(&board, &nextNode, nexti, nextj, &foundWords)
        }
        board[i][j] = currChar
    }
}
