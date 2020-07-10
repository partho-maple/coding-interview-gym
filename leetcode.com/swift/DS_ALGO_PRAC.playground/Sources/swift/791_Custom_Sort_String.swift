import Foundation
class Solution {
    func customSortString(_ S: String, _ T: String) -> String {
        var tCounter = [Character: Int]()
        for character in T {
            tCounter[character, default: 0] += 1
        }
        
        var result = ""
        for character in S {
            if var count = tCounter[character] {
                while count > 0 {
                    result += String(character)
                    count -= 1
                }
                tCounter.removeValue(forKey: character)
            }
        }
        
        for character in tCounter.keys {
            if var count = tCounter[character] {
                while count > 0 {
                    result += String(character)
                    count -= 1
                }
            }
        }
        return result
    }
}
