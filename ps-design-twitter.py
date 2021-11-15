#https://leetcode.com/discuss/interview-question/1270434/Amazon-or-SDEII-or-Phone-Screen-or-High-CoL

import time
import collections
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.twitter=collections.defaultdict(list)
        self.following=collections.defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.twitter[userId].append((tweetId,time.time()))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        
        """
        data=[]
        for t in self.twitter[userId]:
                data.append(t)
        for f in self.following[userId]:
                if f==userId:continue
                for t in self.twitter[f]:
                        data.append(t)
        data.sort(key=lambda x:x[1],reverse=True)
        return list(map(lambda x:x[0],data))[:10]        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.following[followerId]:
                self.following[followerId].remove(followerId)