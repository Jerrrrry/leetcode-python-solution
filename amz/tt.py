import random
def generate():
    data=[[0]*5 for _ in range(5)]
    d=[1,15]
    
    for i in range(5):
        v=set()
        c=[x for x in range(d[0],d[1]+1)]
        for j in range(5):
            while True:
                r=random.choice(c)
                if r not in v:
                    v.add(r)
                    data[j][i]=r
                    break
            
        d[0]+=15
        d[1]+=15
    return data

data=generate()

for x in data:
        print(x)