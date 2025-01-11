class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def set_next_node(self, next_node_input):
        self.next_node = next_node_input
    
    def get_next_node(self):
        return self.next_node

class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def print_list(self):
        current_node = self.head_node
        while current_node is not None:
            print(current_node.get_value())
            current_node = current_node.get_next_node()
    
    def remove_first(self):
        first_node = self.head_node

        if first_node is None:
            return "The list is empty"
        else:
            self.head_node = first_node.get_next_node()
            first_node.set_next_node(None)
            return f"{first_node.get_value()} has been deleted" 

    def remove_by_value(self, value):
        current_node = self.head_node

        if current_node is None:
            return "The list is empty"
        elif current_node.get_value() == value:
            return self.remove_first()
        else:
            while current_node is not None:
                next_node = current_node.get_next_node()
                if next_node is None:
                    return 'Value not found'
                else:
                    if next_node.get_value() == value:
                        current_node.set_next_node(next_node.get_next_node())
                        next_node.set_next_node(None)
                        return f"{next_node.get_value()} has been deleted" 
                    current_node = next_node
                    
my_linked_list = LinkedList(5)
my_linked_list.insert_beginning(10)
my_linked_list.insert_beginning(15)
my_linked_list.insert_beginning(20)
my_linked_list.insert_beginning(2500)
my_linked_list.insert_beginning(30)
my_linked_list.insert_beginning(40)

print(my_linked_list.remove_by_value(10))
print('')
my_linked_list.print_list()
