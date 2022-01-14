# this is a function that executes a specified function for each item.the function is sent to the function as a parameter
# syntax map(function,iterable)
# def myfunct(a,b):
#     return a+b
#     x=map(myfunct,('apple','orange'))
#     print(x)
def addition(a):
    return a+a
numbers=[1,2,3,3,4,5,6,7,8,9]
result=map(addition,numbers)
print(list(result))


