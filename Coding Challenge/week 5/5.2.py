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

    def max_twin_sum(self):
        # Step 1: Find the middle of the linked list
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Calculate max twin sum
        max_sum = 0
        first, second = self.head, prev
        while second:
            max_sum = max(max_sum, first.data + second.data)
            first = first.next
            second = second.next

        return max_sum

def create_linked_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.insert_at_end(value)
    return linked_list

# Test Case 1
ll1 = create_linked_list([5, 4, 2, 1])
print(ll1.max_twin_sum())  # Expected Output: 6

# Test Case 2
ll2 = create_linked_list([4, 2, 2, 3])
print(ll2.max_twin_sum())  # Expected Output: 7