#Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.
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
    
    def search_by_value(self, value_to_search):
        is_value_in_list = False
        current_node = self.head_node
        while current_node is not None:
            if current_node.get_value() == value_to_search:
                is_value_in_list =  True
            current_node = current_node.get_next_node()
        return is_value_in_list

my_linked_list = LinkedList(5)
my_linked_list.insert_beginning(10)
my_linked_list.insert_beginning(15)
my_linked_list.insert_beginning(20)
my_linked_list.insert_beginning(25)
my_linked_list.insert_beginning(30)
my_linked_list.insert_beginning(40)

print(f"Is the value (40) in the linked list? {my_linked_list.search_by_value(15)}")
print(f"Is the value (7) in the linked list? {my_linked_list.search_by_value(7)}")

