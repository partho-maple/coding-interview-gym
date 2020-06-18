extension Array where Element: Equatable {
    // Remove first collection element that is equal to the given `object`:
    mutating func remove(object: Element) {
        if let index = index(of: object) {
            remove(at: index)
        }
    }
}

public class Solution_3 {
    public func lengthOfLongestSubstring(_ s: String) -> Int {
        let length = s.characters.count
        var stringArray:[Character] = Array(s.characters) as [Character]
        var traversedArray:[Character] = []
        var i = 0, j = 0, ans = 0
        
        while i<length && j<length {
            if !traversedArray.contains(stringArray[j]) {
                traversedArray.append(stringArray[j])
                j += 1
                ans = max(ans, j-i)
            } else {
                traversedArray.remove(object: stringArray[i])
                i+=1
            }
        }
        
        return ans
    }
}
