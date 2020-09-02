class Solution {
    func largestTimeFromDigits(_ A: [Int]) -> String {
        var permutations = [[Int]]()
        let sortedA = A.sorted(by: >)
        for i in 0..<sortedA.count {
            for j in 0..<sortedA.count {
                if j == i {
                    continue
                }
                for k in 0..<sortedA.count {
                    if k == i || k == j {
                        continue
                    }
                    for l in 0..<sortedA.count {
                        if l == i || l == j || l == k {
                            continue
                        }
                        let permutation = [sortedA[i], sortedA[j], sortedA[k], sortedA[l]]
                        permutations.append(permutation)
                    }
                }
            }
        }
        
        for permutation in permutations {
            let (hour, minuites) = ((permutation[0]*10) + permutation[1], (permutation[2]*10) + permutation[3])
            if hour < 24 && minuites < 60 {
                var (hourStr, minuitesStr) = (String(hour), String(minuites))
                if hour < 10 {
                    hourStr = "0" + hourStr
                }
                if minuites < 10 {
                    minuitesStr = "0" + minuitesStr
                }
                return hourStr + ":" + minuitesStr
            }
         }
        return ""
    }
}
