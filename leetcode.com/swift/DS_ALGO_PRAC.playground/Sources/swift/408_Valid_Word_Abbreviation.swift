import Foundation

class Solution {
    func validWordAbbreviation(_ word: String, _ abbr: String) -> Bool {
        let wordArray = Array(word), abbrArray = Array(abbr)
        var wordPtr = 0, abbrPtr = 0, currentNumber = [String]()
        while wordPtr < wordArray.count && abbrPtr < abbrArray.count {
            if abbrArray[abbrPtr].isNumber {
                if currentNumber.isEmpty && String(abbrArray[abbrPtr]) == "0" {
                    return false
                }
                currentNumber.append(String(abbrArray[abbrPtr]))
                abbrPtr += 1
            } else if currentNumber.count > 0 {
                let num = Int(currentNumber.reduce("") { $0 + $1 })
                wordPtr += num!
                currentNumber.removeAll()
            } else if wordArray[wordPtr] == abbrArray[abbrPtr] {
                wordPtr += 1
                abbrPtr += 1
            } else {
                return false
            }
        }

        if currentNumber.count > 0 {
            let num = Int(currentNumber.reduce("") { $0 + $1 })
            wordPtr += num!
            currentNumber.removeAll()
        }
        return (wordPtr == wordArray.count && abbrPtr == abbrArray.count) ? true : false
    }
}


