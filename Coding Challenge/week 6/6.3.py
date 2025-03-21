class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        sum_val = carry  # Start with carry

        if l1:
            sum_val += l1.val
            l1 = l1.next  # Move to next node

        if l2:
            sum_val += l2.val
            l2 = l2.next  # Move to next node

        # Compute new digit and update carry
        carry, digit = divmod(sum_val, 10)

        # Add new node to result list
        curr.next = ListNode(digit)
        curr = curr.next

    return dummy.next

# Input: l1 = [2,4,3], l2 = [5,6,4]
list1 = ListNode(2, ListNode(4, ListNode(3)))
list2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(list1, list2)

# Function to print linked list
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

print_list(result)  # Output: [7,0,8]