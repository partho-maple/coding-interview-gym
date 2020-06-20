class Solution {
    func getPermutation(_ n: Int, _ k: Int) -> String {
        let factorialDict: [Int:Int] = [1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880]
        var digits = Array(1...n)
        
        var numbers = [Int]()
        var currentK = k - 1
        
        while digits.count > 0 {
            var (chosenDigitIndex, currentK) = currentK.quotientAndRemainder(dividingBy: factorialDict[numbers.count + 1])
            numbers.append(digits.remove(at: chosenDigitIndex))
        }
        numbers.append(digits[0])
        let result = numbers.map { String($0) }
        return result.joined(separator: "")
    }
}
