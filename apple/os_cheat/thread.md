What is a Thread?
A thread is a path of execution within a process. A process can contain multiple threads.


Multi-threading is a bad idea if:

Several threads access and update the same resource (set a variable, write to a file), and you don't understand thread safety.

Several threads interact with each other and you don't understand mutexes and similar thread-management tools.

The process of switching between two executing processes on the CPU is called process context switching. Process context switching is expensive because the kernel has to save old registers and load current registers, memory maps, and other resources.


Let’s review the differences between processes and threads in the Linux context:

Process	Thread
A process is heavyweight.
A process has its own memory.
Inter-process communication is slower due to isolated memory.
Context switching between processes is expensive due to saving old and loading new process memory and stack info.
An application with several processes for its components can provide better memory utilization when memory is scarce. We can assign low priority to inactive processes in the application. This idle process is then eligible to be swapped to disk. This keeps the active components of the application responsive



A thread is a lightweight process also called an LWP.
A thread shares the memory with the parent process and other threads within the process.
Inter-thread communication is faster due to shared memory.
Context switching between threads is less expensive due to shared memory.
When memory is scarce, the multi-threaded application does not provide any provision to manage memory.


