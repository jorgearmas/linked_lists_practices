# Write a Python program to swap two nodes within a list
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
    
    def print_list(self):
        current_node = self.head_node
        while current_node is not None:
            print(current_node.get_value())
            current_node = current_node.get_next_node()
    
    def swap_nodes(self, val1, val2):
        node1 = self.head_node
        node2 = self.head_node
        node1_prev = None
        node2_prev = None

        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1_prev is None:
            node2_prev.set_next_node(node2.get_next_node())
            node2.set_next_node(node1.get_next_node())
            node1.set_next_node(node2_prev.get_next_node())
            node2_prev.set_next_node(node1)
            self.head_node = node2
        
        if node2_prev is None:
            node1_prev.set_next_node(node1.get_next_node())
            node1.set_next_node(node2.get_next_node())
            node2.set_next_node(node1_prev.get_next_node())
            node1_prev.set_next_node(node2)
            self.head_node = node1
        
        node2_prev.set_next_node(node2.get_next_node())
        node1_prev.set_next_node(node2)
        node2.set_next_node(node1.get_next_node())
        node1.set_next_node(node2_prev.get_next_node())
        node2_prev.set_next_node(node1)

        # if node2_prev is not None:
        #     print('vox')
        #     node1_prev.set_next_node(node1.get_next_node())
        #     node2_prev.set_next_node(node1)
        #     node1.set_next_node(node2.get_next_node())
        #     node2.set_next_node(node1_prev.get_next_node())
        #     node1_prev.set_next_node(node2)
            
my_linked_list = LinkedList(10)
my_linked_list.insert_beginning(20)
my_linked_list.insert_beginning(30)
my_linked_list.insert_beginning(40)
my_linked_list.insert_beginning(500)
my_linked_list.insert_beginning(60)
my_linked_list.insert_beginning(70)
my_linked_list.insert_beginning(80)
my_linked_list.insert_beginning(90)
my_linked_list.insert_beginning(1000)

my_linked_list.swap_nodes(500, 20)
my_linked_list.print_list()


