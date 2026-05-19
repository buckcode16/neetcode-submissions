class MyHashSet:

    def __init__(self):
        self.hs = []
        

    def add(self, key: int) -> None:
        if key not in self.hs:
            self.hs.append(key)
        

    def remove(self, key: int) -> None:
        if not len(self.hs):
            return None
        i = 0
        while i < len(self.hs):
            if self.hs[i] == key:
                self.hs.pop(i)
                break
            i+=1

    def contains(self, key: int) -> bool:
        if not len(self.hs):
            return False
        i = 0
        while i < len(self.hs):
            if self.hs[i] == key:
                return True
            i+=1
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)