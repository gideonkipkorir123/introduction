def factorials(n):
    if n==1:
     return 1
    else:
        return n * factorials(n-1)
for n in range (1,10):
    print(n,factorials(n))    

