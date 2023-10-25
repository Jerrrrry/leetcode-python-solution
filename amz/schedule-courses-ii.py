class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for c, p in prerequisites:
            g[p].append(c)
            degrees[c] += 1
        
        res = []
        q = [i for i, r in enumerate(degrees) if not r]

        while q:
            c = q.pop(0)
            
            for n in g[c]:
                degrees[n] -= 1
                if degrees[n] == 0:
                    q.append(n)

                
            res.append(c)
            
        return res if len(res) == numCourses else []