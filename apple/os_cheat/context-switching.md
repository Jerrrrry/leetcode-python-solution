Then with help of PID which is causing issue, one can get all system calls details:

Raw
# strace -c -f -p <pid of process/thread>
Let this command run for a few minutes while the load/context switch rates are high. It is safe to run this on a production system so you could run it on a good system as well to provide a comparative baseline. Through strace, one can debug & troubleshoot the issue, by looking at system calls the process has made.

vmstat

https://medium.com/geekculture/linux-cpu-context-switch-deep-dive-764bfdae4f01