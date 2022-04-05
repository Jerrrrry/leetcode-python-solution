data=[[1,2,3,4,5] for _ in range(5)]
print(data)
col=[]
for c in range(5):
        res=[]
        for i in range(5):
                res.append(data[i][c])
        col.append(res)
print(col)