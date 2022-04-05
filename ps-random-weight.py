#https://leetcode.com/discuss/interview-question/1108165/Amazon-or-SDE-II-or-Phone-Screen-Interview-or-USA-or-2021
# Please upvote if you find this helpful. I tried to describe the problem in enough detail.

# Interviewer asked the below question first, then leadership principles / behavioral questions. No system design questions here.

# suppose you receive the data below. Do not focus on the delivery method. You could assume it is a DB table or whatever alternative method you'd like.

# Category ID | item ID | Frequency
# 1.................. | 1 ......... | 10 ....
# 1.................. | 2 ......... | 20 ....
# 2.................. | 3 ......... | 5 ......
# 2.................. | 4 ......... | 30 ....

# item ID refers to a specific item. This item could be any consumer product that we might want to advertise for on our frontend. Category ID refers to the category of items that this item belongs to. a category could be grocery items, smartphones, etc. a specific item ID would refer to, say, samsung galaxy s20, a specific product belonging to the smartphone category. Frequency refers to the frequency at which we want to advertise the given product. If a company pays us more to advertise their product, we will show it more, for example. The frequency number denotes the frequency we want to advertise the item relative to other items. (the interviewer did not explain this that deeply first, but basically, if one item has frequency 20 and the other 10, then the first should be shown 20 times as much as the second).

# write a function that takes a category ID as an argument and returns the item ID as an answer. The item ID returned should be the item we would advertise next. Suppose we have a website with a lot of traffic. We would invoke this function when the website is requested and determine which item to advertise based on your function given a category ID.

# The item ID returned should roughly abide by the frequencies we described above. We mostly care about this when looking at overall numbers.

# One thing we would like is randomness. If the function returns product 3 one time, the next time we would want something different than 3, ideally, so that the user gets different products every time.

# You will probably be storing some form of data on the server about what items users had been shown (as in past return values of the function). Describe how you would store this data to aid your answer.

# Performance here is key (they meant time complexity). Followed by memory usage and order (randomness).
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum=0
        self.prefix_sums=[]
        for weight in w:
            self.prefix_sum+=weight
            self.prefix_sums.append(self.prefix_sum)
        self.total=self.prefix_sum

    def pickIndex(self) -> int:
        r=self.total*random.random()
        for i,prefix_sum in enumerate(self.prefix_sums):
            if r<prefix_sum:
                return i

"""
RandomLoanAccess:

get(customer_id) -> merchant:
For a given customer id, returns the merchant a customer has received a loan for. O(1)

put(customer_id,merchant) -> None: 
Adds a customer id and merchant pair to the to the RandomLoanAccess. O(1)

delete(customer_id) -> None: 
removes a customer id and merchant pair from the RandomLoanAccess data structure. O(n)

get_random_merchant() -> v: 
Randomly returns a merchant from the data stored in RandomLoanAccess. O(1)

{
    "Sherry": "Amazon",
    "Deon": "Amazon",
    "Link": "Peloton",
    "Ash": "Amazon"
}
P(Amazon) = 50%
P(Peloton) = 50%
"""

prefix_sum=0
prefix_sums=[]

count=collections.defautdict(int)

for x in self.data:
    count[self.data[x]]+=1
    
for c in count:
    preefix_sum+=count[c]
    prefix_sums.append(prefix_sum)
total=prefix_sum
r=total*random.random()
for i,p in enumerate(prefix_sums):
    if r<p:
        return i



import random
import collections
class Solution:
    def __init__(self):
        # {customer -> merchant}, []
        self.data=collections.defaultdict(str)
        self.q=[]
        
        
    def put(self,customer_id,merchant)->None:
        if customer_id not in self.q:
            self.q.append(customer_id)
        self.data[customer_id]=merchant
        
    def get_random_merchant(self): 
        # Need to use a list for random selection
        r=random.randrange(0,len(self.q))
        return self.data[self.q[r]]
    
    def get(self,customer_id)->str:
        if customer_id in self.data:
            return self.data[customer_id]
        return None
    
    def delete(self,customer_id)->None:
        if customer_id in self.data:
            del self.data[customer_id]
            self.q.remove(customer_id)
            
c=Solution()
c.put('Sherry',"Amazon")
c.put('yubin','Amazon')
c.put('payton','Google')

for _ in range(3):
    print(c.get_random_merchant())
        





