import Foundation
class Solution {
    func countBits(_ num: Int) -> [Int] {
        var result = [Int]()
        for i in 0...num {
            if i == 0 {
                result.append(0)
            } else if i == 1 || i == 2 {
                result.append(1)
            } else if i == 3 {
                result.append(2)
            } else {
                var iCopy = i
                var previousPowForBaseTwo = 0
                while iCopy > 1 {
                    previousPowForBaseTwo += 1
                    iCopy = iCopy >> 1
                }
                let differenceFromPreviousTwoBaseNum = i - Int(pow(Double(2), Double(previousPowForBaseTwo)))
                let previousPopCount: Int = result[differenceFromPreviousTwoBaseNum]
                let currentPopCount: Int = previousPopCount + 1
                result.append(currentPopCount)
            }
        }
        return result
    }
}


/*
 Input: 2
 Output: [0,1,1]
 
 0,1,2
 [0,1,1]
  
 Between the range of 2^x to 2^(x + 1) - 1, there could be maximum of x + 1 number of 1s could appear, which would start from 1 to x + 1.
 
 0 0
 1 1 2^0
 
 10 2 2^1
 11 3
 
 100 4 2^2
 101 5
 110 6
 111 7
 
 1000 8 2^3
 1001 9
 1010 10
 1011 11
 1100 12
 1101 13
 1110 14
 1111 15
 
 10000 16 2^4
 10001 17
 10010 18
 10011 19
 10100 20
 10101 21
 10110 22
 10111 23
 11000 24
 11001 25
 .
 .
 11111 31
 
 100000 32 2^5
 100001
 

 
Popcount means the number of 1's in the binary representation of a number.
Function for popcount P(x):
 where x is a number, lets say which is 9
 and b is it's next power of 2's, lets say which is 16 = 2^4
 where b = 2^m > x
 so, P(x + b) = P(x) + 1
 
 Example:
 P(25) = P(9 + 16) = P(9) + 1 = 2 + 1 = 3
 p(33) = P(1 + 32) = P(1) = 1 = 1 + 1 = 2
 
 
 
 2^0 = 1
 2^1 = 2
 2^2 = 4
 2^3 = 8
 2^4 = 16
 2^5 = 32
 2^6 = 64
 2^7 = 128
 2^8 = 256
    
 */
