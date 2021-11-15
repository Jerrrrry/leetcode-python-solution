import heapq
from collections import OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {} # each entry key, tuple(useCount, value)
        self.capacity = capacity
        self.counterHeap = [] # Using a heap allow us to do heap[0] to get the minor number
        self.keysByUseCount = {} # key: counter, value: OrderDictionary{cacheKey, True} <-- The ordered dictionary allos to have the LRU with easy access (would be better to have an OrderedSet)

    def get(self, key: int) -> int:
        if key in self.cache:
            cacheEntry = self.cache.get(key)
            count = cacheEntry[0] + 1
            self.cache[key] = (count, cacheEntry[1])
            self.updateLFU(count, key)
            return cacheEntry[1]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # Basic use cases..
        if self.capacity == 0:
            return            

        ## Count the usage of the key
        count = 1
        if key in self.cache:
            cacheEntry = self.cache.get(key)
            count = 1 + cacheEntry[0] 

        ## If there is no capacity to add another key
        if len(self.cache) >= self.capacity and key not in self.cache:
            ## The keysByUseCount map may have been updated so min could be different
            while self.counterHeap[0] not in self.keysByUseCount:
                heapq.heappop(self.counterHeap)
            
            minKey = self.keysByUseCount[self.counterHeap[0]].popitem(last=False)[0]
            del self.cache[minKey]
            if len(self.keysByUseCount[self.counterHeap[0]]) == 0:
                del self.keysByUseCount[self.counterHeap[0]]

        self.cache[key] = (count, value)
        self.updateLFU(count, key)
        
                
    
    def updateLFU(self, count, key):
        if count not in self.keysByUseCount:
            heapq.heappush(self.counterHeap, count)
        self.keysByUseCount[count] = self.keysByUseCount.get(count, OrderedDict())
        self.keysByUseCount[count][key] = True
        
        ## If we are adding an item that was added before, we should update the count - 1
        if count > 1:
            if key in self.keysByUseCount[count - 1]:
                del self.keysByUseCount[count - 1][key]
            if len(self.keysByUseCount[count - 1]) == 0:
                del self.keysByUseCount[count -1]
                if self.counterHeap[0] == count - 1:
                    heapq.heappop(self.counterHeap)