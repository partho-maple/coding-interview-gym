//: Testing code for each solution

import UIKit
import Foundation



//MARK: Solution test code for: #1 - Two Sum
let inputArr = [0,4,3,0]
let target = 0
var solution_1 : Solution_1 = Solution_1()
solution_1.twoSum(inputArr, target)



let num = 22
let str = String(num, radix: 2)
print(str) // prints "10110"

let charAtIndex = str[str.index(str.startIndex, offsetBy: 4)]




var strNum = String(5, radix: 2)
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


var complement = Int(String(strComplement), radix: 2)!





