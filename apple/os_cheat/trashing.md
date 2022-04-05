Causes of Thrashing :  

High degree of multiprogramming : If the number of processes keeps on increasing in the memory then the number of frames allocated to each process will be decreased. So, fewer frames will be available for each process. Due to this, a page fault will occur more frequently and more CPU time will be wasted in just swapping in and out of pages and the utilization will keep on decreasing. 
For example: 
Let free frames = 400 
Case 1: Number of process = 100 
Then, each process will get 4 frames. 

Case 2: Number of processes = 400 
Each process will get 1 frame. 
Case 2 is a condition of thrashing, as the number of processes is increased, frames per process are decreased. Hence CPU time will be consumed in just swapping pages. 
 

Lacks of Frames: If a process has fewer frames then fewer pages of that process will be able to reside in memory and hence more frequent swapping in and out will be required. This may lead to thrashing. Hence sufficient amount of frames must be allocated to each process in order to prevent thrashing.
Recovery of Thrashing :  

1. Do not allow the system to go into thrashing by instructing the long-term scheduler not to bring the processes into memory after the threshold.
2. If the system is already thrashing then instruct the mid-term schedular to suspend some of the processes so that we can recover the system from thrashing.


Swapping is necessary for two important reasons. First, when the system requires more memory than is physically available, the kernel swaps out less used pages and gives memory to the current application (process) that needs the memory immediately. Second, a significant number of the pages used by an application during its startup phase may only be used for initialization and then never used again. The system can swap out those pages and free the memory for other applications or even for the disk cache.


https://microcontrollerslab.com/difference-between-long-term-and-short-term-scheduler-in-the-operating-system/

long term schedule(job scheduler) pick process from job pool, to main memory and ready queue 

short term scheduler(cpu scheduler) push process from queue to cpu

short term scheduler pick process with different schedling algrit Round Robin, last in first out, earliest deadline first, rate monotonic and least laxity first.