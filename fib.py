def fib(n):
    if n <1:
        return None
    if n <3:
        return 1
    num_1=num_2=1
    sum_1=0
    for n in range (3, n+1):
         sum_1= num_2+ num_1
         num_1,num_2=num_2,sum_1
    return sum_1
        
for n in range  (1,10):
    print (n,fib(n))
    


