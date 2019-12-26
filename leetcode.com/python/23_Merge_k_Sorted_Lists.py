
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




import heapq

# Heap bassed approach. It's preferrale over the other approaches. ALso  check PriorityQueue here: https://tinyurl.com/yx4xh9tq
# Source: https://tinyurl.com/vaetc9d
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minHeap = []

        # put the root of each list in the min heap
        for idx, listRoot in enumerate(lists):
            if listRoot:
                heapq.heappush(minHeap, (listRoot.val, idx, listRoot))

        resultHead, resultTail = None, None
        while minHeap:
            currentNodeVal, currentListIdx, currentNode = heapq.heappop(minHeap)
            if not resultHead:
                resultHead, resultTail = currentNode, currentNode
            else:
                resultTail.next = currentNode
                resultTail = resultTail.next
            if currentNode.next:
                heapq.heappush(minHeap, (currentNode.next.val, currentNodeVal, currentNode.next))

        return resultHead




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.val < other.val




import heapq

# Not Accepted, because List node is not iteratable since we are not allowed to edit the ListNode object to make it iteratable
# Heap bassed approach. It's preferrale over the other approaches.
# But the prolem of this approach is that you need to modify the ListNode and overload it's operator. To be comparable on the heap.
# Source: https://tinyurl.com/vaetc9d
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minHeap = []

        # put the root of each list in the min heap
        for listRoot in lists:
            if listRoot:
                heapq.heappush(minHeap, listRoot)

        resultHead, resultTail = None, None
        while minHeap:
            currentNode = heapq.heappop(minHeap)
            if not resultHead:
                resultHead, resultTail = currentNode, currentNode
            else:
                resultTail.next = currentNode
                resultTail = resultTail.next
            if currentNode.next:
                heapq.heappush(minHeap, currentNode.next)

        return resultHead



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Approach 5. Source: https://tinyurl.com/rybqon6
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        numerOfLists = len(lists)
        interval = 1
        while interval < numerOfLists:
            for idx in range(0, numerOfLists - interval, interval * 2):
                lists[idx] = self.mergeTwoLists(lists[idx], lists[idx + interval])
            interval *= 2
        return lists[0] if numerOfLists > 0 else None


    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2
        p1, p2, p1Prev = l1, l2, None
        while p1 and p2:
            if p1.val < p2.val:
                p1Prev = p1
                p1 = p1.next
            else:
                if p1Prev:
                    p1Prev.next = p2
                p1Prev = p2
                p2 = p2.next
                p1Prev.next = p1
        if not p1:
            p1Prev.next = p2
        return l1 if l1.val < l2.val else l2


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------