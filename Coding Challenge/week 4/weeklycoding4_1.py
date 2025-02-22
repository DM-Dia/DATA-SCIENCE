class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_mid(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print("The middle element is", slow.val)

def create_list(ele):
    if not ele:
        return None
    head = ListNode(ele[0])
    cur = head
    for val in ele[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

# Test Cases
test1 = create_list([2, 3, 4, 5])
find_mid(test1)  # Output: The middle element is 4

test2 = create_list([1, 2, 3, 4, 5])
find_mid(test2)  # Output: The middle element is 3

test3 = create_list([1, 2, 3, 4, 5, 6])
find_mid(test3)  # Output: The middle element is 4