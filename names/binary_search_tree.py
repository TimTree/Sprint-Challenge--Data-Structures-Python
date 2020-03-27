import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: # new value less than current value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                temp = self.left
                temp.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                temp = self.right
                temp.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value: # target less than current value
                try:
                    temp = self.left
                    return temp.contains(target)
                except AttributeError:
                    return False
            else:
                try:
                    temp = self.right
                    return temp.contains(target)
                except AttributeError:
                    return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
