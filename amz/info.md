Coding Round 1:
Given a pool of infinite positive numbers, write the following 2 methods:
out(): returns the next smallest positive number
in(): takes a positive integer which has to be stored back in the pool
Eg:
out() => 1
out() => 2
in(1)
int(4)
out() => 1
out() => 3
out() => 4
Solved by using a PriorityQueue (increasing order) and Integer variable.
Forgot to test a corner case of duplicate numbers, so changed to using a TreeSet instead of PriorityQueue on interviewers feedback. (eg in(5), in(5) should not give 5 twice.)

Coding Round 2:
Given several files (diff types, sizes etc) how would you write extensible/modular code that can filter these files based on file types and/or file size, name etc
Eg: Give all files of type XML, Give all files of type text which are greater than 5MB in size, Give all files with name "foo"
Interviewer mentioned the question is intentionally open ended.
I was coding using java, used the filter design pattern https://www.tutorialspoint.com/design_pattern/filter_pattern.htm
Also discussed the pros how different types of files and Filters could be easily created by implementing File interface and Filter interface.

##################################

Adding links for the questions:

Looks like it is: https://leetcode.com/discuss/interview-question/233869/Design-Amazon-Locker-system
https://leetcode.com/problems/merge-k-sorted-lists/
https://leetcode.com/problems/implement-strstr/


https://leetcode.com/discuss/interview-question/1946226/Amazon-SDE-or-Onsite-Loop-or-Rejected

https://leetcode.com/problems/largest-rectangle-in-histogram/

https://leetcode.com/discuss/interview-question/1725495/Amazon-Onsite-Experience-or-2022

https://leetcode.com/discuss/interview-question/1690696/Amazon-or-onsite-or-seattle-or-SDE-1-2-or-Dec-2021-or-REJECT


https://leetcode.com/discuss/interview-question/1671315/Amazon-or-Onsite-or-SDE1-or-Seattle