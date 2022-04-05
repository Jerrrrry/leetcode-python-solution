A translation lookaside buffer (TLB) is a memory cache that stores the recent translations of virtual memory to physical memory.

To overcome this problem a high-speed cache is set up for page table entries called a Translation Lookaside Buffer (TLB). Translation Lookaside Buffer (TLB) is nothing but a special cache used to keep track of recently used transactions. TLB contains page table entries that have been most recently used. Given a virtual address, the processor examines the TLB if a page table entry is present (TLB hit), the frame number is retrieved and the real address is formed. If a page table entry is not found in the TLB (TLB miss), the page number is used as index while processing page table. TLB first checks if the page is already in main memory, if not in main memory a page fault is issued then the TLB is updated to include the new page entry. 


Steps in TLB hit: 
 

CPU generates virtual (logical) address. 
 
It is checked in TLB (present). 
 
Corresponding frame number is retrieved, which now tells where in the main memory page lies. 
 
Steps in TLB miss: 
 

CPU generates virtual (logical) address. 
 
It is checked in TLB (not present). 
 
Now the page number is matched to page table residing in main memory (assuming page table contains all PTE). 
 
Corresponding frame number is retrieved, which now tells where in the main memory page lies. 
 
The TLB is updated with new PTE (if space is not there, one of the replacement technique comes into picture i.e either FIFO, LRU or MFU etc). 


https://www.indeed.com/career-advice/career-development/virtual-memory

https://www.geeksforgeeks.org/virtual-memory-in-operating-system/

Swapping a process out means removing all of its pages from memory, or marking them so that they will be removed by the normal page replacement process. Suspending a process ensures that it is not runnable while it is swapped out. At some later time, the system swaps back the process from the secondary storage to the main memory. When a process is busy swapping pages in and out then this situation is called thrashing. 