#Write a Python program to find the size of a singly linked list.

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node_input):
        self.next_node = next_node_input
    
class LinkedList():
    def __init__(self, value):
        self.head_node = Node(value)
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def get_size(self):
        counter = 0
        current_node = self.head_node
        while current_node:
            counter += 1
            current_node = current_node.get_next_node()
        
        return f"The linked list has ({counter}) elements"
    
my_linked_list = LinkedList(5)
my_linked_list.insert_beginning(10)
my_linked_list.insert_beginning(15)
my_linked_list.insert_beginning(20)

print(my_linked_list.get_size())