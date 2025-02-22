class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def reverse(head):
    prev = None
    while head:
        nxt, head.next = head.next, prev
        prev, head = head, nxt
    return prev

def add_two_numbers(l1, l2):
    l1, l2 = reverse(l1), reverse(l2)
    carry, dummy = 0, ListNode()
    current = dummy

    while l1 or l2 or carry:
        carry, val = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry, 10)
        current.next = ListNode(val)
        current = current.next
        l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)

    return reverse(dummy.next)

def create_list(lst):
    head = current = ListNode(lst[0])
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print("->".join(result) + "->NULL")

# Test Cases
l1, l2 = create_list([5, 6, 3]), create_list([8, 4, 2])
print_list(add_two_numbers(l1, l2))  # Output: 1->4->0->5->NULL

l1, l2 = create_list([7, 5, 9, 4, 6]), create_list([8, 4])
print_list(add_two_numbers(l1, l2))  # Output: 7->6->0->3->0->NULL