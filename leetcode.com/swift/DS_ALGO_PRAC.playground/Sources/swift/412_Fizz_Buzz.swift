
class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var stringArr: [String] = []
        
        for index in 1...n {
            if ((index % 3) == 0) && ((index % 5) == 0) {
                stringArr.append("FizzBuzz")
                print("FizzBuzz")
            } else if ((index % 3) == 0) {
                stringArr.append("Fizz")
                print("Fizz")
            } else if ((index % 5) == 0) {
                stringArr.append("Buzz")
                print("Buzz")
            } else {
                stringArr.append(String(index))
                print(index)
            }
        }
        
        return stringArr
    }
}

