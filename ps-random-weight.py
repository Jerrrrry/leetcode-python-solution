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