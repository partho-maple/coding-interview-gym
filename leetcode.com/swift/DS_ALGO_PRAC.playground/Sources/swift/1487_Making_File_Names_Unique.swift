// Linear search. Time: O(n^2). TLE for big input
class Solution {
    func getFolderNames(_ names: [String]) -> [String] {
        var counter = [String:Int]()
        var result = [String]()
        for name in names {
            if counter[name] == nil {
                counter[name, default: 0] += 1
                result.append(name)
                continue
            }
            var k = counter[name]!, newName = "\(name)(\(k))"
            while counter[newName] != nil {
                k += 1
                newName = "\(name)(\(k))"
            }
            counter[newName, default: 0] += 1
            result.append(newName)
        }
        return result
    }
}

// Linear search. Time: O(n^2). Similar to mi above one but it's accepted. No idea why?  https://tinyurl.com/yy9kwrbm
class Solution {
    func getFolderNames(_ names: [String]) -> [String] {
        var dict : [String:Int] = [:]
        var res : [String] = []
        for n in names{
            if dict[n] == nil{
                dict[n] = 0
                res.append(n)
            }
            else{
                if dict[n] != nil{
                    var i = dict[n]! + 1
                    var val = n + String("(\(i))")
                    while(dict[val] != nil) {
                        i += 1
                        val = n + String("(\(i))")
                    }
                    dict[n] = i
                    dict[val] = 0
                    res.append(val)
                }
            }
        }
        return res
    }
}

// Binary search. Time: O(n). Wrong answer for some cases
class Solution {
    func getFolderNames(_ names: [String]) -> [String] {
        var counter = [String:Int]()
        var result = [String]()
        for name in names {
            if counter[name] == nil {
                counter[name, default: 0] += 1
                result.append(name)
                continue
            }
            var startK = counter[name]!, endK = names.count
            while startK < endK {
                let midK = startK + ((endK - startK) / 2)
                let newName = "\(name)(\(midK))"
                if counter[newName] == nil {
                    endK = midK
                } else {
                    startK = midK + 1
                }
            }
            let newName = "\(name)(\(startK))"
            counter[newName, default: 0] += 1
            result.append(newName)
        }
        return result
    }
}
