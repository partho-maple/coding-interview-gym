// Bruteforce exustive search with backtracking. Time limit exceeded. 44 / 103 test cases passed.
// Time: O(2^(A + B))
class Solution {
    func strWithout3a3b(_ A: Int, _ B: Int) -> String {
        var allComb = [String]()
        var currComb = [String]()
        strWithout3a3bHelper(A, B, currComb, &allComb)
        return allComb.first!
    }
    
    func strWithout3a3bHelper(_ A: Int, _ B: Int, _ currComb: [String], _ allComb: inout [String]) {
        if allComb.count >= 1 {
            return
        }
        if currComb.count >= 3 {
            let currStr = currComb[(currComb.count - 3)..<currComb.count].reduce("") { $0 + $1 }
            if currStr == "aaa" || currStr == "bbb" {
                return
            }
        }
        if A <= 0 && B <= 0 {
            let currStr = currComb.reduce("") { $0 + $1 }
            allComb.append(currStr)
            return
        }
        
        if A > 0 {
            strWithout3a3bHelper(A - 1, B, currComb + ["a"], &allComb)
        }
        if B > 0 {
            strWithout3a3bHelper(A, B - 1, currComb + ["b"], &allComb)
        }
    }
}

// Recursive greedy solution, Accepted
class Solution {
    func strWithout3a3b(_ A: Int, _ B: Int) -> String {
        if A == 0 {
            return Array(repeating: "b", count: B).reduce("") { $0 + $1 }
        } else if B == 0 {
            return Array(repeating: "a", count: A).reduce("") { $0 + $1 }
        } else if A == B {
            return Array(repeating: "ab", count: A).reduce("") { $0 + $1 }
        } else if A > B {
            return "aab" + strWithout3a3b(A - 2, B - 1)
        } else {
            return "bba" + strWithout3a3b(A - 1, B - 2)
        }
    }
}

// Iterative greedy solution, Accepted
class Solution {
    func strWithout3a3b(_ A: Int, _ B: Int) -> String {
        var result = [String]()
        var (a, b) = (A, B)
        while a > 0 || b > 0 {
            if a == 0 {
                return (result + Array(repeating: "b", count: b)).reduce("") { $0 + $1 }
            } else if b == 0 {
                return (result + Array(repeating: "a", count: a)).reduce("") { $0 + $1 }
            } else if a == b {
                return (result + Array(repeating: "ab", count: a)).reduce("") { $0 + $1 }
            } else if a > b {
                result += ["aab"]
                a -= 2
                b -= 1
            } else {
                result += ["bba"]
                a -= 1
                b -= 2
            }
        }
        return result.reduce("") { $0 + $1 }
    }
}



