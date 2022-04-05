import collections
def bestRate(self,s:str,e:str)->float:
        edges=set()
        graph=self.getGraph()
        paths=collections.defaultdict()
        for e in graph:
                paths[e]=float('inf')
                for x in graph[e]:
                        paths[x]=float('inf')
                        edges.add((e,x))
        
        n=len(paths)

        while n>0:
                for src,end in edges:
                        paths[end]=min(paths[end],paths[src]+graph[src][end])
                n-=1
        
        if paths[e]==float['inf']:
                return -1
        else:
                return paths[e]

#time complacity is number of edges * number verticles 