class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        n = ListNode(value, key)
        self.add(n)
        if len(self.cache) == self.capacity:
            z =self.head.next.key
            self.remove(self.cache[z])
            del self.cache[z]

        self.cache[key] = n
    
    def add(self, node):
        p = self.tail.prev
        n = self.tail
        node.next = n
        node.prev = p
        p.next = node
        n.prev = node

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)