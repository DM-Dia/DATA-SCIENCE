class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->" if temp.next else "")
            temp = temp.next
        print()

def create_linked_list(values):
    linked_list = LinkedList()
    for value in reversed(values):
        linked_list.insert_at_beginning(value)
    return linked_list

# Test Case 1
ll1 = create_linked_list([2, 3, 4, 5])
ll1.insert_at_beginning(1)
ll1.print_list()  # Expected Output: 1->2->3->4->5

# Test Case 2
ll2 = create_linked_list([3, 2, 5, 7, 1, 2])
ll2.insert_at_beginning(9)
ll2.print_list()  # Expected Output: 9->3->2->5->7->1->2