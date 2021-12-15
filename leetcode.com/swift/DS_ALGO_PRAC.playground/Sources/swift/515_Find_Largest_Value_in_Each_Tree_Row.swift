class Solution {
    func largestValues(_ root: TreeNode?) -> [Int] {
        guard let root = root else {
            return []
        }
        var result = [Int](), queue = [TreeNode]()
        queue.append(root)
        while !queue.isEmpty {
            var currentMax = Int.min
            let currentLevelLength = queue.count
            for i in 0..<currentLevelLength {
                let node = queue.removeFirst()
                currentMax = max(currentMax, node.val)
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
            result.append(currentMax)
        }
        return result
    }
}
