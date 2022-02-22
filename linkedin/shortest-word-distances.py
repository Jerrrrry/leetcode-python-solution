# https://leetcode.com/problems/shortest-word-distance-ii/

class Solution:
        def __init__(self,wordsDict:List[str]):
                self.data=collections.defaultdict(list)
                for i,w in enumerate(wordsDict):
                        self.data[w].append(i)

        def distance(self,w1:str,w2:str)->int:
                l1=self.data[w1]
                l2=self.data[w2]
                res=math.inf
                for i in l1:
                        for j in l2:
                                res=min(res,abs(i-j))
                return res