class Solution {
    func removeDuplicates(_ s: String, _ k: Int) -> String {
        var counterStack = [(String, Int)]()
        var sStr = Array(s)
        var (currChar, currCount) = ("", 0)
        for i in 0..<sStr.count {
            currChar = String(sStr[i])
            currCount += 1
            var (prevChar, prevCount) =  (counterStack.count > 0) ? counterStack.last! : ("", 0)
            if currChar == prevChar && !currChar.isEmpty {
                (prevChar, prevCount) = counterStack.popLast()!
                currCount += prevCount
                if currCount > k {
                    counterStack.append((currChar, (currCount % k)))
                } else if currCount < k {
                    counterStack.append((currChar, (currCount)))
                }
            } else {
                counterStack.append((currChar, currCount))
            }
            (currChar, currCount) = ("", 0)
        }
        var result = ""
        print(counterStack)
        for (char, count) in counterStack {
            for i in 0..<count {
                result += char
            }
        }
        return result
    }
}
