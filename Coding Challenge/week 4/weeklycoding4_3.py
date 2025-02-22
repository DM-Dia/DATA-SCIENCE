class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_dup(head):
    if not head:
        return None

    cur = head

    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

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
        print(cur.val, end="->")
        cur = cur.next
    print("NULL")

# Test Cases
test1 = create_list([11, 11, 11, 13, 13, 20])
print_list(remove_dup(test1))  # Output: 11->13->20

test2 = create_list([10, 15, 15, 15, 20, 20, 20, 23, 25, 25])
print_list(remove_dup(test2))  # Output: 10->15->20->23->25