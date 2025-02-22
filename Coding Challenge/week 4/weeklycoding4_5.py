class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev

def addOne(head):
    head = reverse(head)  # Reverse list
    curr, carry = head, 1

    while curr:
        curr.val += carry
        carry, curr.val = divmod(curr.val, 10)
        if not carry:
            break
        if not curr.next and carry:
            curr.next = ListNode(0)
        curr = curr.next

    return reverse(head)  # Reverse back

# Helper functions
def create_list(num):
    head = ListNode(int(str(num)[0]))
    curr = head
    for digit in str(num)[1:]:
        curr.next = ListNode(int(digit))
        curr = curr.next
    return head

def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("NULL")

# Test Cases
test1 = create_list(1999)
print_list(addOne(test1))  # Output: 2->0->0->0->NULL

test2 = create_list(3453)
print_list(addOne(test2))  # Output: 3->4->5->4->NULL