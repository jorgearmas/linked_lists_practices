# Write a Python program to count the number of items of a given doubly linked list.

class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def set_prev_node(self, prev_node_input):
        self.prev_node = prev_node_input
    
    def get_prev_node(self):
        return self.prev_node
    
    def set_next_node(self, next_node_input):
        self.next_node = next_node_input
    
    def get_next_node(self):
        return self.next_node

class DoublyLinkedList():
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    
    def add_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        
        self.head_node =  new_head

        if self.tail_node is None:
            self.tail_node = new_head
    
    def add_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail
    
    def print_foward_linked_list(self):
        str_list = ""
        current_node = self.head_node
        counter = 0

        while current_node is not None:
            str_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
            counter += 1
    
        return str_list +"| No. of items -> "+ str(counter)+" |"

dll = DoublyLinkedList()
dll.add_head(10)
dll.add_head(20)
dll.add_tail(100)
dll.add_tail(200)
dll.add_tail(300)
dll.add_tail(400)
dll.add_tail(5000)
dll.add_tail(600)
dll.add_tail(700)
print(dll.print_foward_linked_list())
