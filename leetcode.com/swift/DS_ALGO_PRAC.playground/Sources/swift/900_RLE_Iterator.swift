import Foundation

class RLEIterator {

    var A = [Int]()
    var current_counter_index = 0
    
    init(_ A: [Int]) {
        self.A = A
    }
    
    func next(_ n: Int) -> Int {
        guard current_counter_index < A.count - 1 else {
            return -1
        }
        var currentN = n

        while current_counter_index < A.count && currentN > A[current_counter_index] {
            currentN -= A[current_counter_index]
            current_counter_index += 2
        }
        
        if current_counter_index < A.count {
            A[current_counter_index] -= currentN
            return A[current_counter_index + 1]
        }
        
        return -1
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * let obj = RLEIterator(A)
 * let ret_1: Int = obj.next(n)
 */
