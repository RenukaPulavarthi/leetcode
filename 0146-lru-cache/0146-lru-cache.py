class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        

    def get(self, key: int) -> int:
        if key in self.dict:
            n=self.dict[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        n=Node(key,value)
        self._add(n)
        self.dict[key]=n
        if len(self.dict) > self.capacity:
            n=self.head.next
            self._remove(n)
            del self.dict[n.key]

    def _remove(self,node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p

    def _add(self,node):
        k=self.tail.prev
        node.next=self.tail
        node.prev=k
        k.next=node
        self.tail.prev=node       


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)