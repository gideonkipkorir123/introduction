# itertools are products and permutations that accumulate infinite iterators
# they consist product,permuation,combination,accumulate,group by and iterators
# product gives the possible combination of characters in a list
# from itertools import product
# from timeit import repeat
# a=[1,2]
# b=[3,4]
# x=product(a,b ,repeat=1)
# print(list(x))
# from itertools import permutations
# x=[1,2,3,4]
# y=permutations(x,4)
# print(list(y))
# from itertools import combinations,combinations_with_replacement
# x=[1,2,3,4,5]
# y=combinations(x,2)
# z=combinations_with_replacement(x,2)
# print(list(z)
# )
# print(list(y))
# from itertools import accumulate
# import operator
# x=[1,2,3,4]
# y=accumulate(x,func=max)
# print(list(x))
# print(list(y))
# from itertools import groupby
# students =[{"name":"Tim","age":25,"sex":"male"},
#     {"name":"Gideon","age":27,"sex":"male"},

# {"name":"mike","age":26,"sex":"male"
# }]
# y=groupby(students,key=lambda x:x["age"])
# for key,value  in y:
#     print(key,list(value))
from itertools import count,cycle,repeat
# for i in count(1):
#     print(i)
#     if    i==15:

#          break
x=[1,2,3,4]
for i in cycle(x):
    print(i)
    if i==4:
        break
