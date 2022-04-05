consider disk performance 

1. time it takes to find the right block

2. time it read data 

3. time it ued to put data in memory 

short is good 

dstat -d

check linux log 

cd /var/log 

atop | grep DSK

The df command stands for disk free, and it shows you the amount of space taken up by different drives.

[root@VM-20-4-centos ~]$ df -h 
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        3.9G     0  3.9G   0% /dev
tmpfs           3.9G   24K  3.9G   1% /dev/shm
tmpfs           3.9G  636K  3.9G   1% /run
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/vda1       197G  5.1G  184G   3% /
tmpfs           783M     0  783M   0% /run/user/0


devtmpfs is a kernel maintained filesystem of automated device nodes. tmpfs is a RAM disk.


tmpfs           3.9G   24K  3.9G   1% /dev/shm

virtual memory 

inode 

ls -li 

find / -inum 11272717


Let’s use the -B (block size) option to specify a block size of 4096 bytes and check the regular disk usage:

df -B 4096 /dev/sda1



inode read metadata

11272717 beta_db.conf

sudo debugfs -R "stat <11272717>" /dev/sda1

As we’ve covered, three components are required to have a well-formed and accessible file in the file system: the file, the directory structure, and the inode. The file is the data stored on the hard drive, the directory structure contains the name of the file and its inode number, and the inode contains all the metadata for the file.


What are Soft Links?
Quick definition: In Linux, a soft link, also known as a symbolic link, is a special sort of file that points at a different file. In Windows vocabulary, you could think of it like a shortcut. Because the connection is a logical one, and not a duplication, soft links can point at entire directories or link to files on remote computers. Hard links cannot do this.

What are Hard Links?
Quick definition: In the Linux operating system, a hard link is equivalent to a file stored in the hard drive – and it actually references or points to a spot on a hard drive. A hard link is a mirror copy of the original file. The distinguishing characteristic of a hard link from a soft link is that deleting the original file doesn't affect a hard link, while it renders a soft link inoperable.

softlink 

ln -s new old (shorcut)

ln new old ( copy)

Inode Overheads
it’s a neat system, but there are overheads. To read a file, the file system has to do all the following:

Find the right directory structure
Read the inode number
Find the right inode
Read the inode information
Follow either the inode links or the extents to the relevant disk blocks
Read the file data