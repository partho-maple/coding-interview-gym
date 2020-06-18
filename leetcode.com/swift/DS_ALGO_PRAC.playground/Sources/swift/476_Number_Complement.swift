class Solution {
    func findComplement(_ num: Int) -> Int {
        var strNum = String(num, radix: 2)
        var strComplement = ""
        
        for index in 0..<strNum.characters.count {
            let charAtIndex = strNum[strNum.index(strNum.startIndex, offsetBy: index)]
            print(charAtIndex)
            
            if charAtIndex != "1" {
                strComplement.append("1")
            } else {
                strComplement.append("0")
            }
        }
        let complement = Int(String(strComplement), radix: 2)!
        return complement
    }
}







