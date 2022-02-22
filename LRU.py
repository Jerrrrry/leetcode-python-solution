import collections

class LRUCache(object):

    def __init__(self,capacity):
        self.capacity=capacity
        self.q=collections.deque()
        self.d=dict()

    def get(self,key):
        if key in self.d.keys():
            value=self.d[key]
            self.q.remove((key,value))
            self.q.append((key,value))
            return self.d[key]
        return -1

    def put(self,key,value):
        keys=self.d.keys()
        if len(self.q)+1>self.capacity and key not in keys:
            k,v=self.q.popleft()
            del self.d[k]
        if key in keys:
            self.q.remove((key,self.d[key]))
        self.q.append((key,value))
        self.d[key]=value
