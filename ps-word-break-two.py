def Solution:
        def breakdown(self,words:List[str],s:str)->List[str]:
                words=set(words)
                data=collections.defaultdict(list)
                def breakdown(s):
                        if not s:
                                return [[]]
                        if s in data:
                                return data[s]
                        for e in range(1,len(s)+1):
                                tmp=s[:e]
                                if tmp in words:
                                        for cs in breakdown(s[e:]):
                                                data[s].append([tmp]+cs)
                        return data[s]
                breakdown(s)

                return [' '.join(w) for w in data[s]]