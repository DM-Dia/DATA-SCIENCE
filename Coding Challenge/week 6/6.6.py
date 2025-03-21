class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delDup(head: ListNode) -> ListNode:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # Skip the duplicate node
        else:
            current = current.next  # Move to the next node
    return head

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list for easy comparison
def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head1 = createLinkedList([1, 1, 2])
print(linkedListToList(delDup(head1)))  # Output: [1, 2]

head2 = createLinkedList([1, 1, 2, 3, 3])
print(linkedListToList(delDup(head2)))  # Output: [1, 2, 3]