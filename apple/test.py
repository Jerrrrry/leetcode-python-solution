n=14
print(bin(n))
#101
n|=n>>1
print(bin(n))

n|=n>>2
print(bin(n))

n|=n>>4
print(bin(n))

n|=n>>8
print(bin(n))

n|=n>>16
print(bin(n))
print(n)


