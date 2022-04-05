what happen after ls 

[pathak_home@toolbox ~]$ strace -f -etrace=execve,clone bash -c '{ ls; }'
execve("/usr/bin/bash", ["bash", "-c", "{ ls; }"], 0x7fff153d0ed0 /* 36 vars */) = 0
clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLDstrace: Process 115538 attached
, child_tidptr=0x7fe8b4f10a10) = 115538
[pid 115538] execve("/usr/bin/ls", ["ls"], 0x55eed8e42be0 /* 36 vars */) = 0
Desktop  Documents  Downloads  Dropbox	IdeaProjects  Music  Pictures  Public  Templates  Videos  revision  soft
[pid 115538] +++ exited with 0 +++
--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=115538, si_uid=1000, si_status=0, si_utime=0, si_stime=0} ---
+++ exited with 0 +++

We can observe from the output above that it takes two steps to create a process:

The clone system call creates the process as a clone of the bash process
The execve system call then replaces the executable in the process with the ls command binary
Another important point is that even though we say the child process is a copy/clone of the parent with the same address space, implementation-wise, Linux does not copy the child’s memory until the child writes. This clever implementation of the process in Linux saves RAM space and avoids unnecessary memory allocation. This implementation is also called Copy on Write (COW).