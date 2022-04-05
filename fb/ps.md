Welcome to Meta!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!

You are given an integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:

 "a->b" if a != b
 "a" if a == b
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Input:  [0,2,3,4,6,8,9]
    
0
2-4
6
8-9

// sorted 
// duplicates



def numrange(nums):
    res=[]
    n=len(nums)
    i=0
    while i<n:
        tmp=i
        while (nums[tmp]+1==nums[tmp+1] or nums[tmp]==nums[tmp+1]) and tmp<n-1:
            tmp+=1
        res.append(str(nums[i])+'->'+str(nums[tmp-1]))
        i=tmp
        
    return res
            
        
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
    
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
    
// traverse all current intervals
// if result is empty / non-overlapping (previous added interval and ni)
// add current interval
// else  merge interval

//update result 
    
    
def buildintervals(intervals,ni):
    q=[]
    intervals.append(ni)
    intervals.sort(key=lambda x:x[0])
    
    for i in range(len(intervals)-1):
        if not q or intervals[i][0]>q[-1][1]:
            q.append(intervals[i])
        else:
            if intervals[i][1]>q[-1][1]:
                q[-1][-1]=intervals[i][-1]
                
    return q
            