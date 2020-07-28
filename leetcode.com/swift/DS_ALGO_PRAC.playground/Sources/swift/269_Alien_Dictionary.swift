import Foundation
class Solution {
    func alienOrder(_ words: [String]) -> String {
        guard words.count > 1 else {
            return words.first ?? ""
        }
        
        var graph = [Character:[Character]]()
        var inDegree = [Character:Int]()
        for word in words {
            for char in word {
                graph[char] = [Character]()
                inDegree[char] = 0
            }
        }
        
        for i in 1..<words.count {
            let prevWordArr: [Character] = Array(words[i - 1])
            let currWordArr: [Character] = Array(words[i])
            for (prevCh, currCh) in zip(prevWordArr, currWordArr) {
                if prevCh == currCh {
                    continue
                } else {
                    graph[prevCh]!.append(currCh)
                    inDegree[currCh]! += 1
                    break
                }
            }
        }
        
        var sources = [Character]()
        for key in inDegree.keys {
            if inDegree[key] == 0 {
                sources.append(key)
            }
        }
        
        var order = [Character]()
        while sources.count > 0 {
            let nodeChar = sources.removeFirst()
            order.append(nodeChar)
            for neighbour in graph[nodeChar]! {
                inDegree[neighbour]! -= 1
                if inDegree[neighbour]! == 0 {
                    sources.append(neighbour)
                }
            }
            graph.removeValue(forKey: nodeChar)
        }
        return order.count != inDegree.keys.count ? "" : order.reduce("", { $0 + String($1)})
    }
}
