What is a process in OS and What are the different states of a process?

A process is a program in execution. For example, when we write a program in C or C++ and compile it, the compiler creates binary code. The original code and binary code are both programs. When we actually run the binary code, it becomes a process. 

1. New: Newly Created Process (or) being-created process.

2. Ready: After creation process moves to Ready state, i.e. the 
          process is ready for execution.

3. Run: Currently running process in CPU (only one process at
        a time can be under execution in a single processor).

4. Wait (or Block): When a process requests I/O access.

5. Complete (or Terminated): The process completed its execution.

6. Suspended Ready: When the ready queue becomes full, some processes 
                    are moved to suspended ready state

7. Suspended Block: When waiting queue becomes full.