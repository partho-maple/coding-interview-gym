/*
// https://tinyurl.com/y9az7nef
// O(n^3) time and O(n^2) space. Musbe be asked to improve
class Solution {
    func multiply(_ A: [[Int]], _ B: [[Int]]) -> [[Int]] {
        var ab = Array(repeating: Array(repeating: 0, count: B[0].count), count: A.count)
        let (rowA, colB, colArowB) = (A.count, B[0].count, B.count)
        for i in 0..<rowA {
            for k in 0..<colArowB {
                if A[i][k] == 0 {
                    continue
                }
                for j in 0..<colB {
                    ab[i][j] += (A[i][k] * B[k][j])
                }
            }
        }
        return ab
    }
}
*/

//https://tinyurl.com/y9az7nef
class Solution {
    func multiply(_ A: [[Int]], _ B: [[Int]]) -> [[Int]] {
        var ab = Array(repeating: Array(repeating: 0, count: B[0].count), count: A.count)
        let (rowA, colB, colArowB) = (A.count, B[0].count, B.count)
        for i in 0..<rowA {
            for k in 0..<colArowB {
                if A[i][k] == 0 {
                    continue
                }
                for j in 0..<colB {
                    ab[i][j] += (A[i][k] * B[k][j])
                }
            }
        }
        return ab
    }
}

/*
 Input:

 A = [
   [ 1, 0, 0],
   [-1, 0, 3]
 ]

 B = [
   [ 7, 0, 0 ],
   [ 0, 0, 0 ],
   [ 0, 0, 1 ]
 ]

 Output:

      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
 AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                   | 0 0 1 |
 */
