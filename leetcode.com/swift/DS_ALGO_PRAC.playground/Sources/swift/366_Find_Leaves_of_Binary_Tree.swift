class Solution {
    func findLeaves(_ root: TreeNode?) -> [[Int]] {
        var result = [[Int]]()
        getHeight(root, &result)
        return result
    }
    
    @discardableResult
    func getHeight(_ root: TreeNode?, _ leaves: inout [[Int]]) -> Int {
        guard let root = root else {
            return -1
        }
        
        let (left, right) = (getHeight(root.left, &leaves), getHeight(root.right, &leaves))
        let height = max(left, right) + 1
        if height < leaves.count {
            leaves[height].append(root.val)
        } else {
            leaves.append([root.val])
        }
        return height
    }
}
