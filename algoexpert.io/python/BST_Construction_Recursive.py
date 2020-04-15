# My solution. Failing on 2 test case but do't know why
class BST:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parent = None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min_value()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass  # This is a single-node tree. nothing to do
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self

    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()




# Source: https://tinyurl.com/rxnq4sz
def traverse_list(node):
    visit_order = list()
    if node:
        visit_order.append(node.value)
        visit_order += traverse_list(node.left)
        visit_order += traverse_list(node.right)
    return visit_order


def traverse(node):
    visit_order = list()
    if node:
        visit_order.append(node)
        visit_order += traverse(node.left)
        visit_order += traverse(node.right)
    return visit_order


def get_min_node_value(node):
    while node.left:
        node = node.left
    return node.value


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def compare(self, target):
        if self.value > target:
            return -1
        elif self.value < target:
            return 1
        else:
            return 0

    def insert(self, value):

        node = self
        while True:
            comparision = node.compare(value)
            if comparision == -1:
                if node.left:
                    node = node.left
                else:
                    node.left = BST(value)
                    break
            else:  # comparision == 1 or equals
                if node.right:
                    node = node.right
                else:
                    node.right = BST(value)
                    break

        return self

    def contains(self, value):
        node = self
        while node:
            comparision = node.compare(value)
            if comparision == -1:
                node = node.left
            elif comparision == 1:
                node = node.right
            else:
                return True

        return False

    def remove(self, value, parent_node=None):
        node = self
        while True:
            comparision = node.compare(value)
            if comparision == -1:
                if node.left:
                    parent_node = node
                    node = node.left
                else:
                    print('Value not found')
                    break
            elif comparision == 1:
                if node.right:
                    parent_node = node
                    node = node.right
                else:
                    print('Value not found')
                    break
            else:
                if node.left and node.right:  # node with left and child
                    node.value = get_min_node_value(node.right)
                    node.right.remove(node.value, node)
                elif parent_node is None:  # parent node
                    if node.left:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:  # parent node with no children
                        node.value = None

                elif parent_node.left == node:  # found in the left node with right None
                    parent_node.left = node.left if node.left else node.right
                elif parent_node.right == node:  # found in the right node with left None
                    parent_node.right = node.left if node.left else node.right
                break

        return self