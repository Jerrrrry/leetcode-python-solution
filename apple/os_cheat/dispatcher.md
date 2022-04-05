https://www.geeksforgeeks.org/difference-between-dispatcher-and-scheduler/


1. Long term (job) scheduler – Due to the smaller size of main memory initially all program are stored in secondary memory. When they are stored or loaded in the main memory they are called process. This is the decision of long term scheduler that how many processes will stay in the ready queue. Hence, in simple words, long term scheduler decides the degree of multi-programming of system.


2. Medium term scheduler – Most often, a running process needs I/O operation which doesn’t requires CPU. Hence during the execution of a process when a I/O operation is required then the operating system sends that process from running queue to blocked queue. When a process completes its I/O operation then it should again be shifted to ready queue. ALL these decisions are taken by the medium-term scheduler. Medium-term scheduling is a part of swapping.


3. Short term (CPU) scheduler – When there are lots of processes in main memory initially all are present in the ready queue. Among all of the process, a single process is to be selected for execution. This decision is handled by short term scheduler.
Let’s have a look at the figure given below. It may make a more clear view for you.