class Solution {
    func lowestCommonAncestor(_ p: Node?,_ q: Node?) -> Node? {
        var pDepth = getDepth(p, 0), qDepth = getDepth(q, 0)
        var pCopy = p, qCopy = q
        if pDepth > qDepth {
            while pDepth > qDepth {
                pCopy = pCopy.parent
                pDepth -= 1
            }
        } else if pDepth < qDepth {
            while pDepth < qDepth {
                qCopy = qCopy.parent
                qDepth -= 1
            }
        }
        
        while pCopy != qCopy {
            pCopy = pCopy.parent
            qCopy = qCopy.parent
        }
        
        return pCopy
    }
    
    func getDepth(_ node: Node?, _ depth: Int) -> Int {
        guard let node = node else {
            return depth
        }
        return getDepth(node.parent, depth + 1)
    }
}
