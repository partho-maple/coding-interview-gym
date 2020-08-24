class Solution {
    func groupStrings(_ strings: [String]) -> [[String]] {
        var groupMap = [String:[String]]()
        strings.forEach { string in
            let patttern = getPatternKey(string)
            groupMap[patttern, default: [String]()] += [string]
        }
        return Array(groupMap.values)
    }
    
    func getPatternKey(_ string: String) -> String {
        let asciiValues = string.unicodeScalars.map({ Int($0.value) })
        let diffValue = asciiValues.map({ (26 + $0 - asciiValues[0]) % 26 })
        return diffValue.reduce("", { $0 + " \($1)" })
    }
}
