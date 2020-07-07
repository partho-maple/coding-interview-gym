import Foundation
// Source: https://tinyurl.com/ycotov9v
class Solution {
    func isNumber(_ s: String) -> Bool {
        var (metDot, metE, metDigit) = (false, false, false)
        let stringArray: [Character] = Array(s.trimmingCharacters(in: .whitespaces))
        print("stringArray: \(stringArray)")
        for (index, char) in stringArray.enumerated() {
            print("-----NEW CHAR: \(char)-----")
            if ["+", "-"].contains(char) {
                if index > 0 && stringArray[index - 1] != "e" {
                    print("1")
                    return false
                }
            }
            else if char == "." {
                if metDot || metE {
                    print("2")
                    return false
                }
                metDot = true
            }
            else if char == "e" {
                if metE || !metDigit {
                    print("3")
                    return false
                }
                metE = true
                metDigit = false // resetting digit, because after e, e need only digit
            }
            else if char.isWholeNumber {
                print("isNumber")
                metDigit = true
            }
            else {
                print("4")
                return false
            }
        }
        print("5")
        return metDigit
    }
}
