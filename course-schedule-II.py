class Solution:
    def findOrder(self,numCourse:int,prerequisites:List[List[int]])->List[int]:
        graph=collections.defaultdict(list)
        indegress=collections.default(int)
        res=[]
        for u,v in prerequisites:
            graph[v].append(u)
            indegrees[u]+=1
        for i in range(numCourse):
            found=False
            for j in range(numCourse):
                if indegrees[j]==0:
                    found=True
                    break
            if not found :return []
            indegrees[j]=-1
            res.append(j)
            for node in graph[j]:
                indegrees[node]-=1
        return res