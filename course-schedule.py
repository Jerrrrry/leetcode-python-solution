class Solution:
    def canFinish(self,numCourses:int,prerequisites:List[List[int]])->bool:
        indegrees=collections.defaultdict(int)
        graph=collections.defaultdict(list)
        for u,v in prerequisites:
            indegrees[u]+=1
            graph[v].append(u)
        for i in range(numCourses):
            found=False
            for j in range(numCourses):
                if indegrees[j]==0:
                    found=True
                    break
            if not found:return False
            indegrees[j]=-1
            for node in graph[j]:
                indegrees[node]-=1
        return True