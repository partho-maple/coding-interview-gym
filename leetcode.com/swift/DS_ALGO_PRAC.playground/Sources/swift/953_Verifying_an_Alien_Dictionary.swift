import Foundation

class Solution {
    func isAlienSorted(_ words: [String], _ order: String) -> Bool {
        guard words.count > 1 else {
            return true
        }
        var letterIdxMap = [Character:Int]()
        letterIdxMap[Character("#")] = -1
        for (index, item) in order.enumerated(){
            letterIdxMap[item] = index
        }
        for i in 1..<words.count {
            let previousWord: [Character] = Array(words[i - 1])
            let currentWord: [Character] = Array(words[i])
            var charIdx = -1
            while charIdx < max(previousWord.count, currentWord.count) {
                charIdx += 1
                let prevChar = charIdx < previousWord.count ? previousWord[charIdx] : Character("#")
                let currChar = charIdx < currentWord.count ? currentWord[charIdx] : Character("#")
                if prevChar == currChar {
                    continue
                }
                if letterIdxMap[prevChar] ?? -1 > letterIdxMap[currChar] ?? -1 {
                    return false
                } else {
                    break
                }
            }
        }
        return true
    }
}
