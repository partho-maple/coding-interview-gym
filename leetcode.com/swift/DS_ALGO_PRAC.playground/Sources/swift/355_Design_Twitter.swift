import Foundation

class Twitter {

    var userIDAndTweetMap = [Int:[(Int, Int)]]()
    var followerAndfolloweeMap = [Int:Set<Int>]() // [follower: Set<followee>]
    let maxPost = 10
    var currentTimeRef = 10000
    
    init() {
        
    }
    
    func postTweet(_ userId: Int, _ tweetId: Int) {
        currentTimeRef += 1
        
        // add tweet to user's feed
        userIDAndTweetMap[userId, default: [(Int, Int)]()].append((tweetId, currentTimeRef))
        if userIDAndTweetMap[userId]!.count > maxPost {
            userIDAndTweetMap[userId]!.removeFirst()
        }
    }
    
    func getNewsFeed(_ userId: Int) -> [Int] {
        var allFeeds = [(Int, Int)]()
        
        if let feeds = userIDAndTweetMap[userId] {
            allFeeds.append(contentsOf: feeds)
        }
        
        if let followeeIds = followerAndfolloweeMap[userId] {
            for followeeId in Array(followeeIds) {
                if let feeds = userIDAndTweetMap[followeeId] {
                    allFeeds.append(contentsOf: feeds)
                }
            }
        }
        allFeeds.sort { $0.1 > $1.1 }
        let feeds = allFeeds.map { $0.0 }
        
        return feeds.count <= maxPost ? feeds : Array(feeds[0..<10])
    }
    
    func follow(_ followerId: Int, _ followeeId: Int) {
        followerAndfolloweeMap[followerId, default: Set<Int>()].insert(followeeId)
    }
    
    func unfollow(_ followerId: Int, _ followeeId: Int) {
        followerAndfolloweeMap[followerId]?.remove(followeeId)
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * let obj = Twitter()
 * obj.postTweet(userId, tweetId)
 * let ret_2: [Int] = obj.getNewsFeed(userId)
 * obj.follow(followerId, followeeId)
 * obj.unfollow(followerId, followeeId)
 */
