tar -czvf name.tar.gz /xx /xx /xx

mkdir -p /tmp/2022

create folder without error 

mkdir -p -v /test/test

man mkdir 

describe the function/

shutdown /halt

less/tail/head

wc test.md

1,number of lines 2, number of word , 3 number of characters

uname 
-s, (--kernel-name) - Prints the kernel name.
-n, (--nodename) - Prints the system’s node name (hostname). This is the name the system uses when communicating over the network. When used with the -n option, uname produces the same output as the hostname command.
-r, (--kernel-release) - Prints the kernel release.
-v, (--kernel-version) - Prints the kernel version.
-m, (--machine) - Prints the name of the machine’s hardware name.
-p, (--processor) - Prints the architecture of the processor.
-i, (--hardware-platform) - Prints the hardware platform.
-o, (--operating-system) - Print the name of the operating system. On Linux systems that is “GNU/Linux”
-a, (--all) - When the -a option is used, uname behaves the same as if the -snrvmo options have been gi


sed 's/a/b/'  xx.txt 

replace a first time with b 

sed 's/a/b/2'  xx.txt 

replace second a to b 

sed 's/a/b/g'  xx.txt 


tr -s 'a' 'b'

replace a with b 

sort -r sss.txt 

reverse the result 

sort -k 2

sort 2nd column

sort -u 

sort and remove duplicate



diff 

diff a b 

diff -c 

context mode 


cmp a  b

awk 

awk '/manager/ {print}' xx.txt

tcpdump -i -c 100 -vv -t port 80 -w xxx.file


tcpdump host xxxxxxxx


telnet xxx port 

connected 

which means success 


nc 


echo 'ssssssss' | nc -4u host port 

receiving 

nc -l port > write_to_file

sending 

nc host port < file
