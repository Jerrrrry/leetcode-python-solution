class Solution:
        def canWin(self,m:int,t:int)->bool:
                v={}

                def win(data,target):
                        if data[-1]>=target:
                                return 

                        k=tuple(data)
                        if k in v:
                                return v[k]
                        
                        for i in range(len(data)):
                                if not win(data[:i]+data[i+1:],target-data[i]):
                                        v[k]=True
                                        return True
                        v[k]=False
                        return False

                mv=(m+1)*m/2
                if mv<t:
                        return False
                if mv==t:
                        return m%2
                return win(list([i for i in range(1,m+1)]),t)

##tc t*2^m   sc 2^m