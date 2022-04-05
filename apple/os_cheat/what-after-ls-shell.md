https://medium.com/meatandmachines/what-really-happens-when-you-type-ls-l-in-the-shell-a8914950fd73

1. getline stdin and parse args

2. pass to program to executing 

3. check in ls is in alias, if exist in alias , use aliads replace the 'ls'

4. shell program look for binary in $PATH /usr/bin,/usr/sbin,/usr/local/bin,/usr/local/sbin

5. to execute ls , three system call will be called folk,exeve,wait 

6. fork is made to duplicate parent process, create a child process of parent process 

7. execve stop duplicated process , load up new process, replaces defining parts of the current process’ memory stack with the new stuff loaded from the ls executable file.

Meanwhile,
8. the parent process continues to do other things, keeping track of its children as well, using the system call wait().
If the executable binary (ls) file does not exist, an error will be printed. command not found

Lastly,
0. After ls -l is executed, the shell executes shutdown commands, frees up memory, exits, and re-prompts the user for input.

