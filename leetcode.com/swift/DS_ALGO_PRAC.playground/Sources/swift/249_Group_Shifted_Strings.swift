import Foundation

extension String {
    var patternKey: String {
        let asciiValue = self.unicodeScalars.map {Int($0.value)}
        let diffValue = asciiValue.map {(26 + $0 - asciiValue[0]) % 26}
        print("Diff Valets: \(diffValue)")
        return diffValue.reduce("", {$0 + " \($1)"})
    }
}

class Solution {
    func groupStrings(_ strings: [String]) -> [[String]] {
        var groupMap = [Int:[String]]()
        strings.forEach { string in
            let patttern = string.patternKey
            print(patttern)
            groupMap[patttern] = (groupMap[patttern] ?? [String]()) + [string]
        }
        return Array(groupMap.values)
    }
}
