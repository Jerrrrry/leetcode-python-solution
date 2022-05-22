Your company is building 5 new data centers from scratch located in these locations:
    * North America
    * South America
    * EMEA
    * Asia
    * Africa
 
* Each datacenter has about 10,000 servers, but has the capacity to grow. 
* The goal is:
    *  to provision CentOS/RHEL/Oracle Linux 7 on all 50,000 servers within 48 hours using a definition stored in the North America data center, 
    * perform basic OS configuration, 
    * and install OS patches and core applications (about 10GB in size) on each server. 
* The server count is expected to grow to ~250,000 within 5 years and HW refresh cycles is every 5 years. 
 
After the initial deployment, this provisioning system will be used for on-going operations, such as patching, repair/replacements, and hardware refresh.


commit to coustmer but you dont 


Given
* S: A String - Representing the string from which characters will be removed
* x : An Integer - Initially, all substrings of S of length x contain only unique characters

Produce
A function canRemove(S : String, x : Int, index : Int) : Bool which:
* returns true if the character at index index can be removed from S and still maintain the invariant that any given substring of length x must contain only unique characters.
* returns false otherwise.
EXAMPLE 
Given : 
  S = "ababcab"
  x = 2
  
call1 : canRemove(S, x, 1) -> false 
call2 : canRemove(S, x, 4) -> true