// Brute force solution | O(n^2) | Accepted
class Solution {
    func minMeetingRooms(_ intervals: [[Int]]) -> Int {
        if intervals.count <= 0 {
            return 0
        } else if intervals.count == 1 {
            return 1
        }
        var sortedInt = intervals.sorted {$0[0] < $1[0]} // sorting by starting time
        var maxRoomCount = 1
        for i in 1..<sortedInt.count {
            var roomCount = 1
            for j in 0..<i {
                let curInterval = sortedInt[i]
                let prevInterval = sortedInt[j]
                if curInterval[0] < prevInterval[1] {
                    roomCount += 1
                }
            }
            maxRoomCount = max(maxRoomCount, roomCount)
        }
        return maxRoomCount
    }
}


// Using min heap | O(nlogn) | Accepted
class Solution {
    func minMeetingRooms(_ intervals: [[Int]]) -> Int {
        if intervals.count <= 0 {
            return 0
        }
        var sortedInt = intervals.sorted {$0[0] < $1[0]} // sorting by starting time
        var occupiedRooms: Heap<Int> = Heap<Int>(sort: <) // MinHeap which stores the ending time of the meetings
        for i in 0..<sortedInt.count {
            var currentInterval  = sortedInt[i]
            if occupiedRooms.isEmpty {
                occupiedRooms.insert(currentInterval[1])
                continue
            }
            if currentInterval[0] >= occupiedRooms.peek()! {
                occupiedRooms.remove()
            }
            occupiedRooms.insert(currentInterval[1])
        }
        return occupiedRooms.count
    }
}



// Improved Code
class Solution {
    func minMeetingRooms(_ intervals: [[Int]]) -> Int {
        guard intervals.count > 1 else {
            return 1
        }
        let sortedInterval = intervals.sorted { $0[0] < $1[0] }
        var minHeap: Heap<Int> = Heap<Int>(sort: <)
        for i in 0..<sortedInterval.count {
            if let peak = minHeap.peek(), peak <= sortedInterval[i][0] {
                minHeap.remove()
            }
            minHeap.insert(sortedInterval[i][1])
        }
        return minHeap.count
    }
}
