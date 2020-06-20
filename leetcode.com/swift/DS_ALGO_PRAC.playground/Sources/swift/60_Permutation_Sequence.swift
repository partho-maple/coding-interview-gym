class Solution {
    func getPermutation(_ n: Int, _ k: Int) -> String {
        let factorialDict: [Int:Int] = [1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880]
        var digits = Array(1...n)
        
        var numbers = [String]()
        var currentK = k - 1
        
        while digits.count > 1 {
            guard let nextPurmutationCount = factorialDict[n - numbers.count - 1] else {break}
            var chosenDigitIndex = 0
            (chosenDigitIndex, currentK) = currentK.quotientAndRemainder(dividingBy: nextPurmutationCount)
            numbers.append(String(digits.remove(at: chosenDigitIndex)))
        }
        numbers.append(String(digits[0]))
        return numbers.joined(separator: "")
    }
}
