class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        if not self.head:
            self.head = Node(value)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(value)

    def merge_sorted_lists(self, list1, list2):
        dummy = Node(0)
        current = dummy

        while list1 and list2:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach any remaining nodes
        current.next = list1 if list1 else list2

        return dummy.next  # Return the head of the merged list

    def print_list(self, head):
        temp = head
        while temp:
            print(temp.data, end="->" if temp.next else "")
            temp = temp.next
        print()


def create_linked_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.insert_at_end(value)
    return linked_list.head

# Test Cases
ll = LinkedList()

# Example 1
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_head = ll.merge_sorted_lists(list1, list2)
ll.print_list(merged_head)  # Expected Output: 1->1->2->3->4->4

# Example 2
list1 = create_linked_list([])
list2 = create_linked_list([])
merged_head = ll.merge_sorted_lists(list1, list2)
ll.print_list(merged_head)  # Expected Output: (empty list)

# Example 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
merged_head = ll.merge_sorted_lists(list1, list2)
ll.print_list(merged_head)  # Expected Output: 0