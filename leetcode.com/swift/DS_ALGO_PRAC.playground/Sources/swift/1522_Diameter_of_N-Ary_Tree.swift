// My initial solution. 37 / 38 test cases passed. https://tinyurl.com/y2wfypuh
class Solution {
    func diameter(_ root: Node?) -> Int {
        guard let root = root else {
            return 0
        }
        var (excludingThisNode, asRoot, asBranch) = diameterDFSHelper(root)
        return [excludingThisNode, asRoot, asBranch].max()!
    }
    
    func diameterDFSHelper(_ root: Node) -> (Int, Int, Int) {
        guard !root.children.isEmpty else {
            return (0, 0, 0)
        }
        
        var (excludingThisNode, max1, max2) = (0, 0, 0)
        for node in root.children {
            let (_, asRootCurr, asBranchCurr) = diameterDFSHelper(node)
            excludingThisNode = max(excludingThisNode, asRootCurr)
            if asBranchCurr > max1 {
                max2 = max1
                max1 = asBranchCurr
            } else if asBranchCurr > max2 {
                max2 = asBranchCurr
            }
        }
        
        if root.children.count == 1 {
            return (excludingThisNode, 1 + max1, 1 + max1)
        } else {
            return (excludingThisNode, 2 + max1 + max2, 1 + max1)
        }
    }
}

// https://tinyurl.com/y5oyyjpf
class Solution {
    var result = 0
    func diameter(_ root: Node?) -> Int {
        guard let root = root else { return 0 }
        getHeightDFSHelper(root)
        return result
    }
    
    func getHeightDFSHelper(_ root: Node?) -> Int {
        guard let root = root else { return 0 }
        var max1Height = 0
        var max2Height = 0
        for child in root.children {
            let currentHeight = getHeightDFSHelper(child)
            if currentHeight > max1Height {
                max2Height = max1Height
                max1Height = currentHeight
            } else if currentHeight > max2Height {
                max2Height = currentHeight
            }
        }
        result = max(result, max1Height + max2Height)
        return max(max1Height, max2Height) + 1
    }
}
