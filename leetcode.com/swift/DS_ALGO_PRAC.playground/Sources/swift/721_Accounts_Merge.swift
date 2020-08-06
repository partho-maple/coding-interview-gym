import Foundation
class Solution {
    func accountsMerge(_ accounts: [[String]]) -> [[String]] {
        var emailToNameMap = [String: String]()
        var graph = [String: Set<String>]()
        for account in accounts {
            let (name, emails) = (account[0], account[1...])
            for email in emails {
                if graph[emails.first!] == nil {
                    graph[emails.first!] = Set<String>()
                }
                graph[emails.first!]?.insert(email)
                if graph[email] == nil {
                    graph[email] = Set<String>()
                }
                graph[email]!.insert(emails.first!)
                emailToNameMap[email] = name
            }
        }
        var seen = Set<String>()
        var result = [[String]]()
        for (node, _) in graph {
            if !seen.contains(node) {
                seen.insert(node)
                var nodeStack = [String]()
                nodeStack.append(node)
                var connectedNodes = [String]()
                while !nodeStack.isEmpty {
                    let currentNode = nodeStack.popLast()
                    connectedNodes.append(currentNode!)
                    for neighbour in graph[currentNode!]! {
                        if !seen.contains(neighbour) {
                            seen.insert(neighbour)
                            nodeStack.append(neighbour)
                        }
                    }
                }
                result.append([emailToNameMap[node]!] + connectedNodes.sorted(by: <))
            }
        }
        return result
    }
}




/*
 [
 ["John", "johnsmith@mail.com", "john00@mail.com"],
 ["John", "johnnybravo@mail.com"],
 ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
 ["Mary", "mary@mail.com"]
 ]
 
map[email:name]
 
email=key / name-idx=value
 
 ohnsmith@mail.com = j,0; j,2
 john00@mail.com = j,0
 johnnybravo@mail.com = j,1
 john_newyork@mail.com = j,2
 mary@mail.com = m,3
 
 

 
 [
 ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
 ["John", "johnnybravo@mail.com"],
 ["Mary", "mary@mail.com"]]
 
 
 
 Graph problem, consider emails as node and names as edges
 
 it looks like disjoint set problem, where every set will be the answer after merging.
 */

