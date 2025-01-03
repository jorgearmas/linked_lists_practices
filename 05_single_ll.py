# Write a Python program to set a new value of an item in a singly linked list using index value.
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
    
class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def insert_by_index(self, value, index_input):
        if index_input < 0:
            return f"Indexes cannot be less than 0"
        
        current_node = self.head_node
        next_node = current_node.get_next_node()
        index = 0

        if index_input == 0:
            self.insert_beginning(value)
        else:
            while current_node is not None:
                index += 1
                if index == index_input:
                    new_node = Node(value)
                    new_node.set_next_node(next_node)
                    current_node.set_next_node(new_node)
                    break
                current_node = next_node
                next_node = current_node.get_next_node()
        
    def print_list(self):
        current_node = self.head_node
        while current_node:
            print(current_node.get_value())
            current_node = current_node.get_next_node()

        
my_linked_list = LinkedList(5)
my_linked_list.insert_beginning(10)
my_linked_list.insert_beginning(15)
my_linked_list.insert_beginning(20)
my_linked_list.insert_beginning(25)

my_linked_list.insert_by_index(500, 2)
my_linked_list.print_list()