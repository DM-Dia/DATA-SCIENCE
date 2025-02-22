class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def find_second_last(head):
    if not head or not head.next:
        return None  # No second last element if list is empty or has one node

    while head.next.next:  # Stop at second last node
        head = head.next

    return head.val

def create_linked_list():
    values = list(map(int, input("Enter elements of the linked list separated by spaces: ").split()))
    if not values:
        return None
    head = current = ListNode(values[0])
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Taking user input
head = create_linked_list()
result = find_second_last(head)

if result is not None:
    print("Second last element:", result)
else:
    print("No second last element (list too short).")