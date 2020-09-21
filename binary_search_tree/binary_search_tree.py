"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
# path = sys.path.append('..')

sys.path.append('../queue')

# sys.path.insert(1, '../queue/')

from queue import Queue


sys.path.insert(1, '../stack/')

from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:

            if self.left is None:
                self.left = BSTNode(value)

            else:
                self.left.insert(value)

        if value > self.value:

            if self.right is None:
                self.right = BSTNode(value)

            else: 
                self.right.insert(value)
    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if not self.left:
                return False
            else: 
                return self.left.contains(target)

        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        while self.right:
            self = self.right
        return self.value

    def get_min(self):
        if not self.left:
            return self.value
        while self.left:
            self = self.left
        return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    
    def in_order_print(self, node):
        
        if node.left is not None:
            self.in_order_print(node.left)

        print(node.value)

        # print('RIGHT', self.right)
        if node.right is not None:
            self.in_order_print(node.right)

    # def in_order_print(self):
    #     # In-Order -> LEFT NODE | NODE | RIGHT NODE
    #     if self.left != None:  # L
    #         self.in_order_print(self.left)

    #     print(self.value)  # N

    #     if self.right != None:  # R
    #         self.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Queue
    def bft_print(self):
        # queue = Queue()
        # queue.enqueue(node)

        # while len(queue) > 0:

        # print('Q', queue)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Stack
        pass
    def dft_print(self):
        # stack = []


        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# # bst.pre_order_dft()
# print("in order")
# # bst.in_order_dft()
# print("post order")
# # bst.post_order_dft()  
