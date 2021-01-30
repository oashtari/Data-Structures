# MIDDLE NODE 
# hound (middle, speed 1) and hare (end, speed 2)
# take 2 pointers, lable one middle, other end
# start looping with pointers at initial Node
# while end pointer is none

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

    def add(self, value):
        self.next = Node(value)

    def find_middle(self):
        middle = self

        end = self

        while end != None:
            end = end.next
            
            if end:
                end = end.next
                middle = middle.next

        print(f"Middle Value is {middle.value}")

        # building linked list to test the middle algo
#(4)->(7)->(9)->(2)->(12)
root = Node(4)

current_node = root

current_node.add(7)

current_node = current_node.next

current_node.add(9)

current_node = current_node.next

current_node.add(2)

current_node = current_node.next

current_node.add(12)

# MIDDLE solution if looking for first middle in even set
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

    def add(self, value):
        self.next = Node(value)

    def find_middle(self):
        middle = self

        end = self

        while end != None:
            end = end.next
            
            if end and end.next:
                end = end.next
                middle = middle.next

        print(f"Middle Value is {middle.value}")


# SMALLEST MISSING ELEMENT IN ARRAY 