# https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End


# O(n) time | O(1) space
def remove_kth_node_from_end(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next


