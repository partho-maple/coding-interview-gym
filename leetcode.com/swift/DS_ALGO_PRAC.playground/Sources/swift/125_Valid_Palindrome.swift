import Foundation
class Solution {
    func isPalindrome(_ s: String) -> Bool {
        guard !s.isEmpty else {
            return true
        }
        let sArr = Array(s)
        var (left, right) = (0, sArr.count - 1)
        while left <= right {
            let (leftChar, rightChar) = (sArr[left].lowercased(), sArr[right].lowercased())
            if leftChar.isEmpty || leftChar == " " || (!Character(leftChar).isLetter && !Character(leftChar).isNumber) {
                left += 1
                continue
            }
            if rightChar.isEmpty || rightChar == " " || (!Character(rightChar).isLetter && !Character(rightChar).isNumber) {
                right -= 1
                continue
            }
            if leftChar == rightChar {
                left += 1
                right -= 1
            } else {
                return false
            }
        }
        return true
    }
}
