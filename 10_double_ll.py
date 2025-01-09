# Write a Python program to create a doubly linked list and print nodes from current position to first node.
class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
    
    def get_prev_node(self):
        return self.prev_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node

class DoublyLinkedList():
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    
    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        
        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head
    
    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        
        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = None
    
    def print_foward_linked_list(self):
        current_node = self.head_node
        while current_node is not None:
            print(current_node.get_value())
            current_node = current_node.get_next_node()
    
    def print_from_n_to_first(self, n):
        current_node = self.head_node
        n_node = self.head_node
        position = 1
        while current_node is not None:
            if position == n:
                n_node = current_node
                while n_node is not None:
                    print(n_node.get_value())
                    n_node = n_node.get_prev_node()
            position += 1
            current_node = current_node.get_next_node()

dll = DoublyLinkedList()
dll.add_to_head(10)
dll.add_to_head(20)
dll.add_to_tail(100)
dll.add_to_tail(200)
dll.add_to_tail(300)
dll.add_to_tail(400)
dll.add_to_tail(5000)
dll.add_to_tail(600)
dll.add_to_tail(700)
dll.print_from_n_to_first(7)

