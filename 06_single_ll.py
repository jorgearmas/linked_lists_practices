# Write a Python program to delete the first item from a singly linked list

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def delete_first_item(self):
        current_node = self.head_node
        current_node = current_node.get_next_node()
        self.head_node = current_node

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
my_linked_list.delete_first_item()
my_linked_list.print_list()