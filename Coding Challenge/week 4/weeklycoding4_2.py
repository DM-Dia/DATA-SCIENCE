class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def del_mid(head):
    if not head or not head.next:  # If list is empty or has only one node
        return None
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = slow.next
    return head

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
        print(cur.val, end=" ")
        cur = cur.next
    print()

# Test Cases
test1 = create_list([1, 2, 3, 4, 5])
print_list(del_mid(test1))  # Output: 1 2 4 5

test2 = create_list([2, 4, 6, 7, 5, 1])
print_list(del_mid(test2))  # Output: 2 4 6 5 1