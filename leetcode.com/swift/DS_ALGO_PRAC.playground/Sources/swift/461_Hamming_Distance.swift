class Solution {
    func hammingDistance(_ x: Int, _ y: Int) -> Int {
        var hammingDistance: Int = 0
        var maxLen = 0
        
        
        var strX = String(x, radix: 2)
        var strY = String(y, radix: 2)
        if strX.characters.count > strY.characters.count {
            maxLen = strX.characters.count
            strY = self.pad(string: strY, toSize: maxLen)
        } else {
            maxLen = strY.characters.count
            strX = self.pad(string: strX, toSize: maxLen)
        }
        
        for index in 0..<maxLen {
            let a = strX[strX.index(strX.startIndex, offsetBy: index)]
            let b = strY[strY.index(strY.startIndex, offsetBy: index)]
            
            if a != b {
                hammingDistance += 1
            }
        }
        
        
        return hammingDistance;
    }
    
    func pad(string : String, toSize: Int) -> String {
        var padded = string
        for _ in 0..<(toSize - string.characters.count) {
            padded = "0" + padded
        }
        return padded
    }
}
