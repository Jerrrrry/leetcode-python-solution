What is Kernal? (V. Imp)
Whenever a system starts, the Kernel is the first program that is loaded after the bootloader because the Kernel has to handle the rest of the thing of the system for the Operating System. The Kernel remains in the memory until the Operating System is shut-down.


What is a process in OS and What are the different states of a process?



What is a Scheduling Algorithm? Name different types of scheduling algorithms.
What do you mean by FCFS Algorithm and best advantages of it?
What is virtual memory?
What is thread in OS?

what is tlb
What is Cache ? (Use a Example)
What is the difference between paging and segmentation?
What is thrashing in OS?

What is an Inode in unix file system?
An Inode is a data structure containing metadata about the files.
Uniquely existing number for all the files in linux/unix filesystem.
The first number on the left indicates the inode number. -i flag is used to get the inode number Note: The Inode doesn't contain file content, instead it has a pointer to that data.

What are Zombie Processes and how to kill them?

A process which has finished the execution but still has entry in the process table to report to its parent process is known as a zombie process.

How to kill Zombie Process
You can’t kill a zombie process because it’s already dead. It won’t respond to any signals because it’s been removed from memory—there’s nowhere to send a SIGKILL signal. You can try sending the SIGCHLD signal to the parent process, but if it didn’t work when the child process terminated, it’s unlikely to work now, either.

The only reliable solution is to kill the parent process. When it’s terminated, its child processes are inherited by the init process, which is the first process to run in a Linux system (its process ID is 1).

What is Samba Server?


When is multi threading not useful?
What is TLB?
DIfference between Paging and Segmentation?
What is Paging?
What is Virtual Memory?
What is Page fault?
What is Cache?


how to check/do if sys is frozen 
check cpu usage to see it's a busy-run issue or a deadlock/waiting issue.
use strace if busy-run, dump stack if deadlock.

This was discussion question asked during phone interview. Started with abstract ans and lead to kernel level memory management (i-node, memory pointers etc) Basically interviewer was interested in knowing how deep you can go. (~23-25min)

Start with the basics: Memory leak occurs when you allocate memory to heap, but do not manually garbage collect (de-allocate memory) when objects are no longer relevant. So you have an entity allocating heap memory, but no entity deallocating the memory when no longer needed. - obviously this pertains to languages like C/C++, not Java, C# which possess garbage collection mechanisms under the hood. Now you can breakdown your knowledge/understanding of how/where memory is laid out (stack memory allocation, memory hierarchy: cache l1,l2,l3 ,pages, virtual memory, DRAM, performance optimizations like TLB).
