#https://leetcode.com/discuss/interview-experience/923447/coinbase-sde-bay-area-2020-reject

#https://api.pro.coinbase.com/products/" + id + "/book

# https://api.pro.coinbase.com/products
import requests
import json 
import collections
import sys
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
                        res['bid']=req['bids'][0][1]
                        res['ask']=req['asks'][0][1]
                        print(res)
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
                data=open('demo.json')
                data=json.load(data)['data']
                r=collections.defaultdict(dict)

                for d in data:
                        src,to=d['start'],d['to']
                        r[src][to]=float(d['ask'])
                        r[to][src]=1/float(d['bid'])
                print(r)
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
                def backtrack(current,seen,p):
                        if current==e:
                                print(p)
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

c=Currency()
print(c.bestRateBack('USD','BTC'))