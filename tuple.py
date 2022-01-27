# this is an immutable data 
# tuple=(1,2,3,4,)
# tuple_2=(5,6,7,8,9,41)
# # print(tuple[-1])
# for elem in tuple:
#     print(elem)


# the len() function accepts tuples, and returns the number of elements contained inside;
# the + operator can join tuples together (we've shown you this already)
# the * operator can multiply tuples, just like lists;
# the in and not in operators work in the same way as in lists.
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
