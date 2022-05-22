#https://leetcode.com/problems/meeting-rooms-ii/
import heapq
def find(jobs):
        jobs.sort(key=lambda x:x[0])
        q=[]
        heapq.heappush(q,jobs[0][-1])
                
        for i in range(1,len(jobs)):
                if jobs[i][0]>=q[0]:
                        heapq.heappop(q)
                heapq.heappush(q,jobs[i][-1])
                
        return len(q)

#data=[[2,5], [3,6], [5,7]]
#data=[[2,5], [3,6], [5,7], [4,9]]
data=[[2,5], [3,6], [5,7], [3,9], [2,7]]

print(find(data))