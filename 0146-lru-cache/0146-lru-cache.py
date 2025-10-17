class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.lru:
            y = self.lru[key]
            self.remove(self.lru[key])
            self.add(y)
            return y.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.remove(self.lru[key])
        elif self.capacity == len(self.lru):
            n = self.head.next
            self.remove(n)
            del self.lru[n.key]
        n = Node(key, value)
        self.add(n)
        self.lru[key] = n
    
    def remove(self, node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre

    def add(self,nn):
        pre = self.tail.prev
        nxt = self.tail
        nn.prev = pre
        nn.next = nxt
        pre.next = nn
        nxt.prev = nn


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)