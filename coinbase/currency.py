#https://leetcode.com/discuss/interview-question/1647092/coinbase-virtual-on-site-interview-questions
#practice https://leetcode.com/problems/path-with-maximum-probability/
# Bid: The bid price refers to the highest price a buyer will pay for a commodity or security.
# Ask: The ask price refers to the lowest price a seller will accept for a commodity or security.
# If A is purchasing BTC for USD from B, B will "ask" certain price and A will agree to pay certain amount of USD ("bid") for 1 BTC.
# So basically the seller is saying 1 BTC = ask USD. Buyer is quoting that they can pay bid USDs for 1 BTC i.e. 1 USD is equivalant to 1/bid BTC.
# This will help you form edge weights of your graph i.e BTC -> USD = ask and USD -> BTC = 1/bid
import collections
from typing import List
import json
def bellman_ford(start, end, graph):
    paths = dict()
    edges = set()
    for key in graph:
        paths[key] = float('inf')
        for item in graph[key]:
            paths[item] = float('inf')
            edges.add((key, item))

    paths[start] = 0
    n = len(paths)
    print(edges)
    i = 0
    while i < n:
        for edge in edges:
            src, tgt = edge[0], edge[1]
            paths[tgt] = min(paths[tgt], graph[src][tgt] + paths[src])
        i += 1
    print(paths)
    return paths[end]

g = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "D": 2, "E": 2, "C": 5},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "D": 1, "C": 5},
    "C": {"B": 5, "E": 5}
}

#print(bellman_ford('A', 'C', g))

data=open("data.json")

d=json.load(data)

r=collections.defaultdict()

for x in d['data']:
        src,target=x['id'].split('-')
        print('src:'+src)
        print('target: '+target)
        if src not in r:
                r[src]={}
        r[src][target]=float(x['asks'][0][1])
        if target not in r:
                r[target]={}
        r[target][src]=1/(float(x['bids'][0][1]))
print(r)

print(bellman_ford('USD', 'BTC', r))