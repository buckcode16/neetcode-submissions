class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val

        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] 
        
    def insert(self,node):
        prv, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prv
        prv.next = nxt.prev = node


    def remove(self,node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
