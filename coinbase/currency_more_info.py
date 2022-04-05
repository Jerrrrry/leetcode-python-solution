#https://leetcode.com/discuss/interview-experience/923447/coinbase-sde-bay-area-2020-reject

#https://api.pro.coinbase.com/products/" + id + "/book

# https://api.pro.coinbase.com/products
import requests
import json 
import collections
import sys
import heapq
from functools import lru_cache
class Currency:
        def __init__(self):
                self.ids_url='https://api.pro.coinbase.com/products'
                self.data=[]



        def getIds(self):
                prods=requests.get(self.ids_url).json()
                return prods

        def getBidAsk(self,id:str):
                try:
                        url="https://api.pro.coinbase.com/products/" + id + "/book"
                        req=requests.get(url).json()
                        res={}
                        res['start']=id.split('-')[0]
                        res['to']=id.split('-')[1]
                        res['bid']=req['bids'][0][0]
                        res['ask']=req['asks'][0][0]
                        self.data.append(res)
                except Exception as error:
                        print(error)
 


        def createFile(self):
                ids=self.getIds()
                for id in ids:
                        self.getBidAsk(id['id'])
                results={}
                results['data']=self.data

                with open("demo.json", "w") as outfile:
                        json.dump(results, outfile)

        def findPaths(self):
                data=open('demo.json')
                data=json.load(data)['data']
                r=collections.defaultdict(list)

        def getGraph(self):
                f=open('demo.json')
                data=json.load(f)['data']
                r=collections.defaultdict(dict)
                print(len(data))
                for d in data[:300]:
                        src,to=d['start'],d['to']
                        r[src][to]=float(d['ask'])
                        r[to][src]=1/float(d['bid'])
                f.close()
                return r


        def bestRate(self,s:str,e:str):
                #tc n*len(edges)
                path=collections.defaultdict()
                edges=set()
                g=self.getGraph()

                for x in g:
                        path[x]=float('inf')
                        for y in g[x]:
                                path[y]=float('inf')
                                edges.add((x,y))
                path[s]=0

                n=len(g)
                while n>0:
                        for start,to in edges:
                               path[to]=min(path[to],path[start]+g[start][to])
                        n-=1
                return path[e] 
        def bestRateBack(self,s:str,e:str):
                #tc n!
                sys.setrecursionlimit(1000000)
                graph=self.getGraph()
                res=[]
                def backtrack(current,seen,p):
                        if current==e:
                                return 1
                                
                        product=0

                        if current in graph:
                                for nei in graph[current]:
                                        if nei not in seen:
                                                seen.add(nei)
                                                product=max(product,graph[current][nei]*backtrack(nei,seen,p+[nei]))
                                                seen.remove(nei)
                        return product
                return backtrack(s,{s},[s])    

        def convert_currency(self, source, dest):
                graph = self.getGraph()

                # Create the graph of the rates with currencies as edges
                # Edge: s1 -> (s2,rate)
                # Opposite edge: s2 -> (s1, 1/rate)
                # for s1, s2, rate_val in rates:
                #         graph[s1].append((s2, rate_val))
                #         graph[s2].append((s1, 1 / rate_val))

                # pprint(graph, indent=4) Print graph if needed

                visited = set()

                def convert_currency_helper(currency, curr_rate, min_rate):
                        sys.setrecursionlimit(1000000)
                        if currency == dest:
                                return min(min_rate, curr_rate)

                        visited.add(currency)
                        neighbours = graph.get(currency)
                        
                        # Recurse over the currency neighbours and find the min rate
                        for neighbour, rate in neighbours:
                                if neighbour not in visited:
                                        min_rate = convert_currency_helper(neighbour, rate * curr_rate, min_rate)
                        return min_rate

                return convert_currency_helper(source, 1, float("inf"))  

        def betterBack(self,start:str,end:str):
                sys.setrecursionlimit(1000000)
                graph=self.getGraph()
                res=[]
                
                def backtrack(c,value,seen,p):
                        if c==end:
                                res.append((value,p))
                                return
                        for nei in graph[c]:
                                if nei in seen: continue
                                seen.add(nei)
                                backtrack(nei,value*graph[c][nei],seen,p+[nei])
                                seen.remove(nei)
                
                backtrack(start,1,{start},[start])
                mv=float('-inf') 
                pa=None
                for x in res:
                    if x[0]>mv:
                            mv=x[0]
                            pa=x[1]
                print(pa)   
                return mv
                        
        def best_rate_dfs(self,start:str,end:str):
                graph=self.getGraph()
                q=collections.deque()
                res=[]
                def dfs(cur,value,path):
                        if cur==end:
                                res.append((value,path))
                                return
                        for x in graph[cur]:
                                if x not in path:
                                        dfs(x,value*graph[cur][x],path+[x])
                dfs(start,1,[start])
                mv=-1
                p=None
                for r in res:
                        if r[0]>mv:
                                mv=r[0]
                                p=r[1]
                print(p)
                return mv

c=Currency()
#c.createFile()
#print(c.convert_currency('USD','BTC'))
# s=c.bestRate('BTC','USD')
# print(s)

print(1/c.best_rate_dfs('USD','BTC'))

# for x in d:
#         if s==x[0]:
#                 print(x)

#c.getGraph()
x=c.betterBack('USD','BTC')

print(1/x)

