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
