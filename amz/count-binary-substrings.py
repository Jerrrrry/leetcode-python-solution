def count(s):
        data=[1]

        for i in range(1,len(s)):
                if s[i-1]==s[i]:
                        data[-1]+=1
                else:
                        data.append(1)
        res=0
        for i in range(1,len(data)):
                res+=min(data[i].data[i-1])
        return res