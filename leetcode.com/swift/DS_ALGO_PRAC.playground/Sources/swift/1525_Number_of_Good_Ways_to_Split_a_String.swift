class Solution {
    func numSplits(_ s: String) -> Int {
        guard s.count > 1 else { return 0 }
        
        var (pDict, qDict, gSplitCount) = ([Character:Int](), [Character:Int](), 0)
        var stringArray = Array(s)
        stringArray.forEach { item in
            qDict[item, default: 0] += 1
        }
        for index in 0..<(stringArray.count - 1) {
            pDict[stringArray[index], default: 0] += 1
            qDict[stringArray[index], default: 0] -= 1
            if qDict[stringArray[index]] == 0 {
                qDict.removeValue(forKey:stringArray[index])
            }
            if pDict.keys.count == qDict.keys.count {
                gSplitCount += 1
            }
        }
        return gSplitCount
    }
}
