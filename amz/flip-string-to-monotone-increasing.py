#https://leetcode.com/problems/flip-string-to-monotone-increasing/

def minFlipsMonoIncr(s: str):
        data=[0]

        for c in s:
                data.append(data[-1]+int(c))
        res=[]
        for i in range(len(data)):
                res.append(data[i]+len(s)-i-(data[-1]-data[i]))

        return min(res)