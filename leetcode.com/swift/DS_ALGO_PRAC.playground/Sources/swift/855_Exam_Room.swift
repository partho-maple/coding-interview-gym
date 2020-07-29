import Foundation

class ExamRoom {
    var n = 1
    var occupiedSeates = Set<Int>()
    var maxIntervalHeap = [Int]() // A max Heap of interval value
    var maxIntervalRangeMap = [Int:[(Int, Int)]]() // key = max interval, value = lower and upper range of the interval

    init(_ N: Int) {
        self.n = N
    }
    
    func seat() -> Int {
        if occupiedSeates.count <= 0 {
            occupiedSeates.insert(0)
            return 0
        } else {
            
        }
    }
    
    func leave(_ p: Int) {
        occupiedSeates.remove(p)
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * let obj = ExamRoom(N)
 * let ret_1: Int = obj.seat()
 * obj.leave(p)
 */
