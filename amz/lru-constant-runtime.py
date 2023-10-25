import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.c=capacity
        self.data=collections.OrderedDict()
    
    def dna(self,key:int)->None:
        v=self.data[key]
        del self.data[key]
        self.data[key]=v

    def get(self, key: int) -> int:
        if key in self.data:
            self.dna(key)
        return self.data.get(key,-1)
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.dna(key)
        else:
            if len(self.data)==self.c:
                self.data.popitem(last=False)
        self.data[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)