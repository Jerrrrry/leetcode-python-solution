from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
            res=0
            data=collections.defaultdict(int)
            for t in time:
                key=t%60
                if key==0:
                        res+=data[0]
                else:
                        res+=data[60-key]
                data[key]+=1
            return res