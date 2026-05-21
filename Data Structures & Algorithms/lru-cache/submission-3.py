class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].value

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]            

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next = nxt
        node.prev = prv



    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt,prv

        
