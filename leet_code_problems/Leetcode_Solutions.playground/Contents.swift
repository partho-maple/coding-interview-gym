//: Testing code for each solution

import UIKit
import Foundation




var inputArr: [Int] = [1,1,0,1,1,1]
var count = 0
var arrOfOnes: [Int] = []

for index in 0..<inputArr.count {
    print(index)
    print(inputArr[index])
    

    if inputArr[index] == 1 {
        count += 1
        
        if index == (inputArr.count - 1) {
            arrOfOnes.append(count)
        }
    } else {
        arrOfOnes.append(count)
        count = 0
    }
    
    print(count)
    print("\n")
}
print(arrOfOnes)

// Now sort arrOfOnes and get the biggest number. Use quicksort or merge sort.






