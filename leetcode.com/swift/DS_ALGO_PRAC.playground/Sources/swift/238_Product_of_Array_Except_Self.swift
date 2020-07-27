import Foundation
// O(N) time and space
class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        guard nums.count > 1 else {
            return [0]
        }
        var prefixProduct = [Int]()
        for (index, item) in nums.enumerated() {
            if index == 0 {
                prefixProduct.append(item)
            } else {
                prefixProduct.append(prefixProduct.last!*item)
            }
        }
        
        var suffixProduct = [Int]()
        for (index, item) in nums.reversed().enumerated() {
            if index == 0 {
                suffixProduct.append(item)
            } else {
                suffixProduct.append(suffixProduct.last!*item)
            }
        }
        suffixProduct.reverse()
        
        var result = [Int]()
        for i in 0..<nums.count {
            if i == 0 {
                result.append(suffixProduct[i + 1])
            } else if i == nums.count - 1 {
                result.append(prefixProduct[i - 1])
            } else {
                result.append(prefixProduct[i - 1] * suffixProduct[i + 1])
            }
        }
        return result
    }
}


// O(N) time | O(1) space
class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        guard nums.count > 1 else {
            return [0]
        }
        var result = [Int]()
        for (index, item) in nums.enumerated() {
            if index == 0 {
                result.append(item)
            } else {
                result.append(result.last!*item)
            }
        }
        
        var suffixProduct = 0
        for index in stride(from: nums.count - 1, through: 0, by: -1) {
            if index == nums.count - 1 {
                result[index] = result[index - 1]
                suffixProduct = nums[index]
            } else if index == 0 {
                result[index] = suffixProduct
            } else {
                result[index] = result[index - 1] * suffixProduct
                suffixProduct = suffixProduct * nums[index]
            }
        }
        return result
    }
}
