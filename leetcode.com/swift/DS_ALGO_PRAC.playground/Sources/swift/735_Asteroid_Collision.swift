import Foundation
class Solution {
    func asteroidCollision(_ asteroids: [Int]) -> [Int] {
        var stack = [Int]()
        for item in asteroids {
            if item > 0 {
                stack.append(item)
            } else {
                while !stack.isEmpty && stack.last! > 0 && stack.last! < abs(item) {
                    stack.removeLast()
                }
                if stack.isEmpty || stack.last! < 0 {
                    stack.append(item)
                } else if stack.last! == -item {
                    stack.removeLast()
                }
            }
        }
        return stack
    }
}
