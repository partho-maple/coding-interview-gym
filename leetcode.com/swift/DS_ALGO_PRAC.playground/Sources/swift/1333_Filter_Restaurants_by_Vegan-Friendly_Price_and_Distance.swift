class Solution {
    func filterRestaurants(_ restaurants: [[Int]], _ veganFriendly: Int, _ maxPrice: Int, _ maxDistance: Int) -> [Int] {
        var filteredRestaurants = [[Int]]()
        for restaurant in restaurants {
            let (id, rating, veganFriendliness, price, distance) = (restaurant[0], restaurant[1], restaurant[2], restaurant[3], restaurant[4])
            if veganFriendly == 1 && veganFriendliness == 0 {
                continue
            }
            if price > maxPrice || distance > maxDistance {
                continue
            }
            filteredRestaurants.append(restaurant)
        }
        filteredRestaurants.sort {
            if $0[1] != $1[1] {
                return $0[1] > $1[1]
            } else {
                return $0[0] > $1[0]
            }
        }
        
        var result = [Int]()
        filteredRestaurants.forEach {
            result.append($0[0])
        }
        return result
    }
}

/*
veganFriendly == 1 > take only 1
veganFriendly == 0 > take all

1. By rating, decending
2. By ID, decending
3. price <= maxPrice
4. distance <= maxDistance

result [IDs]
*/
