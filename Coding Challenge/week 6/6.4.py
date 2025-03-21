from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    min_heap = []

    # Push the head of each linked list into the heap
    for l in lists:
        if l:
            heappush(min_heap, l)

    dummy = ListNode()  # Dummy node to simplify list construction
    curr = dummy

    while min_heap:
        # Get the smallest node
        node = heappop(min_heap)
        curr.next = node
        curr = node  # Move pointer

        if node.next:
            heappush(min_heap, node.next)

    return dummy.next  # Return merged list starting from dummy.next

# Input: [[1,4,5],[1,3,4],[2,6]]
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
merged_head = mergeKLists(lists)

# Function to print merged linked list
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

print_list(merged_head)  # Output: [1,1,2,3,4,4,5,6]