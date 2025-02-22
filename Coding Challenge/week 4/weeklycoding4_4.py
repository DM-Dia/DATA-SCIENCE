class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev

def create_list(ele):
    if not ele:
        return None
    head = ListNode(ele[0])
    cur = head
    for val in ele[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

def print_list(head):
    cur = head
    while cur:
        print(cur.val, end="->")
        cur = cur.next
    print("NULL")

# Test Cases
test1 = create_list([1, 2, 3, 4])
print_list(reverse_list(test1))  # Output: 4->3->2->1->NULL

test2 = create_list([1, 2, 3, 4, 5])
print_list(reverse_list(test2))  # Output: 5->4->3->2->1->NULL