"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        # self.stack.insert(0, value)
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None




class StackLL:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length +=1

    def remove_head(self):
        if not self.head:
            return None

        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -=1
            return current_head.value

        else:
            current.head = self.head
            self.head = current_head.next
            self.length-=1
            return current_head.value

    def remove_tail(self):
        pass





	
# from singly_linked_list import LinkedList

# 	class Stack:
# 	def __init__(self):
# 		self.size = 0
# 		self.storage = LinkedList()`
		
# 	def __len__(self):
# 		return self.size
		
# 	def push(self, value):
# 		self.storage.add_to_head(value) - O(1)
# 		self.storage.add_to_tail(value) - 0(1)
# 		self.size += 1
		
# 	def pop(self):
# 		if len(self.size) > 0:
# 			return self.storage.remove_head() - O(1)
# 			return self.storage.remove_tail() - O(n)
# 			self.size -= 1
# 		return None


# class Stack:
# 	def __init__(self):
# 		self.size = 0
# 		self.storage = []
		
# 	def __len__(self):
# 		return len(self.storage)
		
# 	def push(self, value):
# 		self.storage.insert(0, value) - NO - O(n)
# 		self.storage.append(value) - O(1)
		
# 	def pop(self):
# 		if len(self.storage) > 0:
# 			return self.storage.pop() - O(1)
# 		return None