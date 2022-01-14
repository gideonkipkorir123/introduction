def is_prime(num):
    num=int(input('enter value'))
    if num>1:
         for i in range(2,num//2):
             if (num % i) == 0:
                print(num,"is not a prime number")
         print(i,"times",num//i,"is",num)
    
    else:
        print(num,'is not prime number')
    is_prime(num)  