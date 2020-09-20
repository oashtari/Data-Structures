"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next 
        if self.next:
            self.next.prev = self.prev

    # def get_value(self):
    #     return self.value
        
    # def get_next(self):
    #     return self.next
        
    # def set_next(self, new_next):
    #     self.next = new_next

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1


        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        if not self.head and not self.tail:
            return None
        else:
            removed_head = self.head.value
            self.length -=1
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.next
                self.head.prev = None
            return removed_head

    # def remove_from_head(self):
    #     value = self.head.value
    #     self.delete(self.head)
    #     return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):

        if not self.head and not self.tail:
            return None
        else:
            removed_tail = self.tail.value
            self.length -=1
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return removed_tail
            else:
                self.tail = self.tail.prev
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        
        elif self.length == 1:
            return
        elif self.tail == node:
            new_head = node
            self.tail = node.prev
            node.prev.next = None
            self.head.prev = new_head 
            new_head.next = self.head
            self.head = new_head
        else:
            new_head = node
            node.next.prev = node.prev
            node.prev.next = node.next
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        elif self.length == 1:
            return
        elif self.head == node:
            new_tail = node
            self.head = node.next
            node.next.prev = None
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
        else:
            new_tail = node
            node.prev.next = node.next
            node.prev = self.tail
            node.next = None
            self.tail.next = node 
            self.tail = node        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        if not self.head and not self.tail:
            return

        elif self.head is self.tail:
            self.head = None
            self.tail = None

        elif self.head is node:
            self.head = node.next
            node.delete()

        elif self.tail is node:
            self.tail = node.prev
            node.delete()

        else: 
            node.delete()
        self.length -=1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value

        current = self.head.next

        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value