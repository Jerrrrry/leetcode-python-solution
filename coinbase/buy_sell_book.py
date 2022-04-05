
import heapq
class Solution: 
        def __init__(self):
                self.sell=[]
                self.buy=[]

        def match(self,price:int,ops:bool)->int:
                res=-1
                if ops:
                        heapq.heappush(self.buy,-price)  
                else:
                        heapq.heappush(self.sell,price)    

                if self.sell and self.buy:
                        b=-heapq.heappop(self.buy)
                        s=heapq.heappop(self.sell)

                        if b>s:
                                res=b
                        else:
                                heapq.heappush(self.buy,-b)
                                heapq.heappush(self.sell,s)
                print(self.buy)
                print(self.sell)
                return res


c=Solution()
print(c.match(1000,False))
print(c.match(2000,False))
print(c.match(500,False))
print(c.match(100,False))
print(c.match(200,True))
print(c.match(300,True))

print(c.match(100,False))
print(c.match(150,False))

class Match:
        def __init__(self):
                self.buy=[]
                self.sell=[]