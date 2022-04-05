Paging and Segmentation are the two ways which allow a process’s physical address space to be non-contiguous. It has advantage of reducing memory wastage but it increases the overheads due to address translation. It slows the execution of the memory because time is consumed in address translation. 


paging 

In paging, program is divided into fixed or mounted size pages.

page frame 4k

For paging operating system is accountable.

Page size is determined by hardware.

It is faster in the comparison of segmentation.

Paging could result in internal fragmentation.

Internal fragmentation occurs when we split the physical memory into contiguous mounted-sized blocks and allocate memory for a process that can be larger than the memory requested. 

In paging, logical address is split into page number and page offset.

Paging comprises a page table which encloses the base address of every page.

Page table is employed to keep up the page data.

In paging, operating system must maintain a free frame list.

Paging is invisible to the user.


In paging, processor needs page number, offset to calculate absolute address.


It is hard to allow sharing of procedures between processes. 


In paging, a programmer cannot efficiently handle data structure.


In this protection is hard to apply.




Segment
In segmentation, program is divided into variable size sections.

Here, the section size is given by the user.

Segmentation is slow.

Segmentation could result in external fragmentation.

Here, logical address is split into section number and section offset.

While segmentation also comprises the segment table which encloses segment number and segment offset.

Section Table maintains the section data.

In segmentation, operating system maintain a list of holes in main memory.


	Segmentation is visible to the user.

In segmentation, processor uses segment number, offset to calculate full address.

Facilitates sharing of procedures between the processes.

It can efficiently handle data structures.

Easy to apply protection in segmentation.

internal/external fragmentation 

https://www.geeksforgeeks.org/difference-between-internal-and-external-fragmentation/

