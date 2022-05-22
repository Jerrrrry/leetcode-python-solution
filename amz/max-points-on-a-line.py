from typing import List
import collections
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        mv=1
        
        for i,p1 in enumerate(points[:-1]):
            data=collections.defaultdict()
            
            for p2 in points[i+1:]:
                
                if p1[0]==p2[0]:
                    m='inf'
                    c=p1[0]
                else:
                    m=(p1[1]-p2[1])/(p1[0]-p2[0])
                    c=p1[1]-m*p1[0]
                    
                data[(m,c)]=data.setdefault((m,c),1)+1
                
            mv=max(mv,max(data.values()))
            
        return mv