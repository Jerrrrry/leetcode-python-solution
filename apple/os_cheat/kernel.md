uname -r : Find Linux kernel version.
cat /proc/version : Show Linux kernel version with help of a special file.
hostnamectl | grep Kernel : For systemd based Linux distro you can use hotnamectl to display hostname and running Linux kernel version.

Linux uses an open-source, Monolithic Kernel
macOS and Windows both use Hybrid Kernels.

Whenever a system starts, the Kernel is the first program that is loaded after the bootloader because the Kernel has to handle the rest of the thing of the system for the Operating System. The Kernel remains in the memory until the Operating System is shut-down.

The Kernel is responsible for low-level tasks such as disk management, memory management, task management, etc. It provides an interface between the user and the hardware components of the system. When a process makes a request to the Kernel, then it is called System Call.

Functions of a Kernel
Following are the functions of a Kernel:

Access Computer resource: A Kernel can access various computer resources like the CPU, I/O devices and other resources. It acts as a bridge between the user and the resources of the system.

Resource Management: It is the duty of a Kernel to share the resources between various process in such a way that there is uniform access to the resources by every process.

Memory Management: Every process needs some memory space. So, memory must be allocated and deallocated for its execution. All these memory management is done by a Kernel.

Device Management: The peripheral devices connected in the system are used by the processes. So, the allocation of these devices is managed by the Kernel.

type of kernel 

1. monolithic kernel 

software -> kernel -> hardware

cons: all in one , one fail for all 

2. microkernel 

memory , resouce sepereated 
easy add new source 

communication consume resource 



3 hybridkernel 
monolithic + micro



