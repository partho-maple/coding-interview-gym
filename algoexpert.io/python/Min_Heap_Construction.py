# https://www.algoexpert.io/questions/Min%20Heap%20Construction


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    # O(n) time | O(1) space
    def build_heap(self, array):
        first_parent_index = (len(array) - 2) // 2
        for current_index in reversed(range(first_parent_index + 1)):
            self.shift_down(current_index, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def shift_down(self, current_index, end_index, heap):
        child_one_index = current_index * 2 + 1
        while child_one_index <= end_index:
            child_two_index = current_index * 2 + 2 if current_index * 2 + 2 <= end_index else -1
            if child_two_index != -1 and heap[child_two_index] < heap[child_one_index]:
                index_to_swap = child_two_index
            else:
                index_to_swap = child_one_index
            if heap[index_to_swap] < heap[current_index]:
                self.swap(current_index, index_to_swap, heap)
                current_index = index_to_swap
                child_one_index = current_index * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space
    def shift_up(self, current_index, heap):
        parent_index = (current_index - 1) // 2
        while current_index > 0 and heap[current_index] < heap[parent_index]:
            self.swap(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self): # We mainly remove the root node by default. the first element of the array.
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop() # Heap follows a stack data structure
        self.shift_down(0, len(self.heap) -  1, self.heap)
        return value_to_remove

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.shift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

