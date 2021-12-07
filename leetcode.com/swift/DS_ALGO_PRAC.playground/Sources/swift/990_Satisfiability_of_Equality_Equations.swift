class Solution {
    func equationsPossible(_ equations: [String]) -> Bool {
        let uf = UnionFind(equations)
        
        for equation in equations {
            let equationArr = Array(equation)
            let sign = equationArr[1...2].reduce("") { "\($0)\($1)" }
            if sign == "==" {
                uf.union(equationArr[0], equationArr[3])
            }
        }
        
        for equation in equations {
            let equationArr = Array(equation)
            let sign = equationArr[1...2].reduce("") { "\($0)\($1)" }
            if sign == "!=" {
                if let parentX = uf.find(equationArr[0]), let parentY = uf.find(equationArr[3]), parentX == parentY {
                    return false
                }
            }
        }
        return true
    }
}

class UnionFind {
    var parents = [Character:Character]()
    var rank = [Character:Int]()
    
    public init(_ equations: [String]) {
        makeSet(equations)
    }
    
    func makeSet(_ equations: [String]) {
        for equation in equations {
            let equationArr = Array(equation)
            let sign = equationArr[1...2].reduce("") { "\($0)\($1)" }
            if sign == "!=" {
                continue
            }
            parents[equationArr[0]] = equationArr[0]
            parents[equationArr[3]] = equationArr[3]
            rank[equationArr[0], default: 0] += 1
            rank[equationArr[3], default: 0] += 1
        }
    }
    
    func find(_ x: Character) -> Character? {
        guard let parentX = parents[x] else {
            parents[x] = x
            return x
        }
        if x == parentX {
            return x
        }
        return find(parentX)
    }
    
    func union(_ x: Character, _ y: Character) {
        guard let parentX = find(x),
              let parentY = find(y) else {
            return
        }
        if parentX == parentY {
            return
        }
        if rank[parentX]! >= rank[parentY]! {
            parents[y] = parentX
            rank[parentX]! += 1
        } else {
            parents[x] = parentY
            rank[parentY]! += 1
        }
    }
}
