class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data=collections.defaultdict(list)
        q=[]
        for i in range(len(username)):
            heapq.heappush(q,(timestamp[i],username[i],website[i]))
            
        while q:
            t,u,w=heapq.heappop(q)
            data[u].append(w)
        freq=collections.defaultdict(int)
        mv=0
        res=tuple()
        for u in data:
            cbs=combinations(data[u],3)
            
            for cb in set(cbs):
                freq[cb]+=1
                if freq[cb]>mv:
                    mv=freq[cb]
                    res=cb
                elif freq[cb]==mv:
                    if cb<res:
                        res=cb
        return res