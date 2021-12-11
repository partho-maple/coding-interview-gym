
class MovingAverage {

    var queue = [Int]()
    var currentSum = 0
    let size: Int
    init(_ size: Int) {
        self.size = size
    }
    
    func next(_ val: Int) -> Double {
        queue.append(val)
        currentSum += val
        if queue.count <= size {
            return Double(currentSum) / Double(queue.count)
        } else {
            let first = queue.removeFirst()
            currentSum -= first
            return Double(currentSum) / Double(queue.count)
        }
    }
}
