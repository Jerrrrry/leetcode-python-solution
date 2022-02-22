 #def say_hello():
#    print('Hello, World')

#for i in range(5):
#    say_hello()


# 
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings
# 
# Enjoy your interview!
# 
# 
# hi yubin
# hello

##################################################
##### Paste _all_ output from CoderPad here ######
##################################################

queries = [
     'starbucks cupertino', 
     'McDonalds',
     'apple park',
     'park ave',
     'cupertino ca',
     'Mcdonalds', 
     'mcdonalds',
     'Starbucks',
     'starbucks',
     'cupertino Ca',
     'starbucks ca',
     'starbucks Ca', 
     'mcdonalds SF',
     'apple park',
     'park ave',
     'cupertino ca  ',
     'starbucks Cupertino', 
     'mcdonalds',
     'Apple park',
     'park ave',
     'cupertino ca',
     'starbucks cupertino', 
     'mcdonalds',
     'mcdonalds',
     'mcdonalds',
     'Starbucks',
     'apple park',
     'park ave',
     'cupertino ca',
     ]

#### 1) Find the query count for each query in the list. Make each query undercase and stripped of start/end whitespace ### 
#### Example output - {"mcdonalds": 2, "park ave": 1, ... } ### 


def get_query_counts( queries = None)->dict:
    c={}
    if not queries:
        return c
    
    
    for q in queries:
        tmp=q.lower().strip()
        if tmp not in c:
            c[tmp]=1
        else:
            c[tmp]+=1    
    return c






#### 2) Find the token counts for each query in the list (undercase and stripped of start/end whitespace) ### 
#### Tokens are strings with query separated by whitespace - "park ave" -> ["park","ave"]


def get_token_counts( queries = None):
    c={}
    if not queries:
        return c
    for q in queries:
        tmp=q.lower().strip()
        for x in tmp.split(' '):
            if x not in c:
                c[x]=1
            else:
                c[x]+=1
    
    return c


import heapq
#### 3) Order output of tokens by count popularity.
def get_ordered_token_counts( queries = None):
    
    c=get_token_counts(queries)
    if len(c.keys())==0:
        return []
    q=[]
    
    for key in c:
        heapq.heappush(q,(-c[key],key))
        
    res=[]
    
    while q:
        v,k=heapq.heappop(q)
        #Nlog(N)
        res.append([k,-v])
    
    
    return res

#len(query)+(number of token)* (log (number of token))

#number tokens 

print(get_ordered_token_counts(queries))


c=set()

c.add(newvalue)
c.add(newvalue)

import json
with open(file) as f:
    data=json.load(f)
    
    
machine 65000

/c/b /tmp

inode

easy permission 

/path mount space disk 

database normalization and denormalization