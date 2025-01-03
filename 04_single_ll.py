 # Write a Python program to access a specific item in a singly linked list using index value.
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
    
    def search_by_index(self, index_input):
        if index_input < 0:
            return f"Indexes cannot be less than 0"
        
        current_node = self.head_node
        current_position = 0

        while current_node:
            if current_position == index_input:
                return f"The index [{current_position}] has the value of ({str(current_node.get_value())})"
            current_node = current_node.get_next_node()
            current_position += 1

        return f"Index [{str(index_input)}] does not exist within linked list"
    
    def print_list(self):
        current_node = self.head_node
        position = 0
        while current_node:
            print(f"Node - {current_node.get_value()} is at position [{position}]")
            current_node = current_node.get_next_node()
            position += 1

my_linked_list = LinkedList(5)
my_linked_list.insert_beginning(10)
my_linked_list.insert_beginning(15)
my_linked_list.insert_beginning(25)
my_linked_list.insert_beginning(30)
my_linked_list.insert_beginning(35)
my_linked_list.print_list()

print(my_linked_list.search_by_index(5))