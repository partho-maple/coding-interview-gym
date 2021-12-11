// Using dictionary. Accepted
class SparseVector {
    var nonZeros = [Int:Int]()
    init(_ nums: [Int]) {
        for (index, item) in nums.enumerated() {
            if item != 0 {
                nonZeros[index] = item
            }
        }
    }

    // Return the dotProduct of two sparse vectors
    func dotProduct(_ vec: SparseVector) -> Int {
        var result = 0
        for index in vec.nonZeros.keys {
            if let otherItem = nonZeros[index] {
                result += (otherItem * vec.nonZeros[index]!)
            }
        }
        return result
    }
}

// Using 2 pointers. Accepted
class SparseVector {
    var pairs = [(Int, Int)]() // (index, item)
    init(_ nums: [Int]) {
        for (index, item) in nums.enumerated() {
            if item != 0 {
                pairs.append((index, item))
            }
        }
    }

    // Return the dotProduct of two sparse vectors
    func dotProduct(_ vec: SparseVector) -> Int {
        var result = 0, ptrOne = 0, ptrTwo = 0
        while ptrOne < pairs.count && ptrTwo < vec.pairs.count {
            if pairs[ptrOne].0 == vec.pairs[ptrTwo].0 {
                result += (pairs[ptrOne].1 * vec.pairs[ptrTwo].1)
                ptrOne += 1
                ptrTwo += 1
            } else if pairs[ptrOne].0 < vec.pairs[ptrTwo].0 {
                ptrOne += 1
            } else {
                ptrTwo += 1
            }
        }
        return result
    }
}
