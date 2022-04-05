https://leetcode.com/discuss/interview-question/operating-system/125030/What-is-Virtual-Memory

virtual memory provide a logical address space which does not have 1v1 mapping with physical memory. The mapping between virtual memory to physical memory is done through a few levles of page tables. This essentially means that continuous address space of an application doest not have be contiguous in physical memory. Different non contiguous fragments of physical memory can be mapped to a contiguos virtual memory segment

One key function the OS provided is Virtualizing. virtual memory is used by the OS to provide the virtualizing on the physical memory. it makes the each process feel like it access the whole memory.

The main concept behind virtual memory is to increase the degree of multiprogramming. A process actually thinks all of its code is loaded into RAM when its running. Let's say this is a huge process, then putting all the code in RAM will take up too much space. So you only load a tiny portion of this code in RAM and leave the rest on the hard disk, and load it as you need. For example, think of your typical Word application, there are a ton of features that you rarely use. Putting all the code for that process in RAM is wasting memory. You can utilize memory by having independent jobs loaded in RAM.

Random Access Memory

https://www.enterprisestorageforum.com/hardware/virtual-memory/