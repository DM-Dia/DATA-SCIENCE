class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap to store key-node pairs
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node from linked list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node right after head (mark as recently used)
    def _insert(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move to front
            self._insert(node)
            return node.value
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])  # Remove old position

        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self._insert(new_node)

        if len(self.cache) > self.capacity:
            # Remove LRU node from tail
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

lruCache = LRUCache(2)
lruCache.put(1, 1)  # cache = {1=1}
lruCache.put(2, 2)  # cache = {1=1, 2=2}
print(lruCache.get(1))  # Output: 1
lruCache.put(3, 3) # cache = {1=1, 3=3}
print(lruCache.get(2))  # Output: -1
lruCache.put(4, 4)  # cache = {3=3, 4=4}
print(lruCache.get(1))  # Output: -1
print(lruCache.get(3))  # Output: 3
print(lruCache.get(4))  # Output: 4